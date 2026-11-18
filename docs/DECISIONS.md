# Decisiones

Registro de las decisiones del proyecto: qué se decidió, qué alternativa se descartó y por qué.

### D-001 · 2026-11-17 · Prosa en español; código y archivos en inglés
- **Decisión:** explicaciones y documentación en español; código, nombres de archivos,
  comentarios del código, ramas y commits en inglés.
- **Alternativa descartada:** todo en español, incluido el código.
- **Motivo:** el inglés es la lengua de trabajo del área (bibliotecas, documentación,
  artículos). Así el código sirve tal cual para una futura versión en inglés.

### D-002 · 2026-11-17 · PyTorch como único framework
- **Decisión:** todo el código del curso se escribe en PyTorch. TensorFlow, JAX y Keras se
  presentan como parte del ecosistema en el Tema 2, sin código de TensorFlow.
- **Alternativa descartada:** PyTorch y Keras/TensorFlow en paralelo.
- **Motivo:** verificado en PyPI el 2026-11-17: PyTorch 2.15.0 salió el 2026-10-28, mientras
  que la última versión de TensorFlow (2.21.0) es del 2026-03-06; además, Hugging Face
  Transformers 5.23.0 solo ofrece soporte para PyTorch. Un solo framework también reduce el
  tamaño de la instalación y el tiempo del CI.

### D-003 · 2026-11-17 · Notebooks con salidas guardadas
- **Decisión:** las lecciones se versionan con sus salidas (gráficas y resultados);
  `nbstripout --keep-output --keep-count` solo limpia metadatos.
- **Alternativa descartada:** borrar todas las salidas antes de cada commit.
- **Motivo:** cualquiera puede leer la lección en GitHub sin ejecutarla. El CI vuelve a
  ejecutar todas las lecciones en modo rápido para garantizar que siguen funcionando.

### D-004 · 2026-11-17 · Licencias: MIT para el código, CC BY 4.0 para el contenido
- **Decisión:** `LICENSE` (MIT) cubre el código; `LICENSE-CONTENT` (texto oficial de CC BY 4.0)
  cubre textos, explicaciones y figuras.
- **Alternativa descartada:** una sola licencia para todo.
- **Motivo:** MIT es estándar para código y CC BY 4.0 lo es para material educativo; ambas
  permiten reutilizar citando la fuente.

### D-005 · 2026-11-17 · Temario y bibliografía revisados
- **Decisión:** se corrigieron erratas y la numeración del Tema 7; el Tema 2 se actualizó
  (Theano y CNTK como antecedentes, Keras como concepto, PyTorch como práctica); la
  bibliografía se reorganizó en básica y complementaria, priorizando obras de acceso libre.
- **Motivo:** precisión y vigencia; cualquier persona puede seguir el curso sin comprar libros.

### D-006 · 2026-11-17 · Python 3.12
- **Decisión:** el proyecto usa Python 3.12 (`.python-version`).
- **Alternativa descartada:** Python 3.13.
- **Motivo:** paridad con Google Colab, para que las lecciones se comporten igual en local y
  en Colab. Todas las dependencias resuelven en 3.12.

### D-007 · 2026-11-17 · Material calificable y grabaciones fuera del repositorio público
- **Decisión:** las soluciones de exámenes y actividades calificadas, las grabaciones y los
  datos de alumnos no se versionan aquí (`private/` está en `.gitignore`).
- **Motivo:** publicar soluciones calificables anula la evaluación, y las grabaciones y datos
  de alumnos son personales.

### D-008 · 2026-11-17 · Sitio web después
- **Decisión:** primero el contenido en GitHub; el sitio web (Quarto o Jupyter Book en GitHub
  Pages) se evalúa cuando existan dos o tres temas.
- **Motivo:** construir el contenido antes que la vitrina.

### D-009 · 2026-11-17 · Autoría
- **Decisión:** Maximino Jiménez Robles es el único autor de los commits; la asistencia de
  Claude Code se declara en la sección "Herramientas utilizadas" del README.
- **Motivo:** el autor revisa y aprueba todo el contenido y responde por él.

### D-010 · 2026-11-18 · Ejercicios sin soluciones públicas
- **Decisión:** los ejercicios de las lecciones se publican sin solución; las soluciones se
  guardan como material privado del instructor (`private/`, fuera de Git).
- **Alternativa descartada:** publicar soluciones de práctica en notebooks aparte.
- **Motivo:** los ejercicios por tema forman parte de la evaluación (trabajo continuo, 35 %).

### D-011 · 2026-11-18 · Cada fórmula se explica después de escribirla
- **Decisión:** toda fórmula va seguida de "Donde", "Qué hace" y "Para qué se usa"; las que
  definen una herramienta entre alternativas agregan "Cuándo usarla" y "Limitaciones"
  ([STYLE_GUIDE.md](STYLE_GUIDE.md)). Las lecciones no indican tiempo estimado.
- **Motivo:** una fórmula sin explicación solo sirve a quien ya la entiende. El tiempo de
  lectura es subjetivo, y el de ejecución ya lo garantiza el CI (menos de 5 minutos).
