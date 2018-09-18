![1532855822053](C:\Users\jm\AppData\Local\Temp\1532855822053.png)

分析：固定噪声是由于target function f 本身$Q_f$太大造成的。若f本身的$Q_f$太大，那么用h去拟合这种高次的目标函数是不容易的，所以固定噪声大。当我们用更小的H‘代替H来拟合f的时候，由于H’更加小，那么对f的拟合程度更加不好，所以deterministic noise会增加 

![1532856894889](C:\Users\jm\AppData\Local\Temp\1532856894889.png)

分析：把定义看懂，带入计算即可，选2

![1532914646619](C:\Users\jm\AppData\Local\Temp\1532914646619.png)

![1532914662425](C:\Users\jm\AppData\Local\Temp\1532914662425.png)

分析：求出$E_{aug}(w)$的偏导数，再根据公式$w_{t+1} = w_t - \eta \frac{\partial E} {\partial w}$,即可求解

![1532915265318](C:\Users\jm\AppData\Local\Temp\1532915265318.png)

不会

![1532917677537](C:\Users\jm\AppData\Local\Temp\1532917677537.png)

参考别人的答案：![1532917868211](C:\Users\jm\AppData\Local\Temp\1532917868211.png)

![1532919411761](C:\Users\jm\AppData\Local\Temp\1532919411761.png)

分析：第一次$2^5$,第二次$2^4$,依次类推

![1532919696494](C:\Users\jm\AppData\Local\Temp\1532919696494.png)

分析:$cost = 10\times(32+16+8+4+2+1) = 630$,1000-630 = 370

![1532930749767](C:\Users\jm\AppData\Local\Temp\1532930749767.png)

答案：1

![1532930861677](C:\Users\jm\AppData\Local\Temp\1532930861677.png)

根据hoffding公式计算即可

![1532930894251](C:\Users\jm\AppData\Local\Temp\1532930894251.png)

分析：真实情况不理想的原因是数据被污染了，因为数据已经被a(x)处理。解决办法：如果能通过a(x)的测试，则再进一步进行g(x)的测试（因为g(x)对a(x)的结果预测效果好）。因此a(x)ANDg(x)，即两者都说“可信”的情况下，真实情况比较好。

![1532932293799](C:\Users\jm\AppData\Local\Temp\1532932293799.png)

分析：直接求导再计算即可 $w = (X^TX+X'^TX')^{-1}(X^TY + X'^TY)$.

![1532932343992](C:\Users\jm\AppData\Local\Temp\1532932343992.png)

分析：$w_{reg} = (z^Tz+\lambda I)^{-1}Z^Ty$,与11题式子作对比即可得到答案 



 

