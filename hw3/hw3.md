![1532224350894](C:\Users\jm\AppData\Local\Temp\1532224350894.png)

分析：简单的计算题，把值代入即可

![1532224388883](C:\Users\jm\AppData\Local\Temp\1532224388883.png)

分析：H是对称的，幂等的，半正定的，存在d+1个特征值为1

对称：$H^T = H$

幂等：$H^2 = H$

半正定：$Hw = \lambda w = H^2w = \lambda^2w$,$\lambda = 0或1$.所有$\lambda \ge0$,所以半正定

存在d+1个特征值为1：$trace(H)=trace(X(XTX)^{−1}XT)=trace((X^TX)^{−1}XTX)=trace(I_{d+1×d+1})=d+1trace(H)=trace(X(XTX)−1XT)=trace((X^TX)^{−1}X^TX)=$

$trace(I_{d+1×d+1})=d+1$ 

![1532229871002](C:\Users\jm\AppData\Local\Temp\1532229871002.png)

![1532229891261](C:\Users\jm\AppData\Local\Temp\1532229891261.png)

分析：以$W^tX$为横坐标，Err为纵坐标画图，可知，答案为b

![1532241576236](C:\Users\jm\AppData\Local\Temp\1532241576236.png)

分析：b,d,e

![1532243201524](C:\Users\jm\AppData\Local\Temp\1532243201524.png)

分析：PLA的参数方程：$w_{t+1} = w_t + sign(w^T_tx_n\ne y_n)x_ny_n$.梯度下降：$w_{t+1} = w_t-\frac{\partial E}{\partial w_t}$

$W^T_tx\ne y$时，$y_nw^T_tx_n < 0$,PLA方程右边第二项变为$x_ny_n$,故$\frac{\partial E}{\partial w_t}=-x_ny_n$,当$y_nw_t^Tx_n<0$时，$\frac{\partial E}{\partial w_t}=0$,答案为c

![1532246618685](C:\Users\jm\AppData\Local\Temp\1532246618685.png)

分析：都是计算，不想做。

![1532336424224](C:\Users\jm\AppData\Local\Temp\1532336424224.png)

分析：题意为能被二次及线性函数分类的所有点的最大个数，答案为6个，具体分析不会

![1532336642562](C:\Users\jm\AppData\Local\Temp\1532336642562.png)

分析：这题的关键在于理解这种特征转换，举个例子，如第1个数据$x_1$，根据上述规则则变为$[1,0,…,0]^T$，（矩阵大小N×1）就是将第几个数对应的行置为1，其他行均为0。显然，不管多少数，其转换后的向量均是线性无关的，因此均可以被shatter，所以$d_{vc}(H_Φ)=∞$.

  

