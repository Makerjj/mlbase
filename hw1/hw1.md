**1.Which of the following problems are best suited for machine learning?** 

(i) Classifying numbers into primes and non-primes

(ii) Detecting potential fraud in credit card charges 

(iii) Determining the time it would take a falling object to hit the ground

(iv) Determining the optimal cycle for traffic lights in a busy intersection 

(v) Determining the age at which a particular medical test is recommended 

Please provide explanation of your choices. 

分析：

判断一个问题是否适合采用机器学习方法的三个准则：

a. 存在某种可以被学习到的潜在规律 

b. 规律难以被简单的定义，直接编写规律的程序是困难的 

c. 有相关的数据 

选择2、4、5

**For Problems 2-5, identify the best type of learning that can be used to solve each task below. Suggested choices include supervised learning, unsupervised learning, active learning, and reinforcement learning. But you can put in other choices as long as your explanations are reasonable.**

2.Play chess better by practicing different strategies and receive outcome as feedback. Please provide explanation of your choice. 

分析：不断根据以往情况学习。  强化学习

3.Categorize books into groups without given topics. Please provide explanation of your choice.

分析：没有分类标签。  无监督学习 

4.Recognize whether there is a face in the picture by a thousand face pictures and ten thousand non-face pictures. Please provide explanation of your choice.

分析：已有参照数据。  监督学习 

5.Selectively schedule experiments on mice to quickly evaluate the potential of cancer medicines. Please provide explanation of your choice. 

分析：主动学习（不了解）

Problem 6-8 are about Off-Training-Set error. Let $\chi = {x_1,x_2,...,x_{N+L}}$ and Y = {−1, +1} (binary classification). Here the set of training examples is $ D = \lbrace (x_n,y_n)\rbrace^N_{n=1} $  , where $y_n ∈ \gamma$, and the set of test inputs is $\lbrace x_{N+\iota}\rbrace^L_{\iota=1}$. The *Off-Training-Set error (OTS)* with respect to an underlying target $f$ and a hypothesis $g$ is

​				$$E_{OTS}(g, f) = \frac{1}{L}\sum_{\iota=1}^L[g(x_{N+\iota}) \neq f(x_{N+\iota})] $

6.Consider$f(x) = +1$ for all x and $g(x) = \lbrace^{+1, for x = x_k and k is odd and 1 \le k \le N + L}_{-1, otherwise}$ . $E_{OTS}(g, f) =?$ Please provide proof of your answer. 

分析：题意即为分析N+1~~N+L有多少个偶数(向上还是向下取证可举例)

​	   $\frac{1}{L}\times(\lfloor \frac{N+l}{2} \rfloor - \lfloor{\frac{N}{2}} \rfloor)$

7.We say that a target function f can “generate” D in a noiseless setting if $f(x_n) = y_n$ for all $(x_n, y_n) ∈ D$. For all possible $f : \chi → \gamma$, how many of them can generate D in a noiseless setting? Note that we call two functions f1 and f2 the same if $f1(x) = f2(x) $for all $x ∈ X $. Please provide proof of your answer.

分析： f的不同取决于$(x_{N+1},y_{N+L}),…,(x_{N+L},y_{N+L})(x_{N+1},y_{N+L}),…,(x_{N+L},y_{N+L})$，则共有$2^L$种可能的输出$y_{N+1},…,y_{N+L},y_{N+1},…,y_{N+L}$结果。 

8.A determistic algorithm A is defined as a procedure that takes D as an input, and outputs a hypothesis g. For any two deterministic algorithms A1 and A2, if all those f that can “generate” D in a noiseless setting are equally likely in probability, please prove or disprove that 

​				$$E_f\lbrace E_{OTS}(A_1(D),f)\rbrace = E_f\lbrace E_{OTS}(A_2(D),f)\rbrace $$



**For Problems 9-12, consider the bin model introduced in class. Consider a bin with infinitely many marbles, and let µ be the fraction of orange marbles in the bin, and ν is the fraction of orange marbles in a sample of 10 marbles.** 

9.If µ = 0.5, what is the probability of ν = µ? Please provide calculating steps of your answer.

10.If µ = 0.9, what is the probability of ν = µ? Please provide calculating steps of your answer. 

11.If µ = 0.9, what is the probability of ν ≤ 0.1? Please provide calculating steps of your answer. 

12.If µ = 0.9, what is the bound given by Hoeffding’s Inequality for the probability of ν ≤ 0.1? Please provide calculating steps of your answer. 

分析：都是一样的做法$C^{10v}_{10}(v^{10v}(1-v)^{(10-10v)})$

**Problems 13-14 illustrate what happens with multiple bins. Please note that the dice is not meant to be thrown for random experiments in this problem. They are just used to bind the six faces together. The probability below only refers to drawing from the bag. **

Consider four kinds of dice in a bag, with the same (super large) quantity for each kind. 

Consider four kinds of dice in a bag, with the same (super large) quantity for each kind. •

 A: all even numbers are colored orange, all odd numbers are colored green • 

B: all even numbers are colored green, all odd numbers are colored orange • 

C: all small (1-3) are colored orange, all large numbers (4-6) are colored green • 

D: all small (1-3) are colored green, all large numbers (4-6) are colored orange 

13.If we pick 5 dice from the bag, what is the probability that we get five orange 1’s? Please provide calculating steps of your answer. 

14.If we pick 5 dice from the bag, what is the probability that we get “some number” that is purely orange? Please provide calculating steps of your answer 

分析：简单的概率计算