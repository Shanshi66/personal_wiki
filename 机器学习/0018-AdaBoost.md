# AdaBoost

Boosting方法的思想：将一个复杂任务拆解成一系列子任务分别用弱模型解决，然后综合不同模型得到强模型。AdaBoost是其中有代表性的一种。

可以从两个角度来理解Adaboost:
1. 改变数据样本的概率分布，针对不同分布的数据集训练不同的弱模型
2. 通过前向分步算法学习的加法模型

## 角度一：改变样本分布

输入：训练集$T=\{(x_1, y_1), (x_2, y_2), ... , (x_N, y_n)\}, y_i \in \{+1, -1\}$ ，弱学习算法

输出：最终分类器$G(x)$

步骤：
1. 初始化训练数据的权重分布
   $$
    D_1 = (w_{11}, w_{12}, ..., w_{1N}) \\
    w_{1i} = 1/N
   $$

2. 依次训练M个分类器$m=1,2,3,...,M$
   1. 使用具有权值分布$D_m$的训练数据学习得到基本分类器$G_m(x)$
   2. 计算$G_m(x)$在训练数据上的分类误差率
    $$
        e_m = \sum_{i=1}^NP(G_m(x_i) \neq y_i) = \sum_{i=1}^N w_{mi}I(G_m(x_i) \neq y_i)
    $$
   3. 计算$G_m(x)$的系数，当$e_m$越小，$\alpha_m$越大，该模型越重要
    $$
        \alpha_m = \frac{1}{2} \ln \frac{1-e_m}{e_m}
    $$
   4. 更新样本权重，当被误分类，指数为正，样本权重被放大
    $$
        w_{m+1,i} = \frac{w_{mi}}{Z_m} \exp (-\alpha_m y_i G_m(x_i)) \\
        Z_m = \sum_{i=1}^N w_{mi} \exp(-\alpha_m y_i G_m(x_i))
    $$
3. 构建基本分类器的线性组合
   $$
   f(x) = \sum_{m=1}^M \alpha_m G_m(x)
   $$
4. 最终分类器为
   $$
   G(x) = sign(f(x))
   $$


## 角度二：前向分步算法

加法模型
$$
f(x) = \sum_{i=1}^{M} \beta_m b(x; \gamma_m)
$$
其中$b(x;\gamma_m)$为基函数，给定损失函数情况下，求解加法模型需要求解：
$$
\min_{\gamma_m, \beta_m} \sum_{i=1}^N L \left ( y_i, \sum_{i=1}^{M} \beta_m b(x; \gamma_m)\right)
$$

这是一个很复杂的问题，前向分步算法的思想上，每次求解一个基函数，逐步逼近目标结果，即每次求解
$$
(\beta_m, \gamma_m) = \arg \min_{\beta, \gamma} \sum_{i=1}^N L(y_i, f_{m-1}(x_i)+\beta b(x_i; \gamma))
$$

如果$G_m(x) = b(x; \gamma_m), L(y, f(x)) = exp(-yf(x))$，那么最终结果与AdaBoost结果一致。


## 参考

1. 李航《机器学习方法》

