# Nota de diseno: Multicloud + Object Storage + Frontend (Benchmark Ingestor)

Este documento resume y documenta en detalle la conversacion sobre como volver el proyecto **multicloud** sin rehacer pruebas, y como se relaciona con el **frontend** que consume JSON.

---

## 1. Objetivo

El objetivo es convertir `benchmark_ingestor` en un proyecto **multicloud** sin reescribir tests ni duplicar codigo.

La idea central:

- El **core** (logica) no debe saber en que cloud corre
- Los **providers** (adaptadores) son los que hablan con AWS / OCI / GCP / Azure
- El **frontend** solo consume JSON via HTTP y se acopla minimamente a su host mediante una URL base configurable

---

## 2. Que estamos haciendo hoy con AWS (en terminos funcionales)

El proyecto usa S3 para un patron muy especifico:

- Guardar JSON de ejecuciones (history)
- Guardar indices JSON (jobs/index.json y history/index.json)
- Guardar latest.json para consumo rapido del frontend
- Opcionalmente controlar cache (Cache-Control no-store) para evitar que un CDN sirva contenido viejo

Esto es **object storage basico** (key -> object). No depende de caracteristicas avanzadas exclusivas de AWS.

---

## 3. Los otros clouds pueden hacer lo mismo?

Si. Para este caso de uso, los proveedores cloud tienen equivalentes directos:

- AWS: S3
- GCP: Cloud Storage
- Azure: Blob Storage
- OCI: Object Storage

Todos soportan:

- Put object (escritura)
- Get object (lectura)
- Objetos publicos o firmados para consumo via HTTP
- Cabeceras de cache (equivalentes a Cache-Control)
- SDK en Python para automatizar

Para el patron actual (guardar y servir JSON), la funcionalidad es equivalente.

---

## 4. Por que esta abstraccion tiene sentido

El diseno multicloud no busca "copiar AWS". Busca abstraer el minimo comun denominador:

- Un backend de storage que permita escribir y leer objetos por key

Por eso se propone una interfaz tipo:

- put_json(key, data, cache_control=None)
- get_json(key) -> dict

Esta interfaz es portable entre clouds.

---

## 5. Que parte se acopla realmente al cloud o al host?

### 5.1 Core (no se acopla)

El core no debe acoplarse a:

- boto3
- oci sdk
- google-cloud-storage
- azure-storage-blob

El core solo llama al contrato de storage y ejecuta la logica de indices y estructura de datos.

### 5.2 Providers (si se acoplan, por diseno)

Los providers contienen el acoplamiento intencional:

- AWS provider encapsula boto3 y detalles de S3
- OCI provider encapsula oci sdk y detalles de Object Storage
- etc.

Esta capa es la que cambia segun el cloud.

### 5.3 Frontend (se acopla minimamente al host)

El frontend siempre vive en algun host (CDN/bucket/VM/container). Por eso su acoplamiento real es:

- La URL base desde donde consume los JSON

El frontend no se acopla al SDK cloud; solo a una ruta HTTP.

---

## 6. Frontend serverless vs frontend en VM/container

### Caso A: frontend serverless (bucket + CDN)

El frontend hace requests tipo:

- GET /jobs/index.json
- GET /jobs/<job_id>/latest.json
- GET /jobs/<job_id>/history/index.json

El host puede ser CloudFront, CDN, o el propio bucket.

### Caso B: frontend en VM o container

El frontend sigue consumiendo JSON por HTTP. Puede:

- leer desde el mismo CDN/bucket (recomendado)
- o exponer un proxy/backend que los sirva

Importante: el contrato de datos (los JSON) no cambia. Solo cambia la URL base.

---

## 7. Como evitar que el frontend quede hardcodeado a un host

Recomendacion: nunca hardcodear URLs en el codigo JS.

Se debe usar una configuracion por entorno, por ejemplo:

- variable de entorno (VITE_DATA_BASE_URL, NEXT_PUBLIC_DATA_BASE_URL)
- archivo config.json servido junto con la app
- parametros de build/deploy

Ejemplo conceptual:

- DATA_BASE_URL = "https://cdn.example.com/jobs/"

Cambiar de cloud o hosting se vuelve un cambio de configuracion, no de codigo.

---

## 8. Resultado esperado del diseno

Con este diseno se logra:

- Core cloud-agnostic
- Providers intercambiables (AWS/OCI/GCP/Azure/Local)
- Tests estables (no dependen del cloud)
- Frontend portable (solo cambia la URL base configurable)
- Evolucion facil: serverless hoy, VM/container manana, sin cambiar el contrato JSON

---

## 9. Regla mental final

- El core no habla con la nube
- La nube se adapta al core (providers)
- El frontend solo apunta a una URL de datos

---

## 10. Siguientes pasos sugeridos (cuando se retome)

- Definir interfaz StorageBackend en core
- Implementar provider AWS (S3) usando boto3
- Implementar provider Local (filesystem o memoria) para tests
- Refactorizar history/client para recibir el storage inyectado
- Documentar contrato JSON consumido por el frontend (versionado)
