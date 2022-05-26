a. It measure how close two distribution are.



b. The KL-divergence can be transferred two cross-entropy added with another entropy.
$$
\begin{align}
D_{KL}(p||q) &= \sum_{i=1}^n p(x_i)log(\frac{p(x_i)}{q(x_i)}) \\
&= \sum_{i=1}^n p(x_i)log(p(x_i)) - \sum_{i=1}^n p(x_i)log(q(x_i))\\
&= -H(p) + H(p,q)
\end{align}
$$
​	In a deep learning model, p is data distribution and q is model distribution. As we can see, KL-divergence is the addition of entropy of data distribution and cross-entropy of  data and model distribution. Whatever the model changes, the entropy of data distribution does not change. Therefore, in most cases, KL-divergence and cross-entropy have the same performance.

