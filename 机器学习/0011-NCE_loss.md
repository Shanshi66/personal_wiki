# Noise Constrative Estimation

在nlp和推荐系统模型中，由于字典比较大，类别很多，在对softmax求导的时候需要遍历所有类别，使用full softmax计算量很大。为了解决这个问题，一种方法是对softmax进行改进，如层次softmax。另一种方法是基于抽样的softmax，也叫做candidate sampling方法。NCE是其中一种。

## Softmax的问题

在概率模型中，需要将模型的预估分数转化成概率，一般使用softmax实现。公式如下：

$$
p_{\theta}^{h}(w) = \frac{\exp(s_{\theta}(w,h))}{Z_\theta^h} = \frac{u_{\theta}(w,h)}{Z_\theta^h} 
$$

其中，$p_{\theta}^{h}(w)$表示给定上下文h(特征)，词w的概率(标签)

$$
Z_\theta^h = \int\limits_{w^{\prime}} u_{\theta}(w^{\prime},h) dw^{\prime} = \int\limits_{w^{\prime}} \exp(s_{\theta}(w^{\prime},h)) dw^{\prime} 
$$

**由于$Z_\theta^h$对$w$求积分了，因此与$w$无关。**

实际情况下，$w$是离线的，积分可以换成求和

$$
Z_\theta^h = \sum\limits_{w^{\prime}} u_{\theta}(w^{\prime},h) = \sum\limits_{w^{\prime}} \exp(s_{\theta}(w^{\prime},h))
$$

在使用最大似然估计进行求解过程中，添加概率的log，其中有$Z_\theta^h$项，对$\theta$求导需要遍历所有类别，计算成本很高。

$$
\log p_{\theta}^{h}(w) = \log \frac{u_{\theta}(w,h)}{Z_\theta^h} = \log u_{\theta}(w,h) - \log Z_\theta^h = s_{\theta}(w,h) - \log Z_\theta^h
$$

## NCE原理

NCE通过将多分类问题转化成二分类问题从而加快计算：
- 正例：数据集中数据，服从分布$p_d^{h}(w)$
- 负例：从一个噪声分步进行抽样，上下文无关$p_n(w)$，正负样本比例1:k

那么概率，抽样后的概率分布为：

$$
p^h(D=1,w) = \frac{1}{k+1} p_d^h(w)\\ p^h(D=0,w) = \frac{k}{k+1} p_n^h(w)

$$

$$
\begin{aligned} p^h(w) &=  p^h(D=1,w) + p^h(D=0,w) \\ &= \frac{1}{k+1}\big[ p_d^h(w) + kp_n(w) \big] \end{aligned}
$$

$$
\begin{aligned} p^h(D=1|w) &= \frac{p^h(D=1,w)}{p^h(D=1,w)+p^h(D=0,w)} \\ &= \frac{p_d^h(w)}{p_d^h(w) + kp_n(w)}  \end{aligned}
$$

$$
\begin{aligned} p^h(D=0|w) &= \frac{p^h(D=0,w)}{p^h(D=1,w)+p^h(D=0,w)}  \\ &= \frac{kp_n(w)}{p_d^h(w) + kp_n(w)} \\ \end{aligned}
$$

因为我们希望用模型去逼近$p_{d}^{h}(w)$，因此可以用$p_\theta^{h}(w)$代入，得到：

$$
p^h(D=1|w, \theta) = \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \\ p^h(D=0|w, \theta) = \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \\
$$

通过最大似然求解，似然公式：
$$
\begin{aligned} \mathbb{E}_{w \sim p^h(w)}\big[\log p^{h}(d | w, \theta)\big] 
&= \int\limits_{w} p^h(w) \log p^{h}(d | w, \theta) dw 
\\ &= \int\limits_{w} \frac{1}{k+1}\big[ p_d^h(w) + kp_n(w) \big] \log p^{h}(d | w, \theta) dw 
\\ &= \frac{1}{k+1} \big[  \int\limits_{w}  p_d^h(w) \log p^{h}(d | w, \theta) dw + k \int\limits_{w} p_n(w) \log p^{h}(d | w, \theta) dw  \big] 
\\ &= \frac{1}{k+1} \Big\{ \mathbb{E}_{w \sim p_d^h(w)}\big[\log p^{h}(d | w, \theta)\big] + k \mathbb{E}_{w \sim p_n(w)}\big[\log p^{h}(d | w, \theta)\big]  \Big\} \\ \end{aligned}
$$

从$p_d^{h}(w)$中抽样的全是正样本，从$p_n^{h}(w)$中抽样的全是负样本，因此：

$$
\begin{aligned} \mathbb{E}_{w \sim p^h(w)}\big[\log p^{h}(d | w, \theta)\big] &= \frac{1}{k+1} \Big\{ \mathbb{E}_{w \sim p_d^h(w)}\big[\log p^{h}(d | w, \theta)\big] + k \mathbb{E}_{w \sim p_n(w)}\big[\log p^{h}(d | w, \theta)\big]  \Big\} \\ &= \frac{1}{k+1} \Big\{ \mathbb{E}_{w \sim p_d^h(w)}\big[\log p^{h}(D=1 | w, \theta)\big] + k \mathbb{E}_{w \sim p_n(w)}\big[\log p^{h}(D=0 | w, \theta)\big]  \Big\} \\ &= \frac{1}{k+1} \Big\{ \mathbb{E}_{w \sim p_d^h(w)}\big[\log \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \big] + k \mathbb{E}_{w \sim p_n(w)}\big[\log \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \big]  \Big\} \\ \end{aligned}
$$

可以得到目标函数：
$$
J^{h}(\theta) = \mathbb{E}_{w \sim p_d^h(w)}\big[\log \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \big] + k \mathbb{E}_{w \sim p_n(w)}\big[\log \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \big]
$$

但是在以上目标中，要计算$p_\theta^{h}$还是要做normalization。实际上，会将$exp(c^h)$设置为1，一些论文中提到模型可以self-normalization。后文中会提到，如果不这么做，需要每一个上下文学一个normalization参数。
$$
p_{\theta}^h(w) = p_{\theta^0}^h(w) \exp(c^h) = p_{\theta^0}^h(w) = \exp(s_{\theta^0}(w,h)) = u_{\theta^0}(w,h)
$$

在训练过程中会，目标函数中的期望会通过小batch样本进行估计，[A Fast and Simple Algorithm for Training Neural probabilistic Language Models](https://arxiv.org/pdf/1206.6426.pdf)论文中建议一个单词n个负样本, n = k，即
$$

\begin{aligned} {\widehat{J^{h}}}(\theta) &= \frac{1}{m} \sum_{i=1}^{m} \log \frac{p_{\theta}^h(w_i)}{p_{\theta}^h(w_i) + kp_n(w_i)} + \frac{k}{n} \sum_{j=1}^{n} \log \frac{kp_n(w_j)}{p_{\theta}^h(w_j) + kp_n(w_j)} \\ &= \frac{1}{m} \sum_{i=1}^{m} \log \frac{\exp(s_{\theta^0}(w_i,h))}{\exp(s_{\theta^0}(w_i,h)) + kp_n(w_i)} + \frac{k}{n} \sum_{j=1}^{n} \log \frac{kp_n(w_j)}{\exp(s_{\theta^0}(w_j,h)) + kp_n(w_j)} 
\\ &= \log \frac{\exp(s_{\theta^0}(w_i,h))}{\exp(s_{\theta^0}(w_i,h)) + kp_n(w_i)} + \sum_{j=1}^{k} \log \frac{kp_n(w_j)}{\exp(s_{\theta^0}(w_j,h)) + kp_n(w_j)} \end{aligned}
$$


以上目标函数还是显得太复杂，可以进一步简化：
$$
\begin{aligned} p^h(D=1|w, \theta) &= \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \\ &= \frac{1}{1 + \frac{kp_n(w)}{p_{\theta}^h(w)}} \\ &= \frac{1}{1 + \exp(\log \frac{kp_n(w)}{p_{\theta}^h(w)} )} \\ &= \frac{1}{1 + \exp(\log kp_n(w) - \log p_{\theta}^h(w) )} \\ &= \frac{1}{1 + \exp(- (\log p_{\theta}^h(w) - \log kp_n(w)))} \\
 &= \sigma(\log p_{\theta}^h(w) - \log kp_n(w)) \\ &= \sigma(\log \exp(s_{\theta^0}(w,h)) - \log kp_n(w)) \\ &= \sigma(s_{\theta^0}(w,h) - \log kp_n(w)) \\ &= \sigma(\Delta s_{\theta^0}(w,h)) \end{aligned}
$$
$$
\begin{aligned} p^h(D=0|w, \theta) &= 1 - \sigma(\Delta s_{\theta^0}(w,h)) \end{aligned}
$$

最终目标函数可以写成如下，其中b为batchsize,其中$\Delta s_{\theta^0}(w,h) = s_{\theta^0}(w,h) - \log kp_n(w)$
$$
\begin{aligned} {\widehat{J^{h}}}(\theta) &= \sum_{i=1}^{m} \log \sigma(\Delta s_{\theta^0}(w_i,h)) + \frac{k}{n} \sum_{j=1}^{n} \log (1 - \sigma(\Delta s_{\theta^0}(w_j,h))) \end{aligned}
$$
$$
{\widehat{J}}(\theta) = \frac{1}{b} \sum_{i=1}^{b} {\widehat{J^{h_i}}}(\theta)
$$

## NCE性质

对目标函数进行求导：

$$
\begin{aligned} \frac{\partial}{\partial \theta} J^{h}(\theta) &= \frac{\partial}{\partial \theta} \mathbb{E}_{w \sim p_d^h(w)}\big[\log \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \big] + k \frac{\partial}{\partial \theta} \mathbb{E}_{w \sim p_n(w)}\big[\log \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \big] \\ &= \mathbb{E}_{w \sim p_d^h(w)}\big[ \frac{\partial}{\partial \theta} \log \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \big] + k \mathbb{E}_{w \sim p_n(w)}\big[ \frac{\partial}{\partial \theta} \log \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \big]  \\
 &= \mathbb{E}_{w \sim p_d^h(w)}\big[ \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \frac{\partial}{\partial \theta} \log p_{\theta}^h(w) \big] - k \mathbb{E}_{w \sim p_n(w)}\big[ \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \frac{\partial}{\partial \theta} \log p_{\theta}^h(w) \big] \\ 
\\ &= \sum \limits_{w} p_d^h(w) \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \frac{\partial}{\partial \theta} \log p_{\theta}^h(w) - k\sum \limits_{w} p_n(w) \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + kp_n(w)} \frac{\partial}{\partial \theta} \log p_{\theta}^h(w) \\ &= \sum \limits_{w} \frac{kp_n(w)}{p_{\theta}^h(w) + kp_n(w)} \big( p_d^h(w) - p_{\theta}^h(w) \big) \frac{\partial}{\partial \theta} \log p_{\theta}^h(w)  \\ \end{aligned}

$$
当$k \rightarrow \infty$，
$$
\begin{aligned} \frac{\partial}{\partial \theta} J^{h}(\theta) = &= \sum \limits_{w}  \big( p_d^h(w) - p_{\theta}^h(w) \big) \frac{\partial}{\partial \theta} \log p_{\theta}^h(w)  \\ \end{aligned}
$$
和最大似然求导结果一致，这一点是NCE有效性的证明。

而且，当导数等于0，即最优解的时候。$p_d^h(w) - p_{\theta}^h(w) = 0$，即$p_{\theta}^h(w)$不做归一化，也会趋近于实际分布，达到self-normalization的效果。






