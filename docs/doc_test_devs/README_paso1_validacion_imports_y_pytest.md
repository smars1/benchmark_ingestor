# Paso 1 – Validacion estructural y pruebas (explicacion detallada)

Este documento explica en detalle **que hace el comando `python -c`**, **por que se uso en el Paso 1**,
y **a que nos referimos cuando decimos “corre pytest”**, sin introducir nuevas pruebas aun.

Corresponde al **Paso 1 de la Arquitectura B**, manteniendo la version 0.0.1 estable.

---

## 1. Que es `python -c`

El comando:

```bash
python -c "from benchmark_ingestor.core.storage import StorageBackend; print(StorageBackend)"
```

le indica a Python:

> Ejecuta este codigo directamente en el interprete y termina.

No es un script, no es pytest y no es un test funcional.
Es una **ejecucion directa del sistema de importacion de Python**.

---

## 2. Que hace Python internamente

Cuando se ejecuta el comando, Python realiza los siguientes pasos:

1. Arranca el interprete correcto (el del entorno virtual activo)
2. Carga `site-packages`
3. Construye `sys.path`
4. Detecta que `benchmark_ingestor` esta instalado en modo editable
5. Intenta resolver el import solicitado

Este proceso es identico al que ocurre cuando una aplicacion real importa modulos.

---

## 3. Resolucion del import paso a paso

La instruccion:

```python
from benchmark_ingestor.core.storage import StorageBackend
```

se resuelve asi:

1. Python busca el paquete `benchmark_ingestor`
2. Encuentra el paquete en `site-packages` (instalacion editable)
3. Busca el subpaquete `core`
4. Verifica que `core` tiene `__init__.py`
5. Carga el modulo `storage.py`
6. Ejecuta su codigo
7. Encuentra la clase `StorageBackend`

Si alguno de estos pasos fallara, el comando lanzaria un error.

---

## 4. Significado de la salida

La salida:

```text
<class 'benchmark_ingestor.core.storage.StorageBackend'>
```

significa:

- El paquete esta correctamente instalado
- El subpaquete `core` es valido
- El modulo `storage.py` se cargo sin errores
- La clase `StorageBackend` existe
- La ruta absoluta del import es correcta

Esto valida la **estructura del proyecto**, no su comportamiento.

---

## 5. Por que esto es una validacion de arquitectura

Este comando valida aspectos que los tests aun no validan:

- Integridad del arbol de paquetes
- Rutas de import estables
- Instalacion editable correcta
- Separacion fisica del core

Por eso se considera una **validacion estructural**, no un test.

---

## 6. Por que este paso no rompe la version 0.0.1

En el Paso 1:

- No se modifica `client.py`
- No se modifica `history.py`
- No se altera ninguna logica existente
- No se agregan dependencias nuevas

Solo se agrega un contrato que aun no se utiliza.

Por eso, el comportamiento de la version 0.0.1 permanece intacto.

---

## 7. A que pruebas nos referimos con pytest

Cuando se indica:

```bash
pytest
```

no se estan pidiendo pruebas nuevas.

Se refiere a:

> Ejecutar los tests existentes para confirmar que no se introdujeron errores colaterales.

En este punto, pytest valida:

- `test_exceptions.py`
- Que el paquete sigue siendo importable
- Que no hay errores indirectos

Esto se conoce como **regression check**.

---

## 8. Que pruebas aun no existen

En el Paso 1 todavia NO existen:

- Tests para `StorageBackend`
- Tests para `LocalStorage`
- Tests para `BenchmarkIngestor` desacoplado
- Tests para `history` desacoplado

Estas pruebas se introducen en los Pasos 2 y 3.

---

## 9. Por que este paso es importante aunque parezca simple

Porque:

- Define el punto exacto de desacople entre core y cloud
- Evita dependencias futuras a SDKs cloud en el core
- Permite testing local sin credenciales
- Habilita una arquitectura multicloud real

Es un paso de **arquitectura**, no de funcionalidad.

---

## 10. Regla mental clave

> Si el core se puede importar sin SDKs cloud,
> entonces el core es portable y testeable.

El comando `python -c` confirma exactamente eso.

---

## 11. Proximo paso

Con la validacion estructural completa:

**Paso 2: Implementar `LocalStorage` y escribir el primer test real del core sin cloud.**

A partir de ahi, el desacople se vuelve funcional.
