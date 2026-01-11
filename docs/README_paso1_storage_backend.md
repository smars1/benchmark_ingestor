# Paso 1 – Contrato de Storage (StorageBackend)

Este documento explica **que es StorageBackend**, **por que se creo**, **que significa la validacion con `python -c`**
y **a que pruebas nos referimos cuando hablamos de pytest en este paso**.

Este paso corresponde a la **Arquitectura B** y se implementa sin romper la version 0.0.1.

---

## 1. Contexto

Antes del paso 1, el proyecto tenia estas caracteristicas:

- `client.py` y `history.py` acoplados directamente a boto3
- AWS S3 usado de forma directa
- Tests existentes solo para excepciones
- No existia una abstraccion de almacenamiento

Para poder avanzar a multicloud **sin rehacer pruebas**, primero se definio un **contrato**.

---

## 2. Que es StorageBackend

`StorageBackend` es una **interfaz (contrato)** que define:

> “Que operaciones minimas necesita el core para trabajar con object storage”

No implementa AWS, OCI ni ningun cloud.
Solo define **que metodos deben existir**.

Archivo:

```text
benchmark_ingestor/core/storage.py
```

---

## 3. Codigo del contrato

```python
class StorageBackend(ABC):

    def put_json(self, key, data, cache_control=None):
        pass

    def get_json(self, key):
        pass
```

Este contrato representa:

- Guardar JSON en una clave
- Leer JSON desde una clave

Eso es todo lo que el core necesita saber.

---

## 4. Por que NO hay boto3 aqui

Este archivo **no importa boto3** a proposito.

Motivos:

- El core no debe depender de SDKs cloud
- El core debe poder testearse sin red
- El core debe funcionar igual en AWS, OCI, GCP o local

Los SDKs viven en `providers/*`, no en `core/*`.

---

## 5. Que significa el comando `python -c`

Ejecutaste:

```powershell
python -c "from benchmark_ingestor.core.storage import StorageBackend; print(StorageBackend)"
```

Esto hace lo siguiente:

1. Python intenta importar el modulo
2. Verifica que el paquete esta bien instalado
3. Confirma que `core/` es un subpaquete valido
4. Imprime la referencia a la clase

La salida:

```text
<class 'benchmark_ingestor.core.storage.StorageBackend'>
```

Significa:

- El paquete esta bien instalado (`pip install -e .`)
- La ruta `benchmark_ingestor.core.storage` es valida
- No hay errores de import
- El contrato esta disponible para el resto del proyecto

Este comando es una **validacion rapida de arquitectura**, no un test funcional.

---

## 6. Por que este paso no rompe nada

En el paso 1:

- No se modifica `client.py`
- No se modifica `history.py`
- No se cambia comportamiento
- No se agregan dependencias nuevas

Solo se **define una interfaz** que aun no se usa.

Por eso, la version 0.0.1 sigue funcionando igual.

---

## 7. A que pruebas nos referimos con pytest aqui

Cuando se dijo “corre pytest”, **no se refiere a nuevas pruebas**.

Se refiere a:

> Ejecutar los tests existentes para confirmar que no rompimos nada.

En este punto, pytest solo valida:

- `test_exceptions.py`
- Que el paquete sigue importable
- Que no hay errores colaterales

Comando:

```powershell
pytest
```

Si pasa, significa que:
- La arquitectura nueva no rompio la anterior
- El contrato se agrego correctamente

---

## 8. Que pruebas NO existen aun

En el paso 1 **todavia NO existen**:

- Tests para StorageBackend
- Tests para ingestor multicloud
- Tests para history con storage inyectado

Eso viene en el paso 2 y 3.

---

## 9. Por que este paso es importante aunque parezca simple

Porque:

- Define el punto de desacople entre core y cloud
- Evita imports directos a SDKs en el core
- Permite crear LocalStorage para tests
- Permite cambiar de cloud sin tocar el core

Es un paso de **arquitectura**, no de feature.

---

## 10. Regla mental

> Si el core depende de una interfaz y no de boto3,
> entonces el core es testeable sin cloud.

Este paso hace exactamente eso.

---

## 11. Proximo paso

Con el contrato definido y validado:

**Paso 2: crear `LocalStorage` (storage en memoria) y escribir el primer test del core sin AWS.**

Ese sera el primer test realmente multicloud.
