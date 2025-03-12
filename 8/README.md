# Assignment 8
## Question 1
Find the probability density function $ f $ for the continuous random variable $ X $ with cumulative distribution function
$$
F(x) =
\begin{cases} 
0, & \text{for } x < 5 \\
\frac{x}{5} - 1, & \text{for } 5 \leq x < 10 \\
1, & \text{for } x \geq 10
\end{cases}
$$


The probability density function $ f(x) $ is obtained by differentiating $ F(x) $:

$$
f(x) = \frac{d}{dx} F(x)
$$

For $ x < 5 $:
Since $ F(x) = 0 $, we have:
$$
f(x) = 0
$$

For $ 5 \leq x < 10 $:
$$
F(x) = \frac{x}{5} - 1
$$
Differentiating:
$$
f(x) = \frac{d}{dx} \left( \frac{x}{5} - 1 \right) = \frac{1}{5}
$$

For $ x \geq 10 $:
Since $ F(x) = 1 $:
$$
f(x) = 0
$$

Final Answer:
$$
f(x) =
\begin{cases} 
0, & \text{for } x < 5 \\
\frac{1}{5}, & \text{for } 5 \leq x < 10 \\
0, & \text{for } x \geq 10
\end{cases}
$$

## Question 2
Find each of the following for the density function  
$$
f(x) =
\begin{cases} 
|x|, & \text{for } -1 \leq x \leq 1 \\
0, & \text{elsewhere}
\end{cases}
$$

(
  a) The cumulative distribution function $ F $
For $ x < -1 $, the probability is 0 because $ f(x) = 0 $ there.

$$
F(x) = 0, x < -1
$$

For $ -1 \leq x < 0 $, the PDF is $ f(s) = -s $, so we integrate:

$$
F(x) = \int_{-1}^{x} (-s) ds
$$

Computing the integral:

$$
F(x) = \left[ -\frac{s^2}{2} \right]_{-1}^{x}
$$

$$
F(x) = -\frac{x^2}{2} + \frac{(-1)^2}{2}
$$

$$
F(x) = -\frac{x^2}{2} + \frac{1}{2}
$$

For $ 0 \leq x \leq 1 $, the PDF is $ f(s) = s $, so:

$$
F(x) = F(0) + \int_{0}^{x} s ds
$$

Since $ F(0) = \frac{1}{2} $, we compute:

$$
\int_{0}^{x} s ds = \frac{x^2}{2}
$$

$$
F(x) = \frac{1}{2} + \frac{x^2}{2}
$$

For $ x > 1 $, all probability has been accounted for:

$$
F(x) = 1, \quad x > 1
$$

$$
F(x) =
\begin{cases}
0, & x < -1 \\
\frac{1}{2} - \frac{x^2}{2}, & -1 \leq x < 0 \\
\frac{1}{2} + \frac{x^2}{2}, & 0 \leq x \leq 1 \\
1, & x > 1
\end{cases}
$$

(b) $ F(-0.50) $
For $ -1 \leq x < 0 $:

$$
F(-0.50) = \frac{1}{2} - \frac{(-0.50)^2}{2}
$$

$$
= \frac{1}{2} - \frac{0.25}{2} = \frac{1}{2} - \frac{1}{8} = \frac{4}{8} - \frac{1}{8} = \frac{3}{8} = 0.375
$$

(c) $ P(X \geq 0) $  
$$
P(X \geq 0) = 1 - F(0)
$$

From our CDF,

$$
F(0) = \frac{1}{2}
$$

$$
P(X \geq 0) = 1 - \frac{1}{2} = \frac{1}{2} = 0.5
$$

(d) $ F(0.75) $  
For $ 0 \leq x \leq 1 $:

$$
F(0.75) = \frac{1}{2} + \frac{(0.75)^2}{2}
$$

$$
= \frac{1}{2} + \frac{0.5625}{2} = \frac{1}{2} + 0.28125 = 0.78125
$$

(e) $ P(-0.50 < X \leq 0.75) $  
$$
P(-0.50 < X \leq 0.75) = F(0.75) - F(-0.50)
$$

Using our computed values:

$$
P(-0.50 < X \leq 0.75) = 0.78125 - 0.375 = 0.40625
$$

Final Answers:
(a) CDF:  
  $$
  F(x) =
  \begin{cases}
  0, & x < -1 \\
  \frac{1}{2} - \frac{x^2}{2}, & -1 \leq x < 0 \\
  \frac{1}{2} + \frac{x^2}{2}, & 0 \leq x \leq 1 \\
  1, & x > 1
  \end{cases}
  $$
(b) $ F(-0.50) = 0.375 $
(c) $ P(X \geq 0) = 0.5 $
(d) $ F(0.75) = 0.78125 $
(e) $ P(-0.50 < X \leq 0.75) = 0.40625 $



## Question 3
Find each of the following for the density function  

$$
f(x) =
\begin{cases} 
e^{-x}, & \text{for } 0 \leq x < \infty \\
0, & \text{for } x < 0
\end{cases}
$$

(a) The cumulative distribution function $ F $  

Case 1: $ x < 0 $
Since $ f(x) = 0 $ for $ x < 0 $, the cumulative probability is also 0:

$$
F(x) = 0, \quad x < 0
$$

Case 2: $ x \geq 0 $
For $ x \geq 0 $, we integrate $ f(s) = e^{-s} $ from 0 to $ x $:

$$
F(x) = \int_0^x e^{-s} ds
$$

Computing the integral:

$$
F(x) = \left[ -e^{-s} \right]_0^x
$$

$$
F(x) = -e^{-x} + e^{0}
$$

$$
F(x) = 1 - e^{-x}
$$

Final CDF Expression
$$
F(x) =
\begin{cases}
0, & x < 0 \\
1 - e^{-x}, & x \geq 0
\end{cases}
$$

(b) $ F(0) $
Using our CDF formula for $ x \geq 0 $:

$$
F(0) = 1 - e^{-0} = 1 - 1 = 0
$$

(c) $ F(1) $
$$
F(1) = 1 - e^{-1} \approx 1 - 0.3679 = 0.6321
$$

(d) $ P(X \geq 1) $
By definition, $ P(X \geq 1) $ is:

$$
P(X \geq 1) = 1 - F(1)
$$

$$
= 1 - (1 - e^{-1})
$$

$$
= e^{-1} \approx 0.3679
$$

(e) $ P(1 < X \leq 2) $

$$
P(1 < X \leq 2) = F(2) - F(1)
$$

Compute $ F(2) $:

$$
F(2) = 1 - e^{-2} \approx 1 - 0.1353 = 0.8647
$$

Subtract $ F(1) $:

$$
P(1 < X \leq 2) = 0.8647 - 0.6321 = 0.2326
$$

(a) CDF:
  $$
  F(x) =
  \begin{cases}
  0, & x < 0 \\
  1 - e^{-x}, & x \geq 0
  \end{cases}
  $$
(b) $ F(0) = 0 $
(c) $ F(1) = 0.6321 $
(d) $ P(X \geq 1) = 0.3679 $
(e) $ P(1 < X \leq 2) = 0.2326 $

## Question 4
Given the probability density function  
$$
f(x) = 20x^3(1 - x) \quad \text{for } 0 < x < 1 \text{ and } 0 \text{ elsewhere}
$$

find the following:

(a) Find the Cumulative Distribution Function \( F(x) \)  

The cumulative distribution function (CDF) is given by:

$$
F(x) = P(X \leq x) = \int_{0}^{x} f(s) ds
$$

For $ 0 < x < 1 $:

$$
F(x) = \int_0^x 20s^3(1 - s) ds
$$

Computing the integral:

\[
F(x) = 20 \left( \frac{x^4}{4} - \frac{x^5}{5} \right)
\]

\[
= 5x^4 - 4x^5
\]

\[
F(x) =
\begin{cases}
0, & x \leq 0 \\
5x^4 - 4x^5, & 0 < x < 1 \\
1, & x \geq 1
\end{cases}
\]

(b) Compute $ E(X) $ (Expected Value of $ X $)

$$
E(X) = \int_{0}^{1} x f(x) dx
$$

Substituting \( f(x) \):

\[
E(X) = 20 \int_0^1 x^4(1 - x) dx
\]

\[
= 20 \left( \frac{1}{5} - \frac{1}{6} \right)
\]

\[
= 20 \times \frac{1}{30} = \frac{20}{30} = \frac{2}{3}
\]

(c) Compute $ E(X^2) $ (Expected Value of $ X^2 $)

\[
E(X^2) = \int_0^1 x^2 f(x) dx
\]

\[
= 20 \left( \frac{1}{6} - \frac{1}{7} \right)
\]

\[
= 20 \times \frac{1}{42} = \frac{20}{42} = \frac{10}{21}
\]

(d) Compute \( SD(X) \) (Standard Deviation of \( X \))

\[
SD(X) = \sqrt{VAR(X)}
\]

$$
VAR(X) = E(X^2) - (E(X))^2
$$

\[
VAR(X) = \frac{10}{21} - \left(\frac{2}{3}\right)^2
\]

\[
VAR(X) = \frac{10}{21} - \frac{4}{9} = \frac{2}{63}
\]

\[
SD(X) = \sqrt{VAR(X)}= \sqrt{\frac{2}{63}}
\]

\[
SD(X) \approx 0.178
\]

(e) Compute \( P(0.5 < X < 2) \)

\[
P(0.5 < X < 2) = F(2) - F(0.5)
\]

Since \( F(2) = 1 \), we only compute \( F(0.5) \):

\[
F(0.5) = 5(0.5)^4 - 4(0.5)^5
\]

\[
= \frac{3}{16} = 0.1875
\]

\[
P(0.5 < X < 2) = 1 - 0.1875 = 0.8125
\]

Final Answers:
(a) CDF:
  \[
  F(x) =
  \begin{cases}
  0, & x \leq 0 \\
  5x^4 - 4x^5, & 0 < x < 1 \\
  1, & x \geq 1
  \end{cases}
  \]
(b) \( E(X) = \frac{2}{3} \)
(c) \( E(X^2) = \frac{10}{21} \)
(d) \( SD(X) \approx 0.178 \)
(e) \( P(0.5 < X < 2) = 0.8125 \)