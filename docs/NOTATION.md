# Notación

Una sola notación para todo el curso. Es una convención propia, inspirada en la práctica
común del área; cada libro usa la suya, así que al consultar una referencia conviene revisar
su sección de notación. La columna **En el código** indica cómo se llama cada símbolo en
Python: es el puente entre la ecuación y el código.

## Tipos de objetos

| Símbolo | Significado | En el código |
|---|---|---|
| $x$ | Escalar (minúscula en cursiva) | `x` |
| $\mathbf{x}$ | Vector (minúscula en negritas) | `x` |
| $\mathbf{X}$ | Matriz o tensor (mayúscula en negritas) | `X` |
| $x_j$ | Componente $j$ de un vector | `x[j]` |

## Datos

| Símbolo | Significado | En el código |
|---|---|---|
| $\mathcal{D} = \{(\mathbf{x}^{(i)}, y^{(i)})\}_{i=1}^{n}$ | Conjunto de datos con $n$ ejemplos | `dataset` |
| $\mathbf{x}^{(i)}$, $y^{(i)}$ | Entrada y etiqueta del ejemplo $i$ | `X[i]`, `y[i]` |
| $n$ | Número de ejemplos | `n_samples` |
| $d$ | Número de variables de entrada | `n_features` |
| $B$ | Tamaño del lote | `batch_size` |

## Redes neuronales

| Símbolo | Significado | En el código |
|---|---|---|
| $L$ | Número de capas | `n_layers` |
| $\mathbf{W}^{[l]}$, $\mathbf{b}^{[l]}$ | Pesos y sesgos de la capa $l$ | `weight`, `bias` |
| $\mathbf{z}^{[l]} = \mathbf{W}^{[l]}\mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}$ | Preactivación de la capa $l$ | `z` |
| $\mathbf{a}^{[l]} = g(\mathbf{z}^{[l]})$ | Activación de la capa $l$; $\mathbf{a}^{[0]} = \mathbf{x}$ | `a` |
| $g$ | Función de activación | `activation` |
| $\sigma$ | Sigmoide | `sigmoid` |
| $\mathrm{ReLU}(z) = \max(0, z)$ | Unidad lineal rectificada | `relu` |
| $\hat{y}$ | Predicción | `y_hat` |

## Entrenamiento

| Símbolo | Significado | En el código |
|---|---|---|
| $\boldsymbol{\theta}$ | Todos los parámetros del modelo | `params` |
| $\ell(\hat{y}, y)$ | Pérdida de un ejemplo | `loss` |
| $J(\boldsymbol{\theta}) = \frac{1}{n}\sum_{i=1}^{n} \ell(\hat{y}^{(i)}, y^{(i)})$ | Costo: pérdida promedio | `cost` |
| $\nabla_{\boldsymbol{\theta}} J$ | Gradiente del costo | `grad` |
| $\eta$ | Tasa de aprendizaje | `lr` |
| $\lambda$ | Fuerza de la regularización | `weight_decay` |
| $p$ | Probabilidad de apagar una neurona (dropout) | `p` |
| $\epsilon$ | Constante pequeña para estabilidad numérica | `eps` |

## Operaciones

| Símbolo | Significado | En el código |
|---|---|---|
| $\mathbf{A}\mathbf{B}$ | Producto de matrices | `A @ B` |
| $\mathbf{a} \odot \mathbf{b}$ | Producto elemento a elemento | `a * b` |
| $\mathbf{X} * \mathbf{K}$ | Convolución con el kernel $\mathbf{K}$ | `conv2d(X, kernel)` |
| $\mathbf{A}^\top$ | Transpuesta | `A.T` |

## Secuencias

| Símbolo | Significado | En el código |
|---|---|---|
| $t$, $T$ | Paso de tiempo y longitud de la secuencia | `t`, `seq_len` |
| $\mathbf{h}_t$ | Estado oculto en el tiempo $t$ | `hidden` |

## Aprendizaje por refuerzo

| Símbolo | Significado | En el código |
|---|---|---|
| $s$, $a$, $r$ | Estado, acción y recompensa | `state`, `action`, `reward` |
| $\gamma$ | Factor de descuento | `gamma` |
| $\pi$ | Política | `policy` |
| $Q(s, a)$ | Valor de la acción $a$ en el estado $s$ | `q_values` |
