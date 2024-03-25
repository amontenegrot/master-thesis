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

# Instalación de modelos spaCy

Para utilizar spaCy en tu entorno de Python, necesitarás instalar los modelos lingüísticos adecuados. spaCy proporciona varios modelos pre-entrenados para diferentes tamaños y usos. A continuación, se muestra cómo instalar los modelos 'en_core_web_sm', 'en_core_web_md' y 'en_core_web_lg':

## Instalación de 'en_core_web_sm'

Este modelo es más pequeño y tiene menos funcionalidades en comparación con los otros modelos, pero es útil para tareas básicas de procesamiento de texto.

```bash
python -m spacy download en_core_web_sm
```

## Instalación de 'en_core_web_md'

Este modelo es de tamaño medio y ofrece un equilibrio entre precisión y velocidad, siendo adecuado para una amplia gama de aplicaciones de procesamiento de lenguaje natural.

```
python -m spacy download en_core_web_md
```

## Instalación de 'en_core_web_lg'

Este modelo es el más grande de los tres y proporciona una mayor precisión en tareas avanzadas de procesamiento de texto, pero puede requerir más recursos computacionales.

```
python -m spacy download en_core_web_lg
```

## Carga del modelo en el script de Python

Después de la instalación de cada modelo, podrás cargarlos en tu código de Python utilizando spaCy, por ejemplo:

```python
import spacy

# Cargar el modelo 'en_core_web_sm'
nlp_sm = spacy.load('en_core_web_sm')

# Cargar el modelo 'en_core_web_md'
nlp_md = spacy.load('en_core_web_md')

# Cargar el modelo 'en_core_web_lg'
nlp_lg = spacy.load('en_core_web_lg')
```
