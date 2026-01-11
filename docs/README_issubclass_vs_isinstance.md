# issubclass vs isinstance en Python

Este documento explica de forma clara y progresiva cuando usar `issubclass` y cuando usar `isinstance` en Python.

---

## 1. Idea principal

La regla de oro es simple:

- **Clases → `issubclass`**
- **Objetos → `isinstance`**

Si recuerdas esto, no te equivocas.

---

## 2. Que es instanciar

Primero definimos clases (planos):

```python
class Animal:
    pass

class Perro(Animal):
    pass
```

Aqui no existen objetos, solo definiciones.

Cuando instanciamos:

```python
firulais = Perro()
```

Sucede lo siguiente:

- `firulais` es un **objeto**
- Su tipo es `Perro`
- `Perro` hereda de `Animal`

---

## 3. Uso de isinstance

`isinstance` trabaja con **objetos**.

```python
isinstance(firulais, Perro)    # True
isinstance(firulais, Animal)  # True
```

Python evalua:

- firulais es un Perro
- Perro es un Animal
- Entonces firulais tambien es un Animal

### Cuando usar isinstance

- Validaciones en runtime
- Manejo de errores
- Codigo de negocio
- Inputs dinamicos

Ejemplo con excepciones:

```python
try:
    ...
except Exception as e:
    if isinstance(e, BenchmarkError):
        handle_error(e)
```

---

## 4. Uso de issubclass

`issubclass` trabaja con **clases**, no con objetos.

```python
issubclass(Perro, Animal)   # True
issubclass(Animal, Perro)   # False
```

### Cuando usar issubclass

- Tests unitarios
- Validar arquitectura
- Librerias y frameworks
- Contratos de herencia

Ejemplo en tests:

```python
assert issubclass(InvalidPayloadError, BenchmarkError)
```

Esto valida diseño, no ejecucion.

---

## 5. Errores comunes

Incorrecto:

```python
issubclass(firulais, Animal)
```

Porque `firulais` es un objeto.

Incorrecto:

```python
isinstance(Perro, Animal)
```

Porque `Perro` es una clase.

---

## 6. Regla mental rapida

- Si tiene `()` → es un objeto → `isinstance`
- Si no tiene `()` → es una clase → `issubclass`

---

## 7. Resumen final

| Escenario | Funcion |
|---------|--------|
| Validar herencia | issubclass |
| Validar objeto | isinstance |
| Tests de arquitectura | issubclass |
| Runtime y errores | isinstance |

---

## 8. Frase clave para recordarlo

- `issubclass` revisa los planos
- `isinstance` revisa el edificio construido
