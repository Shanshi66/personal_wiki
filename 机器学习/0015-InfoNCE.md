# InfoNCE

损失函数如下，K为负样本个数，$\tau$为温度控制系数，$k_{+}$为正样本，$q$为query。原理同[Sampled Softmax](0013-sampled_softmax_loss.md)

![](img/0015-1.png)

## 参考

1. [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722)