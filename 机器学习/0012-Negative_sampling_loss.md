# Negative Sampling Loss

Negative Sampling是[NCE](./0011-NCE_loss.md)的一个延伸，也是将多分类问题转化成二分类问题，区别是定义条件概率的方式不一样

## 原理

负采样损失定义条件概率方式如下：

$$
p^h(D=1|w, \theta) = \frac{p_{\theta}^h(w)}{p_{\theta}^h(w) + 1} = \frac{u_{\theta}(w,h)}{u_{\theta}(w,h)+1} = \frac{1}{1+exp(-s_\theta(w,h))} = \sigma(s_\theta(w, h))
$$

$$
p^h(D=0|w, \theta) = \frac{1}{p_{\theta}^h(w) + 1} = \frac{1}{u_{\theta}(w,h)+1} = \sigma(-s_\theta(w,h))=1-\sigma(s_\theta(w,h))
$$

目标函数(max)：
$$
\begin{aligned} {\widehat{J^{h}}}(\theta) &= \log \sigma(s_{\theta}(w_i,h)) + \sum_{j=1}^{k} \log (1 - \sigma(\Delta s_{\theta}(w_j,h))) \end{aligned}
$$
$$
{\widehat{J}}(\theta) = \frac{1}{b} \sum_{i=1}^{b} {\widehat{J^{h_i}}}(\theta)
$$

## 与NCE的异同

相同点：NS是NCE一个变种，当NCE中K=|V|，采样概率等于均匀采样时，NS与NCE等同。

区别：NS中完全忽略了负样本的采样分布，定义的条件概率与实际条件概率差异较大，因此最后优化出的概率模型与实际模型不一致。但这不影响NS用来学习embedding，因为根据NCE导数损失函数，负采样概率部分不影响embedding梯度。


