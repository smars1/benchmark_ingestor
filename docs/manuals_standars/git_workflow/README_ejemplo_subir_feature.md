# Ejemplo practico: subir una feature y documentarla como estandar

Este documento usa un **ejemplo real** del proyecto `benchmark_ingestor`
para documentar **paso a paso** como debe subirse una feature y dejarla
como estandar para futuros desarrollos.

El ejemplo se basa en el cierre del **Paso 1 (Arquitectura + StorageBackend)**.

---

## 1. Contexto del ejemplo

Feature trabajada:

- Nombre: `feature/multicloud-storage`
- Alcance:
  - Definicion del contrato `StorageBackend`
  - Nueva estructura `core/`
  - Documentacion de arquitectura
  - Sin cambios funcionales

Resultado esperado:
- Codigo estable
- Tests existentes pasando
- Documentacion completa
- Lista para integrarse a `dev`

---

## 2. Checklist antes de cerrar una feature

Antes de hacer cualquier push o merge, validar:

- [ ] Estas en la rama correcta (`feature/*`)
- [ ] El codigo corre sin errores
- [ ] `pytest` pasa completamente
- [ ] README y docs actualizados
- [ ] No hay archivos temporales o basura

Comando recomendado:

```bash
git status
pytest
```

---

## 3. Commit final de la feature

El ultimo commit de una feature debe:
- representar una idea cerrada
- ser claro
- no mezclar cambios no relacionados

Ejemplo real para Paso 1:

```text
chore: introduce storage contract and multicloud architecture docs
git add core/storage.py
git commit -m"add core storage interface | prepare cloud-agnostic architecture |  keep v0.0.1 behavior intact | 1.0.0v"

git add core/docs
git commit -m"document design decisions"
```

Este commit:
- no agrega funcionalidad visible
- prepara la base para features futuras

---

## 4. Push de la feature

Una vez confirmado el commit:

```bash
git push origin feature/multicloud-storage
```

Esto:
- respalda el trabajo
- permite revision
- habilita PR si el repo lo usa

---

## 5. Integracion de la feature en dev

Cambiar a la rama `dev`:

```bash
git checkout dev
git pull origin dev
```

Integrar la feature:

```bash
git merge feature/multicloud-storage
```

Resolver conflictos si existen y validar nuevamente:

```bash
pytest
```

Luego hacer push:

```bash
git push origin dev
```

---

## 6. Limpieza de la feature

Una vez integrada correctamente:

```bash
git branch -d feature/multicloud-storage
```

Esto mantiene el repositorio limpio.

---

## 7. Que NO se hace en este punto

En este ejemplo NO se:

- mergea a `main`
- crea tag de version
- publica release

La feature solo prepara el terreno.

---

## 8. Como reutilizar este flujo para futuras features

Para cualquier nueva feature:

1. Crear rama desde `dev`
2. Desarrollar una sola idea
3. Documentar cambios relevantes
4. Commit claro
5. Push de feature
6. Merge a `dev`
7. Eliminar feature

Ejemplo:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/local-storage-tests
```

---

## 9. Regla mental final

> Una feature no se termina cuando el codigo funciona,
> sino cuando esta documentada, testeada e integrada.

Este ejemplo debe usarse como **plantilla mental**
para todos los siguientes cambios del proyecto.
