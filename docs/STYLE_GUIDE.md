# Guía de estilo

Cómo se escribe una lección. El objetivo es que todos los temas se lean igual: quien aprende
sabe dónde encontrar la intuición, la matemática y el código.

## Idioma

| En español | En inglés |
|---|---|
| Explicaciones, títulos, ejercicios y documentación | Código, variables, funciones, comentarios del código y docstrings |
| La primera mención de un término técnico va con su nombre en inglés: *descenso de gradiente (gradient descent)* | Nombres de archivos y carpetas, ramas, títulos de pull request y mensajes de commit |

El vocabulario está en [GLOSSARY.md](GLOSSARY.md) y la notación en [NOTATION.md](NOTATION.md).

## Estructura de cada lección

1. **Intuición:** para qué sirve y cómo pensarlo, sin fórmulas.
2. **Matemática:** con la notación del curso; cada paso de una derivación se justifica.
3. **Desde cero:** implementación en NumPy.
4. **Con PyTorch:** el mismo cálculo con el framework, comparado numéricamente con la versión
   desde cero.
5. **Experimenta:** al menos un parámetro que la persona pueda cambiar para observar el efecto.
6. **Errores comunes:** qué suele salir mal y cómo detectarlo.
7. **Ejercicios:** las soluciones van en un notebook aparte.
8. **Para profundizar:** libro y capítulo, y el artículo original
   ([REFERENCES.md](REFERENCES.md)).

## Notebooks

- **Nombre:** número del subtema y nombre corto en inglés, por ejemplo `1.1-ai-ml-dl.ipynb`.
- **Primera celda:** título, objetivos, prerrequisitos y botón *Open in Colab*.
- **Segunda celda:** fija las semillas y lee la variable de entorno `QUICK_MODE`. En modo rápido
  la lección corre en CPU en **menos de 5 minutos**.
- **Salidas:** se guardan, para que la lección se pueda leer en GitHub sin ejecutarla. El hook
  `nbstripout` solo limpia metadatos.
- **Gráficas:** título, ejes rotulados y leyenda cuando haga falta.
- **Datos:** se descargan al ejecutar; nunca se guardan en el repositorio.

## Derechos de autor

- Las explicaciones, el código y las figuras son de elaboración propia.
- **No se copia texto ni figuras** de libros o artículos: se explica con palabras propias y se
  cita la fuente.
- Si una idea, un ejemplo o un resultado viene de otra obra, se cita en el lugar donde se usa,
  por ejemplo *(Goodfellow et al., 2016, cap. 6)*.
- Los datasets se usan solo si su licencia lo permite, y se cita su fuente.

## Código

- Estilo verificado con ruff (lint y formato).
- En `src/`: type hints, docstrings y `logging` en lugar de `print`.
- En los notebooks se permite `print`, porque mostrar resultados es parte de la lección.
- Toda función compartida en `src/` tiene al menos una prueba en `tests/`.

## Commits y pull requests

- Mensajes de commit en inglés con
  [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`,
  `test:`, `chore:`…
- Un tema o un cambio por pull request; el cuerpo del pull request va en español.
