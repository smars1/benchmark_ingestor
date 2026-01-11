# Arquitectura B – Multicloud, Testeable y Cloud-Agnostic

Este documento explica **por que se eligio la Arquitectura B**, que problema resuelve,
y como permite **testear todo el core sin conectarse a ningun cloud**.

---

## 1. Contexto

El proyecto `benchmark_ingestor` nacio inicialmente acoplado a AWS S3.
Esto funcionaba, pero generaba problemas a mediano plazo:

- Dificultad para soportar multiples clouds (OCI, GCP, Azure)
- Tests dependientes de credenciales y red
- Riesgo de rehacer pruebas al cambiar de proveedor
- Core acoplado a SDKs (boto3)

El objetivo fue redisenar la arquitectura **sin romper funcionalidad ni tests existentes**.

---

## 2. Decision arquitectonica

Se eligio la **Arquitectura B**, basada en separacion estricta de responsabilidades:

- El **core** contiene toda la logica de dominio
- Los **providers** encapsulan los SDKs cloud
- El **cliente** solo ensambla dependencias
- El **frontend** consume JSON via HTTP y solo depende de una URL base

Esta arquitectura permite evolucionar el sistema sin deuda tecnica.

---

## 3. Estructura de carpetas (Arquitectura B)

```text
benchmark_ingestor/
├── __init__.py
│
├── core/
│   ├── __init__.py
│   ├── storage.py        # contrato de almacenamiento (interfaz)
│   ├── history.py        # logica pura de indices
│   └── ingestor.py       # BenchmarkIngestor (flujo principal)
│
├── providers/
│   ├── aws/
│   │   └── storage.py    # implementacion S3 (boto3)
│   ├── oci/
│   │   └── storage.py    # implementacion OCI (futuro)
│   └── local/
│       └── storage.py    # storage local (tests y desarrollo)
│
├── schema.py             # validacion de payload (pura)
├── utils.py              # helpers (keys, timestamps)
├── exceptions.py         # jerarquia de errores
├── factories.py          # seleccion de provider
└── client.py             # wrapper / entrypoint
```

---

## 4. Principio clave del diseno

> **El core no sabe en que cloud corre.**  
> **El cloud se adapta al core mediante providers.**

El core no importa SDKs, no conoce buckets, ni credenciales.
Solo interactua con contratos.

---

## 5. Contrato de almacenamiento (idea central)

El core trabaja con una interfaz minima de almacenamiento:

- Guardar JSON por key
- Leer JSON por key
- Opcionalmente controlar cache

Ejemplo conceptual:

```python
storage.put_json(key, data)
storage.get_json(key)
```

Mientras un provider cumpla este contrato, el core funciona igual.

---

## 6. Testing sin cloud (beneficio principal)

Gracias a esta arquitectura:

- El core puede testearse con `LocalStorage`
- No se requiere AWS, OCI, GCP ni Azure
- No se requieren credenciales
- No se requiere acceso a red

Ejemplo conceptual de uso local:

```python
storage = LocalStorage()
ingestor = BenchmarkIngestor(storage)
ingestor.ingest(payload)
```

Esto permite tests:
- rapidos
- deterministas
- ejecutables en cualquier entorno (local o CI)

---

## 7. Que SI se testea sin cloud

- Validacion de payload (`schema`)
- Generacion de keys (`utils`)
- Actualizacion de indices (`core/history`)
- Flujo completo de ingesta (`core/ingestor`)
- Manejo de errores (`exceptions`)

Todo esto se prueba sin dependencias externas.

---

## 8. Que queda fuera del core

El acceso real al cloud vive en `providers/*`:

- AWS: boto3 + S3
- OCI: oci sdk + Object Storage
- GCP: google-cloud-storage
- Azure: azure-storage-blob

Estos providers pueden tener:
- tests de integracion
- configuraciones especificas
- credenciales

Pero **no contaminan el core**.

---

## 9. Relacion con el frontend

El frontend:

- Consume JSON via HTTP
- Solo depende de una URL base configurable
- No conoce el cloud ni el SDK

Cambiar de cloud o de hosting implica:
- cambiar la URL base
- no cambiar el contrato de datos

---

## 10. Beneficios obtenidos

Con esta arquitectura se logra:

- Multicloud real
- Tests locales sin cloud
- Core reutilizable
- Menor deuda tecnica
- Facil CI/CD
- Frontend portable

---

## 11. Regla mental final

- El core no habla con la nube
- La nube se adapta al core
- Los tests no requieren cloud
- El frontend solo apunta a una URL

---

## 12. Proximo paso

Con esta decision documentada, el siguiente paso es:

**Paso 1: definir la interfaz `StorageBackend` en `core/storage.py`.**

A partir de ahi se implementan los providers sin romper nada existente.
