# Tests de Excepciones - benchmark_ingestor

Este documento explica **que prueban estos tests**, **por que existen** y **como ejecutarlos** correctamente.

---

## 1. Que se esta probando

Los tests ubicados en `tests/test_exceptions.py` validan **el sistema de excepciones** del proyecto.

Concretamente prueban:

1. Que todas las excepciones heredan de `BenchmarkError`
2. Que las excepciones pueden lanzarse (`raise`) y capturarse correctamente

No prueban logica de negocio, solo **diseño y comportamiento minimo**.

---

## 2. Archivo bajo prueba

```text
benchmark_ingestor/
├── exceptions.py
tests/
├── test_exceptions.py
```

---

## 3. Tests de herencia (arquitectura)

Ejemplo:

```python
def test_storage_error_is_benchmark_error():
    assert issubclass(StorageError, BenchmarkError)
```

Este test valida que:

- `StorageError` hereda de `BenchmarkError`
- Se puede capturar cualquier error del sistema usando:
  
```python
except BenchmarkError:
    ...
```

Estos tests protegen el **contrato del core**.

---

## 4. Test de raise y captura (runtime)

Ejemplo:

```python
def test_raise_and_catch_invalid_payload_error():
    with pytest.raises(InvalidPayloadError):
        raise InvalidPayloadError("Invalid payload")
```

Este test valida que:

- La excepcion se puede instanciar
- Se puede lanzar con `raise`
- Pytest puede capturarla correctamente

---

## 5. Requisitos para ejecutar los tests

Asegurate de tener:

- Python 3.9 o superior
- pytest instalado

Instalar pytest:

```bash
pip install pytest
```

---

## 6. Como ejecutar los tests

Desde la **raiz del proyecto**, ejecuta:

```bash
pytest
```

Esto:

- Detecta automaticamente archivos `test_*.py`
- Ejecuta todos los tests
- Muestra un resumen

---

## 7. Ejecutar solo los tests de excepciones

```bash
pytest tests/test_exceptions.py
```

---

## 8. Salida esperada

Si todo esta correcto veras algo como:

```text
================== test session starts ==================
collected 4 items

tests/test_exceptions.py ....

=================== 4 passed in 0.05s ===================
```

---

## 9. Cuando fallan estos tests

Estos tests fallan si:

- Una excepcion deja de heredar de `BenchmarkError`
- Se elimina o renombra una excepcion
- Se rompe la jerarquia de errores

Esto es intencional: protege el diseño.

---

## 10. Regla mental

- Estos tests **no prueban funcionalidades**
- Prueban **estructura y contratos**
- Son baratos, rapidos y criticos

---

## 11. Conclusión

Si estos tests pasan:

- El sistema de errores esta sano
- La arquitectura base esta protegida
- El core es estable

Estos tests son la **primera linea de defensa** del proyecto.
