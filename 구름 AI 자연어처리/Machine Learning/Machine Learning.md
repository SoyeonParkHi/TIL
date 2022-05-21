## 목차
* [Lenear regression with one variable](#linear-regression-with-one-variable)
* [Linear Regression with multiple variables](#linear-regression-with-multiple-variables)

## Linear regression with one variable

### Model representation
* 지도학습(Supervised Learning) : 예제데이터로부터 target variable 추출
    - **Regression Problem : real-valued output을 예측 (Continuous, 실수형)**
    - Logistic Regression(Classification) : Discrete-valued output을 예측 (Category, 범주형)
* 비지도학습(Unsupervised Learning) : 대표적으로 Clustering이 있다.
* Notation
    - m = Number of training examples
    - x's = input variable / features
    - y's = output variable / target variable
    - (x,y) = one training example
    - $x^{(i)}, y^{(i)} = i^{th}$ training example
* Hypothesis(가설) : 알고리즘을 통해 도출된 수식, $h_\theta = \theta_0 + \theta_1$
    - Lenear regression with one variable에서는 y = ax + b

### Cost function
* $\theta$'s : Set of Parameters, {$\theta_0, \theta_1$}
* Cost function : 예측치와 실제 값의 차에 제곱(최소화하기 위함)
    - Objective function, Loss function이라고도 한다.
    - Squared error function의 경우,
    - $J(\theta_0, \theta_1) = \frac{1}{2m}\displaystyle\sum_{i=1}^{m}{(h_\theta(x^{(i)})-y^{(i)})^2}$

### Gradient descent
* Loss function을 optimize(최적화)
    - 형태가 smooth한 function에서 기울기에 비례해 좌표 변환
* Term
    - Convex function : 볼록함수
    - Non-convex function : local minima가 존재(국소의 여러 최소)
* Repeat until convergence {$\theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1)$}
    - $\alpha$ = step size, learning rate
* Simultaneous update  
temp0 := $\theta_0 - \alpha\frac{\partial}{\partial\theta_0}J(\theta_0,\theta_1)$  
temp1 := $\theta_1 - \alpha\frac{\partial}{\partial\theta_1}J(\theta_0,\theta_1)$  
$\theta_0$ := temp0  
$\theta_1$ := temp1

## Linear Regression with multiple variables
### Multiple features
* Notation
    - n = number of features
        + feature = dimension = attribute (같은 의미로 사용)
    - $x^{(i)}$ = input (features) of $i^{th}$ training example
    - $x_j^{(i)}$ = value of feature $j$ in $i^{th}$ training example
    - ex) $x_3^{(2)}$ = 2번째 training example에서 3번째 feature의 값
* Target variable은 보통 한번에 하나만 처리
* Feature vector = 한 training example의 feature 값을 column vector로 표현
    - row vector로 나타내고자 할때는 transpose 이용
* $h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + ... + \theta_nx_n = \theta^Tx$
    - $x_0$ = 0
    - x = $\begin{bmatrix} x_0 \\ x_1 \\ ... \\ x_n \end{bmatrix}$
    - $\theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ ... \\ \theta_n \end{bmatrix}$

### Gradient descent in practice 1 : Feature Scaling
