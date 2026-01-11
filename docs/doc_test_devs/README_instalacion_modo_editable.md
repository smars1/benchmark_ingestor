# Instalacion del proyecto en modo editable (pytest + imports)

Este documento explica **por que** y **como** se instalo el proyecto `benchmark_ingestor`
en modo editable para evitar errores de importacion al ejecutar pytest.

Version instalada: **0.0.1**

---

## 1. Problema original

Al ejecutar los tests:

```powershell
pytest test/test_exceptions.py
```

aparecia el error:

```text
ModuleNotFoundError: No module named 'benchmark_ingestor'
```

Esto ocurria aun cuando la carpeta `benchmark_ingestor/` existia.

---

## 2. Causa del problema

Python solo puede importar modulos que:

1. Estan en el directorio actual
2. Estan en el PYTHONPATH
3. Estan instalados en el entorno (site-packages)

El proyecto **no estaba instalado como paquete**, por lo que pytest no podia
resolver el import:

```python
from benchmark_ingestor.exceptions import ...
```

---

## 3. Solucion aplicada (recomendada)

Se instalo el proyecto en **modo editable** usando `pip install -e .`

Esto registra el paquete en el entorno virtual sin copiar el codigo,
permitiendo:

- Imports estables
- Cambios en codigo sin reinstalar
- Ejecucion correcta de pytest
- Uso profesional tipo libreria

---

## 4. Requisitos

- Python 3.9 o superior
- Entorno virtual activo
- pip actualizado

---

## 5. Estructura del proyecto

```text
monitor_web_benchmark_ingestor/
├── benchmark_ingestor/
│   ├── __init__.py
│   ├── exceptions.py
│   └── ...
├── test/
│   └── test_exceptions.py
├── pyproject.toml
├── README.md
└── venv/
```

---

## 6. Archivo pyproject.toml

Se creo el siguiente archivo en la raiz del proyecto:

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "benchmark-ingestor"
version = "0.0.1"

[tool.setuptools.packages.find]
where = ["."]
```

### Explicacion rapida

- `build-system`: define como se construye el paquete
- `name`: nombre del paquete a nivel instalacion
- `version`: version actual del proyecto
- `packages.find`: permite detectar automaticamente `benchmark_ingestor`

---

## 7. Instalacion en modo editable

Desde la **raiz del proyecto** y con el entorno virtual activo:

```powershell
pip install -e .
```

Salida esperada:

```text
Successfully installed benchmark-ingestor-0.0.1
```

---

## 8. Ejecucion de los tests

Una vez instalado el paquete:

```powershell
pytest
```

O solo el archivo de excepciones:

```powershell
pytest test/test_exceptions.py
```

Salida esperada:

```text
collected 4 items
test/test_exceptions.py ....
4 passed
```

---

## 9. Verificacion de la instalacion

Para confirmar que el paquete esta instalado:

```powershell
pip show benchmark-ingestor
```

O:

```powershell
python -c "import benchmark_ingestor; print(benchmark_ingestor.__file__)"
```

---

## 10. Buenas practicas

- No usar sys.path.append en los tests
- Ejecutar pytest siempre desde la raiz
- Mantener el proyecto instalable desde el inicio
- Usar modo editable durante desarrollo

---

## 11. Conclusion

Instalar el proyecto en modo editable resuelve definitivamente los problemas
de importacion y deja el repositorio listo para:

- pytest
- CI/CD
- Portafolio profesional
- Crecimiento del proyecto

Esta es la forma recomendada para proyectos Python reales.
