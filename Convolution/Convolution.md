

用乘法竖式理解卷积

用consequence一词来解释脉冲响应函数



convolve the input with response

[混响与卷积](/Users/lamberhand/Documents/Study/兴趣/DAFX-Digita Audio Effects-2nd.pdf) P182





The most explanatory case will be the sound reverberation 
$$
y[n]\ =\ \sum^\infin_{-\infin}x[k]\ h[n-k]
$$

$$
\begin{aligned}
f(t)\ *\ g(t)\ &= \int_0^tf(t-\tau)\ g(\tau)\ d\tau\\
&=\int_0^tf(\tau)\ g(t-\tau)\ d\tau
\end{aligned}
$$








如何理解卷积运算 $f(t)\ *\ g(t)\ &= \int_0^tf(t-\tau)\ g(\tau)\ d\tau\\$？



我们首先来看数的竖式乘法。平常我们的方法为
$$
\begin{array}{cccccccc}
&&2&2&3&1&6\\
\times&&&&4&2&1\\
\hline
&&2&2&3&1&6\\
&4&4&6&3&2\\
8&9&2&6&4\\
\hline
9&3&9&5&0&3&6
\end{array}
$$
现在用另一个视角来看待这两个数的相乘



By convolving the signal sequence with the impulse response of the system, we get the consequence





