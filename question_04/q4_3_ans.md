For the first function, it is global minima. First of all the answer is 0, which is the smallest value for $f(x_1,x_2)$

What is more, this function's hessian matrix is semi-positive
$$
H_{f(x_1,x_2)} = \left[
\matrix{
  10 & 8\\
  8 & 10
}
\right]
$$
Therefore, for any vector z
$$
\begin{align}
z^TH_{f(x_1,x_2)}z &= 10x_1^2 + 16x_1x_2 + 10x_2^2 \\
&= 10(x_1+x_2)^2 - 4x_1x_2
\end{align}
$$
When $x_1$ and $x_2$ are both positive or negative, the result is obviously positive.

When one of them is positive and the other is negative, $-4x_1x_2$ is positive and $10(x_1+x_2)^2$ is positive, so the result is still positive.

When $x_1 = x_2 = 0$, the result is zero.

In conclusion, the first function is a convex function, so using gradient descent can definitely find global minima





For the second function,  it is still not a minima because of the gradient is too small when the x is close to optimal. It's hessian matrix is too complex to prove if it is a convex function.

