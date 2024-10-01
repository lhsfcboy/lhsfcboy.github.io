
其中的$N_{K(x,D)}$是在 D 中和点 x 最近的 K 个点的索引，而，$\prod (e)$则是指示函数，其中的 e 表示判断条件，如果 e 为真则$\prod (e) =1$，否则$\prod (e)=0$。

这个方法就是“查看”训练集中与输入值 x 最邻近的 K 个点，然后计算样本中每一类有多少个成员包含于这个集合中，然后返回经验分数作为估计值，如图1.14所示。更正规的表示法如下所示：

$p(y=c|x,D,K) = \frac{1}{K} \sum_{i\in N_{K(x,D)}}\prod (y_i=c)$ (1.2)

$$
\prod (e) = \begin{cases} 1 & \text{if e is true}  \\
0 & \text{if e is false}
\end{cases}
$$(1.3)

这个方法属于一种基于记忆的学习（memory-based learning），也是基于实例的学习（instance-based learning）。具体的概率推导过程在本书的14.7.3。

此处看原书图1.16

$$
\prod (e) = \begin{cases} 1 & \text{if e is true}  \\
0 & \text{if e is false}
\end{cases}
$$(1.3)
