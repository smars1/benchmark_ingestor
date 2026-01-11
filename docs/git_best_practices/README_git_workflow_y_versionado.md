# Flujo de trabajo Git y versionado del proyecto

Este documento define el **flujo estandar de trabajo con Git** para el proyecto
`benchmark_ingestor`, incluyendo:

- uso de branches
- estandarizacion de commits
- manejo de versiones
- buenas practicas antes de desarrollar y antes de hacer push

El objetivo es mantener un historial **claro, profesional y facil de mantener**.

---

## 1. Principio general

> Nunca desarrolles directamente sobre `main`.

El trabajo siempre se hace en **features**, se integra en **dev**
y solo lo estable llega a **main**.

---

## 2. Branches base

El repositorio maneja tres niveles principales:

### `main`
- Rama estable
- Representa la ultima version publicada
- Siempre debe estar en estado funcional

### `dev`
- Rama de integracion
- Aqui se juntan las features terminadas
- Puede contener cambios aun no versionados

### `feature/*`
- Rama de trabajo
- Una feature = una idea cerrada
- Nunca se reutiliza para cosas distintas

Ejemplos validos:
- `feature/multicloud-storage`
- `feature/local-storage-tests`
- `feature/aws-provider`
- `feature/docs-workflow`

---

## 3. Flujo obligatorio antes de empezar a desarrollar

Antes de escribir codigo:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/<nombre-feature>
```

Esto asegura:
- partir del ultimo estado integrado
- evitar conflictos innecesarios
- aislar el cambio

---

## 4. Flujo durante el desarrollo

Durante el desarrollo:

1. Realizar cambios pequenos y coherentes
2. Ejecutar tests localmente (`pytest`)
3. Verificar que no se rompio funcionalidad existente

Nunca hacer commits con codigo roto.

---

## 5. Estandar de mensajes de commit

Se utiliza un formato simple inspirado en Conventional Commits.

### Tipos permitidos

- `feat:` nueva funcionalidad
- `refactor:` cambio interno sin romper comportamiento
- `fix:` correccion de bug
- `docs:` documentacion
- `test:` tests
- `chore:` tareas de mantenimiento o preparacion

### Ejemplos correctos

```text
feat: add local storage provider for testing

refactor: introduce storage contract in core

docs: document multicloud architecture decision

chore: prepare v1.0.0 release structure
```

### Reglas
- Un commit = una idea
- Mensaje claro y en presente
- Evitar commits gigantes

---

## 6. Uso de README y documentacion

### README.md (raiz)
- Describe el estado actual del proyecto
- Siempre alineado con la version publicada

### docs/
- Contiene decisiones de arquitectura
- Explica el por que de los cambios
- Puede tener multiples README

### CHANGELOG.md
- Resume cambios por version
- No reemplaza commits
- Complementa el historial

---

## 7. Flujo para cerrar una feature

Cuando la feature esta completa:

```bash
git checkout dev
git pull origin dev
git merge feature/<nombre-feature>
git push origin dev
```

Luego:
- Crear Pull Request (si aplica)
- Revisar cambios
- Eliminar la rama feature

```bash
git branch -d feature/<nombre-feature>
```

---

## 8. Flujo de versionado

Cuando `dev` esta listo para versionarse:

1. Actualizar `README.md`
2. Actualizar `CHANGELOG.md`
3. Hacer commit de version

Ejemplo:

```text
chore: release v1.0.0
```

4. Merge a `main`

```bash
git checkout main
git pull origin main
git merge dev
git push origin main
```

5. Crear tag

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## 9. Regla antes de cada push

Antes de hacer `git push`:

- Ejecutar tests (`pytest`)
- Verificar que el commit tiene sentido
- Confirmar que estas en la rama correcta

Nunca hacer push directo a `main`.

---

## 10. Beneficios de este flujo

Este flujo permite:

- Historial limpio
- Versionado claro
- Facil rollback
- Mejor colaboracion
- Documentacion trazable
- Proyecto presentable como portafolio

---

## 11. Regla mental final

> Feature primero.  
> Commit claro.  
> Dev integra.  
> Main versiona.

Seguir este flujo evita deuda tecnica y errores innecesarios.
