# Convenciones de Nomenclatura de Ramas

En este proyecto, seguimos ciertas convenciones de nomenclatura para nuestras ramas de desarrollo con el fin de mantener un historial claro y comprensible. A continuación, se describen las convenciones que utilizamos para nombrar nuestras ramas.

## Tipos de Ramas

1. **feature/***: Esta nomenclatura indica que estamos trabajando en una nueva característica o funcionalidad del proyecto.

   - **Propósito:** Estas ramas se utilizan para desarrollar nuevas características o funcionalidades específicas del proyecto.
   - **Enfoque:** Cada rama `features/*` se enfoca en una tarea o aspecto particular de la nueva funcionalidad a implementar.
   - **Duración:** Pueden tener una duración más larga, ya que pueden abarcar múltiples commits y cambios relacionados con la nueva característica.
   - **Ejemplo:** `feature/user-authentication`, `feature/shopping-cart`

2. **bugfix/***: Se utiliza cuando estamos resolviendo un problema específico o corrigiendo errores en el código.

   - **Propósito:** Estas ramas se utilizan para corregir problemas específicos o errores en el código.
   - **Enfoque:** Cada rama `bugfix/*` se enfoca en resolver un problema o error concreto identificado en el proyecto.
   - **Duración:** Tienden a tener una duración más corta y están enfocadas en la corrección del problema identificado.
   - **Ejemplo:** `bugfix/login-issue`, `bugfix/database-error`

3. **task/***: Utilizamos este prefijo para identificar tareas generales que no corresponden directamente a una nueva característica o a la corrección de un error.

   - **Propósito:** Estas ramas se utilizan para tareas generales del proyecto que no están directamente relacionadas con una nueva característica específica.
   - **Enfoque:** Cada rama `task/*` se enfoca en una tarea general del proyecto, como la implementación de medidas de seguridad, mejoras en la interfaz de usuario, etc.
   - **Duración:** Tienden a tener una duración más corta y están más orientadas a tareas puntuales y concretas.
   - **Ejemplo:** `task/implement-security`, `task/update-documentation`

## Ejemplos de Nombres de Ramas:

- **feature/nueva-funcionalidad**:
  Esta rama está dedicada al desarrollo de una nueva característica o funcionalidad del proyecto.

- **bugfix/arreglo-error-importante**:
  En esta rama, se resuelve un problema específico o se corrige un error importante en el código.

- **task/implementacion-seguridad**:
  Esta rama se utiliza para trabajar en la implementación de medidas de seguridad como una tarea general dentro del proyecto.

Al seguir estas convenciones, buscamos mantener un flujo de trabajo organizado y comprensible para todos los miembros del equipo.