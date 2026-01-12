# Tests de LocalStorage (Paso 2)

Este documento describe en detalle los tests implementados para `LocalStorage`,
por que existen, que validan exactamente y cuando deben integrarse a `main`
antes de continuar con el Paso 3.

---

## 1. Contexto

En el Paso 2 se implemento `LocalStorage` como un provider local que cumple
el contrato `StorageBackend`.

El objetivo principal fue:
- Permitir tests sin cloud
- Validar el contrato de almacenamiento
- Preparar el refactor del core sin riesgo

Antes de avanzar al Paso 3, es correcto documentar y estabilizar estos tests.

---

## 2. Tests implementados

Archivo:
```
test/test_local_storage.py
```

Codigo:

```python
import pytest
from benchmark_ingestor.providers.local.storage import LocalStorage

def test_local_storage_put_and_get():
    storage = LocalStorage()
    storage.put_json("a.json", {"x": 1})
    assert storage.get_json("a.json") == {"x": 1}

def test_local_storage_missing_key():
    storage = LocalStorage()
    with pytest.raises(FileNotFoundError):
        storage.get_json("missing.json")
```

---

## 3. Test 1: test_local_storage_put_and_get

### Proposito
Validar que LocalStorage puede:
- Guardar un objeto JSON
- Recuperarlo sin alteraciones

### Paso a paso

1. Se crea una instancia nueva de LocalStorage
2. Se guarda un JSON bajo la key "a.json"
3. Se recupera el JSON
4. Se compara el resultado exacto

### Que valida este test
- El metodo put_json funciona
- El metodo get_json devuelve los datos correctos
- No hay transformaciones silenciosas
- El storage respeta el contrato basico

---

## 4. Test 2: test_local_storage_missing_key

### Proposito
Validar el comportamiento cuando se intenta leer una key inexistente.

### Paso a paso

1. Se crea una instancia vacia de LocalStorage
2. Se intenta leer "missing.json"
3. Se espera una excepcion FileNotFoundError

### Que valida este test
- El storage NO devuelve None
- El storage NO crea datos por defecto
- El storage falla de forma explicita

---

## 5. Relacion con arquitectura multicloud

Estos tests aseguran que:
- Todos los providers fallen igual ante una key inexistente
- El core pueda manejar errores sin saber el cloud
- No haya diferencias sutiles entre SDKs

---

## 6. Debe integrarse a main antes del Paso 3?

### Respuesta corta: SI, es recomendable

### Por que

En este punto:
- No hay cambios funcionales
- No hay refactors del core
- Los tests son estables
- El riesgo es minimo

Integrar ahora a main:
- Estabiliza la base
- Reduce el tamaño de cambios futuros
- Permite que el Paso 3 se base en una version probada

---

## 7. Flujo recomendado de ramas

1. feature/provider-local-storage
2. Merge a dev
3. Validar tests en dev
4. Merge a main
5. Crear nueva feature: feature/core-ingestor-refactor

---

## 8. Criterio de salida del Paso 2

El Paso 2 se considera completo cuando:
- LocalStorage esta implementado
- Tests documentados
- pytest pasa en limpio
- Cambios integrados a main

---

## 9. Proximo paso

Paso 3: mover BenchmarkIngestor al core y escribir el primer test de flujo completo sin AWS.
