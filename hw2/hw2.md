![1531722005224](C:\Users\jm\AppData\Local\Temp\1531722005224.png)

分析：求解有噪声时的错误率。当$y=f(x)$时，$err1 = \mu\times\lambda$,当$y\ne f(x)$时，$err2 = (1-\mu)\times(1- \lambda)$, 故$err = err1 + err2$.

![1531722628761](C:\Users\jm\AppData\Local\Temp\1531722628761.png)

分析：$\lambda$为何值时，$err$与$\mu$值无关。由1可知，$\lambda = 0.5$,$err = 0.5$.

![1531723515194](C:\Users\jm\AppData\Local\Temp\1531723515194.png)

分析：要95%的置信率和0.05的$\epsilon$,直接套用公式：$P[|E_{in}(g) - E_{out}(g)| > \epsilon\le4(2N)^{d_{vc}}exp(-\frac{1}{8}\epsilon^2N)] $,算得结果460000

![1531724870543](C:\Users\jm\AppData\Local\Temp\1531724870543.png)

![1531724887998](C:\Users\jm\AppData\Local\Temp\1531724887998.png)

分析：用计算器算出最小值

![1531727813500](C:\Users\jm\AppData\Local\Temp\1531727813500.png)

分析：同4

![1531731652634](C:\Users\jm\AppData\Local\Temp\1531731652634.png)

分析：$C_{N}^{2}\times2 + 2 = N^2 - N + 2$

![1531743883646](C:\Users\jm\AppData\Local\Temp\1531743883646.png)

分析：找出第一个满足$m_h(k)\ne2^k$的k，$d_{vc} = k - 1$, $d_{vc} = 3$.

![1531744976248](C:\Users\jm\AppData\Local\Temp\1531744976248.png)

分析：将其看作一维问题，将r相等的点视为相同，则问题转化为positive integers，答案为$C_{N+1}^2 + 1$.

![1531746668775](C:\Users\jm\AppData\Local\Temp\1531746668775.png)

分析：由函数可知，这是一个感知器，课上已证明$d_{vc} = d + 1$.

![1531815365701](C:\Users\jm\AppData\Local\Temp\1531815365701.png)

不会

![1531815390795](C:\Users\jm\AppData\Local\Temp\1531815390795.png)

分析：这是一个方波，$d_{vc} = \infin$.

![1531816530477](C:\Users\jm\AppData\Local\Temp\1531816530477.png)

分析：二者都$\le2^N$,当N > $d_{vc}$时，$m_h(N) < 2^N$,$2^im_h(N-i)$还没超过$d_{vc}$,=$2^i\times2^{N-i} = 2^N$,所以，是上界。

![1531817814585](C:\Users\jm\AppData\Local\Temp\1531817814585.png)

分析：成长函数得是严格单调递增的，$2^{\sqrt{N}}$不是

![1531820254495](C:\Users\jm\AppData\Local\Temp\1531820254495.png)

分析：$\ge0$是必然的，因为是交集，所以必然取其中最小的$d_{vc}$.

![1531820640784](C:\Users\jm\AppData\Local\Temp\1531820640784.png)

分析：显然并集包含最少似然函数的下界为$max{d_{vc}(Hk)}_{k=1}^K$，上界可以根据一个特例来说明：有一个$H1$，把平面所有点分为+1，$H2$把平面所有点分为-1。$H1$并$H2$的话为VC dimension为1，而各自$d_{vc}$加起来为0。 

![1531916843380](C:\Users\jm\AppData\Local\Temp\1531916843380.png)

分析：$E_{out}$根据第一题的公式计算，其中的$\lambda$代表$y\ne f(x)$的概率，$\mu$代表$f(x)\ne h(x)$的概率。假设s=1,θ>0s=1,θ>0，此时$h$预测情况：[θ,1]→+1，[−1,θ]→−1，将$f(x)$的四种情况列出来，再与$h(x) = sign(x-\theta)$比较，可知在$[0,\theta]$上$h(x) \ne f(x)$的概率=0.8，其他区间0.2，$\mu = \theta / 2$,代入公式$E_{out} = \lambda \mu + (1-\lambda)(1-\mu)$,得$E_{out} = 0.2 + 0.3\theta$,综合$s$与$\theta$的所有四种情况，可得$E_{out} = 0.5+0.3s(|θ|−1)$.