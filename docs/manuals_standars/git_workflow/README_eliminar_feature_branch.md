# Proceso estandar para eliminar (cerrar) una feature branch

Este documento describe el proceso correcto y seguro para cerrar y eliminar
una feature branch en el proyecto `benchmark_ingestor`.

El objetivo es:
- mantener el repositorio limpio
- evitar ramas abandonadas
- preservar el historial de cambios
- asegurar que nada se pierda

Este proceso debe seguirse cada vez que una feature ha sido integrada.

---

## 1. Que significa eliminar una feature

Eliminar una feature NO significa perder trabajo.

Significa que:
- el codigo ya fue integrado a dev
- la rama ya cumplio su objetivo
- el historial queda preservado en Git

Las ramas feature son temporales por diseno.

---

## 2. Precondiciones obligatorias

Antes de eliminar una feature, se debe cumplir todo lo siguiente:

- La feature fue mergeada a dev
- No hay commits pendientes solo en la feature
- dev esta en estado estable
- Tests ejecutados correctamente

Nunca eliminar una feature que:
- no fue mergeada
- contiene cambios no integrados

---

## 3. Flujo recomendado paso a paso

### Paso 1: Cambiar a dev

```bash
git checkout dev
git pull origin dev
```

---

### Paso 2: Verificar que la feature ya no es necesaria

```bash
git branch
```

Confirmar que NO estas parado en la feature.

---

### Paso 3: Eliminar la rama local

```bash
git branch -d feature/multicloud-storage
```

Si Git permite borrarla:
- significa que ya fue mergeada
- es seguro eliminarla

---

### Paso 4: Eliminar la rama remota

```bash
git push origin --delete feature/multicloud-storage
```

Esto limpia el repositorio remoto.

---

## 4. Caso especial: Git no permite borrar la rama

Si Git muestra un error al borrar la rama:

- la feature NO fue mergeada
- hay commits que se perderian

Que hacer:
- no usar -D sin revisar
- evaluar si se debe mergear o descartar

---

## 5. Que no hacer

Nunca:
- eliminar una feature antes del merge
- usar git branch -D sin entender el estado
- borrar ramas desde main
- borrar ramas sin revision

---

## 6. Por que este proceso es importante

Este flujo:
- mantiene historial limpio
- evita errores
- mejora colaboracion
- facilita mantenimiento

---

## 7. Regla mental final

Una feature se elimina solo cuando:
- esta mergeada
- esta documentada
- ya no es necesaria

Si hay duda, no la borres aun.

---

## 8. Uso como estandar

Este documento debe usarse como referencia
para todos los futuros cambios del proyecto.
