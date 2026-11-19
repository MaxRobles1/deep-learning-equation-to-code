# Temario · Aprendizaje profundo (Deep Learning)

## Introducción

Hoy, las herramientas que permiten a una máquina reproducir comportamientos humanos, la
inteligencia artificial (IA), tienen más relevancia que nunca. Como área integral de la IA
está el aprendizaje máquina (machine learning, ML), que permite a las computadoras aprender
de los datos y mejorar lo aprendido. Dentro del ML, el aprendizaje profundo (deep learning),
basado en redes neuronales con dos o más capas ocultas, ha tomado especial relevancia.

## Objetivo

Presentar el aprendizaje profundo: sus conceptos fundamentales, las arquitecturas más
importantes y algunas de sus aplicaciones más relevantes, como el reconocimiento de
imágenes. La asignatura se apoya en conceptos estadísticos, probabilísticos, computacionales
y de manejo de datos. Lo aprendido permitirá entender mejor muchas de las aplicaciones
actuales del aprendizaje profundo: la inteligencia artificial generativa, el reconocimiento
de voz y de rostros, la detección de fraudes y la tecnología detrás de los automóviles
autónomos.

## Temario

### Tema 1 · Introducción al aprendizaje profundo
- 1.1 IA, machine learning y deep learning
- 1.2 Conceptos generales de redes neuronales
- 1.3 Redes neuronales profundas
- 1.4 Hiperparámetros y su relación con el balance entre sesgo y varianza
- 1.5 Arquitecturas más utilizadas en aprendizaje profundo

### Tema 2 · Tensores, máquinas de ejecución y frameworks
- 2.1 Tensores y operaciones asociadas
- 2.2 Grafos computacionales y gradientes
- 2.3 El ecosistema de frameworks: PyTorch, TensorFlow y JAX (Theano y CNTK como antecedentes históricos)
- 2.4 Frameworks de alto nivel: qué es Keras y cómo se relaciona con PyTorch
- 2.5 PyTorch (front-end) y torch (back-end)
- 2.6 Modelos secuenciales en PyTorch (`nn.Sequential`) y TensorBoard

### Tema 3 · Redes neuronales convolucionales (CNN)
- 3.1 Aspectos generales
- 3.2 Convoluciones y filtros
- 3.3 Capas de pooling, ReLU y totalmente conectadas
- 3.4 Modelos preentrenados y transfer learning
- 3.5 Ejemplos de arquitecturas

### Tema 4 · Redes neuronales recurrentes (RNN)
- 4.1 Definición y relación con las redes feedforward
- 4.2 Limitaciones de las RNN y posibles modificaciones
- 4.3 Redes LSTM: arquitectura y usos
- 4.4 Arquitectura GRU
- 4.5 Análisis de series temporales y secuencias

### Tema 5 · Entrenamiento de redes neuronales profundas
- 5.1 Descenso de gradiente y backpropagation
- 5.2 Modificaciones del algoritmo de descenso de gradiente
- 5.3 Descenso de gradiente estocástico (SGD), mini-batch, momentum y gradiente acelerado de Nesterov
- 5.4 Adagrad, RMSprop y Adadelta
- 5.5 Adam

### Tema 6 · Estrategias contra el sobreajuste y la convergencia inadecuada
- 6.1 Reducción del tamaño de la red
- 6.2 Regularización por penalización
- 6.3 Dropout
- 6.4 Desvanecimiento y explosión del gradiente (vanishing y exploding gradient)
- 6.5 Inicialización óptima de los pesos
- 6.6 Batch normalization

### Tema 7 · Optimización de hiperparámetros (HPO)
- 7.1 Grid search, random search y optimización bayesiana
- 7.2 Entrenamiento, validación y prueba; fuga de datos (data leakage)
- 7.3 Hiperparámetros a optimizar
- 7.4 HPO con PyTorch: Optuna y la biblioteca d2l

### Tema 8 · Autoencoders
- 8.1 Definición y aplicaciones
- 8.2 Clasificación
- 8.3 Redes convolucionales profundas (DCN) y redes deconvolucionales
- 8.4 Aplicaciones
- 8.5 Detección de anomalías con autoencoders

### Tema 9 · Redes generativas adversarias (GANs)
- 9.1 Definición y ejemplos de uso
- 9.2 Generador y discriminador
- 9.3 GANs convolucionales profundas (DCGAN)
- 9.4 Aplicaciones

### Tema 10 · Aprendizaje por refuerzo profundo (Deep Reinforcement Learning)
- 10.1 Cadenas de Markov y procesos de decisión de Markov
- 10.2 Q-learning
- 10.3 Q-learning profundo (Deep Q-Network, DQN)
- 10.4 Ejemplos de uso del aprendizaje por refuerzo profundo

## Para ir más allá

Temas que este curso no cubre, cada uno con el artículo original como punto de partida:

| Tema | Punto de partida |
|---|---|
| Variational Autoencoders (VAE) | Kingma, D. P. y Welling, M. (2013). *Auto-Encoding Variational Bayes*. arXiv:1312.6114 |
| Máquinas de Boltzmann y Boltzmann restringidas (RBM) | Ackley, D. H., Hinton, G. E. y Sejnowski, T. J. (1985). A learning algorithm for Boltzmann machines. *Cognitive Science*, 9(1), 147–169 |
| Arquitectura transformer (NLP) | Vaswani, A. et al. (2017). *Attention Is All You Need*. NeurIPS. arXiv:1706.03762 |
| Capsule networks | Sabour, S., Frosst, N. y Hinton, G. E. (2017). *Dynamic Routing Between Capsules*. NeurIPS. arXiv:1710.09829 |
| Mapas autoorganizados (SOM) | Kohonen, T. (1982). Self-organized formation of topologically correct feature maps. *Biological Cybernetics*, 43(1), 59–69 |

## Bibliografía

Las obras marcadas con 🔓 se pueden consultar gratis en línea, publicadas por sus propios
autores o editoriales. Los artículos originales de cada tema están en
[docs/REFERENCES.md](docs/REFERENCES.md).

### Básica
- Goodfellow, I., Bengio, Y. y Courville, A. (2016). *Deep Learning*. MIT Press. 🔓
- Prince, S. J. D. (2023). *Understanding Deep Learning*. MIT Press. 🔓
- Bishop, C. M. y Bishop, H. (2024). *Deep Learning: Foundations and Concepts*. Springer. 🔓
- Zhang, A., Lipton, Z. C., Li, M. y Smola, A. J. (2023). *Dive into Deep Learning*. Cambridge University Press. 🔓
- Raschka, S., Liu, Y. y Mirjalili, V. (2022). *Machine Learning with PyTorch and Scikit-Learn*. Packt.
- Aggarwal, C. C. (2023). *Neural Networks and Deep Learning: A Textbook* (2.ª ed.). Springer.

### Complementaria
- Nielsen, M. A. (2015). *Neural Networks and Deep Learning*. Determination Press. 🔓
- Deisenroth, M. P., Faisal, A. A. y Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press. 🔓
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. 🔓
- Hastie, T., Tibshirani, R. y Friedman, J. (2009). *The Elements of Statistical Learning* (2.ª ed.). Springer. 🔓
- Sutton, R. S. y Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2.ª ed.). MIT Press. 🔓
- Chollet, F. y Watson, M. (2025). *Deep Learning with Python* (3.ª ed.). Manning.
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3.ª ed.). O'Reilly.
- Stevens, E., Antiga, L. y Viehmann, T. (2020). *Deep Learning with PyTorch*. Manning.
- Burkov, A. (2019). *The Hundred-Page Machine Learning Book*. Andriy Burkov.

### Qué leer en cada tema

| Tema | Lecturas principales |
|---|---|
| 1 · Introducción | Goodfellow et al., Prince, Nielsen |
| 2 · Tensores y frameworks | Zhang et al., Raschka et al., Stevens et al. |
| 3 · Redes convolucionales | Goodfellow et al., Prince, Zhang et al. |
| 4 · Redes recurrentes | Goodfellow et al., Zhang et al., Aggarwal |
| 5 · Entrenamiento | Goodfellow et al., Prince, Bishop y Bishop |
| 6 · Sobreajuste y convergencia | Goodfellow et al., Prince, Bishop y Bishop |
| 7 · Hiperparámetros | Zhang et al., Raschka et al. |
| 8 · Autoencoders | Goodfellow et al., Bishop y Bishop |
| 9 · GANs | Goodfellow et al., Prince, Bishop y Bishop |
| 10 · Aprendizaje por refuerzo profundo | Sutton y Barto, Prince |

Matemáticas de apoyo en todos los temas: Deisenroth et al.
