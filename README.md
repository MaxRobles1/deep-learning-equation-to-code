# Aprendizaje profundo con PyTorch

**Intuición, teoría y código.**

Un curso abierto para quien quiere entender el aprendizaje profundo, no solo usarlo. Cada
concepto se explica primero con una idea, después con su ecuación y finalmente con el código
que la implementa, para que puedas comprobar por ti mismo cómo y por qué funciona.

> **Estado.** En construcción: los temas se publican uno a uno.

## Para quién es

Para estudiantes, profesionales que llegan desde otras áreas y quienes ya entrenan modelos pero
quieren saber qué ocurre debajo. Ayuda tener bases de Python, álgebra lineal, cálculo y
probabilidad; lo indispensable se repasa dentro de cada tema.

## Qué vas a encontrar

El recorrido va de la primera neurona a las arquitecturas que hoy sostienen la visión por
computadora, el análisis de secuencias, los modelos generativos y el aprendizaje por
refuerzo. El temario completo, la forma de evaluación y la bibliografía están en
[SYLLABUS.md](SYLLABUS.md).

## Cómo se estudia cada tema

Cada lección construye el mismo concepto desde varios ángulos:

| Paso | Qué encuentras |
|---|---|
| 1. Intuición | Para qué sirve y cómo pensarlo, sin fórmulas |
| 2. Matemática | Cada fórmula paso a paso, con el significado de sus símbolos y para qué sirve |
| 3. Desde cero | Una implementación en NumPy, para comprobar que no hay magia |
| 4. Con el framework | Lo mismo en PyTorch, comparado con la versión desde cero |
| 5. Experimenta | Parámetros que puedes mover para observar qué cambia |
| 6. Errores comunes | Lo que suele salir mal y cómo detectarlo |
| 7. Ejercicios | Práctica guiada al final de cada lección |
| 8. Para profundizar | El capítulo exacto de las referencias |

## Cómo empezar

**Sin instalar nada.** Cada lección tiene un botón *Open in Colab* para ejecutarla en el
navegador, con GPU gratuita para los temas más pesados.

**En tu computadora.** Necesitas [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/MaxRobles1/deep-learning-equation-to-code.git
cd deep-learning-equation-to-code
uv sync              # crea el entorno con las versiones exactas del lockfile
uv run jupyter lab   # abre las lecciones
```

Todas las lecciones corren en CPU en modo rápido; los datos se descargan solos la primera
vez y no se guardan en el repositorio.

## Estructura del repositorio

```
topics/        un tema por carpeta, con sus lecciones y ejercicios
src/           código compartido entre lecciones (implementaciones desde cero, gráficas, datos)
tests/         pruebas del código compartido
activities/    actividades largas
docs/          notación, glosario español-inglés, guía de estilo y referencias
SYLLABUS.md    temario, evaluación y bibliografía
```

## Referencias y derechos de autor

Las explicaciones, el código y las figuras de este repositorio son de elaboración propia.
Cuando una idea, un resultado o un ejemplo proviene de otra obra, se cita su fuente. No se
reproduce texto ni figuras de los libros de referencia: se indica el capítulo para que
puedas consultarlo directamente. La bibliografía completa está en [SYLLABUS.md](SYLLABUS.md),
y las lecturas complementarias y los artículos originales, en
[docs/REFERENCES.md](docs/REFERENCES.md).

## Herramientas utilizadas

- **Lenguaje y entorno:** Python 3.12, uv y `uv.lock`.
- **Aprendizaje profundo:** PyTorch y TensorBoard.
- **Asistencia con IA:** durante la elaboración se usó Claude Code (Anthropic) como asistente
  para redactar borradores y revisar código y explicaciones. El contenido, su revisión y su
  aprobación son responsabilidad del autor.

## Licencia

- **Código:** [MIT](LICENSE).
- **Contenido** (textos, explicaciones y figuras): [CC BY 4.0](LICENSE-CONTENT). Puedes
  usarlo y adaptarlo citando la fuente.

## Autor

Maximino Jiménez Robles · GitHub: [MaxRobles1](https://github.com/MaxRobles1)
