## 목차
* [Lenear regression with one variable](#linear-regression-with-one-variable)
* [Linear Regression with multiple variables](#linear-regression-with-multiple-variables)
* [Logistic Regression](#logistic-regression)

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
temp0 := $\theta_0 - \alpha\frac{\partial}{\partial\theta_0}J(\theta_0,\theta_1) = \theta_0 - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})$    
temp1 := $\theta_1 - \alpha\frac{\partial}{\partial\theta_1}J(\theta_0,\theta_1) = \theta_1 - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x^{(i)}$  
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
* Min-max Normalization
    - 최대, 최소값을 이용해 $0\le x\le1$ 또는 $-1\le x\le1$으로 scaling
* Mean Normalization
    - normalized $x = \frac{x-mean}{stadard deviation}$
* Mean normalization이 더 자주 사용된다
    - Min-max normalization은 outlier(극단치) 처리에 취약하기 때문
* Gradient Descent   
Repeat {$\theta_j := \theta_j - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}$}  
$\theta_0 := \theta_0 - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_0^{(i)}$  
$\theta_1 := \theta_1 - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_1^{(i)}$  
...  
$\theta_n := \theta_n - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_n^{(i)}$  

### Features and polynomial regression
* $x$에 컬럼을 추가하여 Linear Regression with multiple variables 수행
    - ex) $h(x) = \theta_0 + \theta_1(size) + \theta_2\sqrt{(size)}$에서 variable이 3개인 것과 같이 linear regression 수행

## Logistic Regression
### Classification
* Binary classification에 대해 논의 : $y ∈ \lbrace 0, 1 \rbrace$
    - $y = 0 or 1$이어야 하는데 $h_\theta$가 1을 초과하거나 0 미만일 수 있으므로, 기존의 linear regression으로는 불가능
### Hypothesis Representation
* Logistic Regression Model
    - $0\le h_\theta(x) \le 1$을 위해  
    $h_\theta(x) = g(\theta^Tx)$에서 $g(z) = \frac{1}{1+e^{-z}}$  
    $\therefore h_\theta(x) = \frac{1}{1+e^{-\theta^Tx}}$
        - $g(z)$는 sigmoid function 또는 logistic function
### Decision boundary
### Cost function
### Simplified cost function and gradient descent
### Multi-class classificarion : One-vs-all
