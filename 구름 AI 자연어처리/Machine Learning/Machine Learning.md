## 목차
* [Lenear regression with one variable](#linear-regression-with-one-variable)
* [Linear Regression with multiple variables](#linear-regression-with-multiple-variables)
* [Logistic Regression](#logistic-regression)
* [Regularization](#regularization)
* [Cross Validation & Demensionality Reduction](#cross-validation--demensionality-reduction)

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
    - x = $\begin{bmatrix} x_0 \\ x_1 \\ \cdots \\ x_n \end{bmatrix}$
    - $\theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ \cdots \\ \theta_n \end{bmatrix}$

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
$\cdots$  
$\theta_n := \theta_n - \alpha\frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_n^{(i)}$  

### Features and polynomial regression
* $x$에 컬럼을 추가하여 Linear Regression with multiple variables 수행
    - ex) $h(x) = \theta_0 + \theta_1(size) + \theta_2\sqrt{(size)}$에서 variable이 3개인 것과 같이 linear regression 수행

## Logistic Regression
### Classification
* Binary classification에 대해 논의 : $y ∈ \lbrace 0, 1 \rbrace$
    - $y = 0$ or $1$이어야 하는데 $h_\theta$가 1을 초과하거나 0 미만일 수 있으므로, 기존의 linear regression으로는 불가능
### Hypothesis Representation
* Logistic Regression Model
    - $0\le h_\theta(x) \le 1$을 위해  
    $h_\theta(x) = g(\theta^Tx)$에서 $g(z) = \frac{1}{1+e^{-z}}$  
    $\therefore h_\theta(x) = \frac{1}{1+e^{-\theta^Tx}}$
        - $g(z)$는 sigmoid function 또는 logistic function
        - $e^z$와 $e^0 = 1$의 서로에 대한 비율을 의미 
### Decision boundary
* Linear decision boundary(example)
    - $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2x_2)$  
    Let $\theta = \begin{bmatrix} -3 \\ 1 \\ 1 \end{bmatrix}$  
    Predict $y = 1$ if $-3 + x_1 + x_2 \ge 0$
* Non-linear decision boundary(example)
    - $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2x_2 + \theta_3x_1^2 + \theta_4x_2^2)$  
    Let $\theta = \begin{bmatrix} -1 \\ 0 \\ 0 \\ 1 \\ 1 \end{bmatrix}$  
    Predict $y = 1$ if $-1+x_1^2 + x_2^2 \ge 0$
### Cost function
* Logistic regression cost function  
$Cost(h_\theta(x),y) = \begin{cases}-log(h_\theta(x))&\text{if} \space y = 1\\-log(1-h_\theta(x))&\text{if} \space y = 0\end{cases}$
    - $y=0$일 때 $h_\theta(x)$가 1에 가까워질수록 cost가 $\infin$로 발산하고, $y=1$일 때 $h_\theta(x)$가 0에 가까워질수록 cost가 $\infin$로 발산한다.
### Simplified cost function and gradient descent
* Logistic regression cost function
    - 위의 cost function을 다음과 같은 한 수식으로 나타낼 수 있다.
    - $Cost(h_\theta(x),y) = -y\log(h_\theta(x)) - (1-y)\log(1-h_\theta(x))$
* Gradient Descent
    - $J(\theta) = -\frac1m[\displaystyle\sum_{i=1}^{m}y^{(i)}\log h_\theta(x^{(i)}) + (1 - y^{(i)}) \log (1-h_\theta(x^{(i)}))]$  
    $min_\theta J(\theta)$ :  
    Repeat {$\theta_j:=\theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta) = \theta_j - \frac{\alpha}m\displaystyle\sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)}$}
        - $\therefore$ Linear regression과 동일
### Multi-class classificarion : One-vs-all
* n개의 class가 존재할 때,  
$h_\theta^{(i)}(x) = P(y = i|x;0)\space(i = 1, 2, \cdots, n)$
    - i번째 class를 positive($y = 1$), 나머지는 모두 $y = 0$으로 가정
    - $h_\theta^{(i)}(x)$를 각 class $i$에 대해 학습시키고 $y = i$인 확률을 예측하여 가장 높은 class로 분류
    - $\displaystyle\max_i h_\theta^{(i)}(x)$
* Softmax function
    - Sigmoid와 유사하나, 모든 $h_\theta^{(i)}(x)$의 합에 대한 각 $h_\theta^{(i)}(x)$의 비율을 계산 ( $\therefore$ 모두 더하면 1)

## Regularization
### The problem of overfitting
* Overfitting(과적합) : feature(variable)가 너무 많으면 training set 학습을 잘 시킬 수 있지만, 새로운 sample에 대한 generalize에 실패할 가능성이 높다.  
1. feature의 수를 줄인다 (Model selection algorithm)
2. **Regularization**
    - 모든 feature를 유지하되, $\theta_j$의 크기/값을 줄인다.
### Cost function
* 기존의 cost function과 유사하나, regularization term을 추가한다. (파라미터 $\theta$가 n개일 때)  
$J(\theta) = \frac1{2m}[\displaystyle\sum_{i=1}m (h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda\displaystyle\sum_{i=1}^n\theta_j^2]$
    - regularization term에 $\theta_0$는 포함 x
    - 모든 가중치를 억눌러 특정 변수에 대한 dependency를 낮추는 역할
        + 상대적으로 의미가 적은 가중치는 매우 작아진다.

* regularization parameter, $\lambda$
    - $\lambda$가 너무 크면 underfitting, 너무 작으면 overfitting 된다.
    - training set으로 최적화한 loss는 일반적으로 test set을 적용한 loss보다 작다. ($\because$ test set이 아닌 training set에 최적화)  
    $\therefore$ test loss가 작을수록, training loss와 test loss간의 차이가 작을수록 정확

### Gradient Descent in Regularization
* Grdient Descent에서 regularization term을 $\theta_j$에 대해 편미분하면 $2\lambda\theta_j$이다.  
$\theta_j:=\theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta)$에서 $\theta_j$가 양수일때와 음수일때 모두 절대값을 작아지는 방향으로 변화시킨다. (= 억누르는 효과)
* Regularization term을 $\lambda\vert\theta_j\vert$로 사용하기도 함
    - 편미분하면 $\frac\partial{\partial\theta_j}\lambda\vert\theta_j\vert = \begin{cases} \lambda & \theta_j \ge 0 \\ -\lambda & \theta_j \lt 0 \end{cases}$
    - 가중치가 상대적으로 작은 $\theta_j$를 0으로 만들 수 있다.

## Cross Validation & Demensionality Reduction
### Cross Validation
* train set을 train set + validation set으로 분리한 뒤, validation set을 사용해 검증하는 방식
* LOOCV(Leave-One-Out Cross Validation)
    - 전체 train set에서 1개의 샘플을 선택하여 그것을 모델 검증에 사용하는 것을 반복하는 방법
    - 학습 양이 많아 속도가 느리지만, imbalance한 상황에서 유용하게 사용될 수 있다.
* k-fold
    - 전체 데이터를 k등분하여 validation set으로 사용하고, 나머지는 training set으로 학습
    - LOOCV에 비해 속도가 빠르다.
* Train, Validation, Test data
    - Train data로 학습(가중치 결정)
    - Validation data로 검증($\lambda$ 결정)
    - Test data로 테스트(오차, 정확도 예측)

### Demensionality Reduction
* High-dim data를 low-dim data로 변환(No. of dimension 필요)
* 장점
    - Less storage
    - Faster computation
    - Noise removal(improving data quality)
        + 얼굴 구분할 때, 안경 유무, 조명 효과 등의 요소 제거
    - 시각화(2D/3D representation)
* Feature Selection
    - Forward selection : Empty set $\rarr$ Add one variable at a time
        + ex) 100개 중 1개의 변수를 골라 학습 $\rarr$ 가장 성능이 좋은 변수 1개 선택 $\rarr$ 선택한 변수와 남은 99개의 변수중 하나를 합해 2개의 변수로 학습 $\rarr$ 성능이 좋은 변수 1개 선택하여 선택한 2개의 변수와 남은 98개의 변수 중 1개 선택 $\rarr$ n개까지 반복
    - Backward elimination : Entire set $\rarr$ Remove one variable at a time
        + ex) 100개 중 1개 변수만 제외해 학습 $\rarr$ 없을 때 가장 성능이 좋아지는 변수 1개 제거 $\rarr$ 남은 99개중 1개의 변수 제외해 학습 $\rarr$ n번 반복
* Feature Extraction
    - 여러개의 feature(=variable, dimension)가 결합되어 reduced dimension 구성
    - Linear vs Non-linear
        + Linear : 각 reduced dimension을 original dimension의 선형 결합으로 표현

### Principal Component Analysis(PCA)





