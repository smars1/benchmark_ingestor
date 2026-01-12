# Paso 2 – LocalStorage: Explicacion y estrategia de tests

Este documento explica:
1) Que hace el comando `python - << EOF`
2) Como valida LocalStorage
3) Que tipos de tests vamos a escribir
4) Por que se escriben en ese orden

---

## 1. Que significa `python - << EOF`

Este comando es una forma rapida de ejecutar codigo Python inline desde la terminal,
sin crear un archivo `.py`.

Estructura general:

```bash
python - << EOF
# codigo python
EOF
```

- `python` inicia el interprete
- `-` indica que el codigo se leera desde stdin
- `<< EOF` es un here-document
- `EOF` marca el inicio y fin del bloque

Todo lo que esta entre los dos `EOF` se ejecuta como si fuera un script Python.

---

## 2. Ejemplo aplicado a LocalStorage

```bash
python - << EOF
from benchmark_ingestor.providers.local.storage import LocalStorage

s = LocalStorage()
s.put_json("jobs/index.json", {"jobs": []})
print(s.get_json("jobs/index.json"))
EOF
```

Paso a paso:

1) Se importa LocalStorage
2) Se crea una instancia en memoria
3) Se guarda un JSON bajo la key `jobs/index.json`
4) Se recupera ese JSON
5) Se imprime en consola

Si ves el resultado esperado, confirma que:
- El provider local funciona
- El contrato StorageBackend esta bien implementado
- No se necesita cloud ni red

---

## 3. Por que usamos este comando y no un test aun

Este paso es una validacion manual rapida, no un test formal.

Sirve para:
- Verificar imports
- Confirmar comportamiento basico
- Detectar errores obvios antes de escribir tests

---

## 4. Estrategia de testing (vision general)

Vamos a testear el proyecto en capas, de menor a mayor complejidad:

1) Tests de contrato (storage)
2) Tests de providers (local)
3) Tests de core (history)
4) Tests de flujo completo (ingestor)
5) Tests de integracion (cloud, opcional)

---

## 5. Tests del Paso 2: LocalStorage

### Que vamos a testear

- Guardar un JSON
- Recuperar un JSON
- Error al leer una key inexistente

### Ejemplo de test

```python
def test_local_storage_put_and_get():
    storage = LocalStorage()
    storage.put_json("a.json", {"x": 1})
    assert storage.get_json("a.json") == {"x": 1}


def test_local_storage_missing_key():
    storage = LocalStorage()
    with pytest.raises(FileNotFoundError):
        storage.get_json("missing.json")
```

Estos tests:
- No usan cloud
- No usan mocks
- Son rapidos y deterministas

---

## 6. Por que testear primero LocalStorage

Porque:
- Es el provider mas simple
- Valida el contrato sin ruido
- Sirve como base para tests del core
- Evita debugging complejo con SDKs

---

## 7. Como se aplicaran los tests paso a paso

Paso A – Tests de provider local  
Archivo: `test/test_local_storage.py`

Paso B – Tests de history  
Archivo: `test/test_history.py`

Paso C – Tests de ingestor  
Archivo: `test/test_ingestor.py`

---

## 8. Regla de oro de testing

Si un test necesita credenciales cloud para validar logica de negocio,
la arquitectura esta mal.

---

## 9. Proximo paso

Con LocalStorage validado y documentado, el siguiente paso es:

Paso 3: mover BenchmarkIngestor al core y escribir el primer test sin AWS.
