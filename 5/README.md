# Assignment 5 - Andrew Chan

## Question 1
uppose A is a uniform discrete random variable on the set $\{−1, 0, 1, 2, 3\}$. Let $B$ be a random variable for the number of distinct real values of x for which the following equation is true: $4x^2 + 4Ax + A + 2 = 0$. What is the probability mass function of $B$?

First we can use the quadratic formula where it's $ax^2 + bx + c = 0$
So then:
$a = 4$
$b = 4A$
$c = A + 2$

So the discriminant is:
$\Delta = (4A)^2 - 4(4)(A+2)$
$\Delta = 16A^2 - 16(A+2)$
$\Delta = 16A^2 - 16A - 32$

Then we can determine the number of real solutions

Two real solutions if $ \Delta > 0 $.
One real solution if $ \Delta = 0 $.
No real solutions if $ \Delta < 0 $.

For different values of $ A $:

$
\begin{array}{|c|c|c|c|}
\hline
A & \Delta = 16A^2 - 16A - 32 & \text{Sign of } \Delta & B \text{ (Number of solutions)} \\
\hline
-1 & 16(1) + 16 - 32 = 0 & 0 & 1 \\
0 & 16(0) - 16(0) - 32 = -32 & < 0 & 0 \\
1 & 16(1) - 16(1) - 32 = -32 & < 0 & 0 \\
2 & 16(4) - 16(2) - 32 = 32 & > 0 & 2 \\
3 & 16(9) - 16(3) - 32 = 112 & > 0 & 2 \\
\hline
\end{array}
$

We can then compute the probability mass function

Since $ A $ is uniformly distributed over $ \{-1, 0, 1, 2, 3\} $, each value has probability $ \frac{1}{5} $.

$$
P(B = 0) = P(A = 0) + P(A = 1) = \frac{1}{5} + \frac{1}{5} = \frac{2}{5}
$$

$$
P(B = 1) = P(A = -1) = \frac{1}{5}
$$

$$
P(B = 2) = P(A = 2) + P(A = 3) = \frac{1}{5} + \frac{1}{5} = \frac{2}{5}
$$

Final answer:
$$
P(B = 0) = \frac{2}{5}, \quad P(B = 1) = \frac{1}{5}, \quad P(B = 2) = \frac{2}{5}
$$

## Question 2
The coefficient of skewness of a random variable $X$ is defined to be  

$$
\frac{E[(X - \mu)^3]}{\sigma^3}
$$

Show that the coefficient of skewness of a Bernoulli random variable is  

$$
\frac{1 - 2\pi}{\sqrt{\pi(1 - \pi)}}
$$

$\mu = E[X]$ (mean of $X$)
$\sigma^2 = \text{Var}(X)$ (variance of $X$)
$E[(X - \mu)^3]$ is the third central moment of $X$

A Bernoulli random variable $X$ takes values:
$$
X =
\begin{cases} 
0 \quad (1 - \pi),\\
1 \quad \pi
\end{cases}
$$

$$
E[X] = 1 \cdot \pi + 0 \cdot (1 - \pi) = \pi.
$$

$$
\text{Var}(X) = E[X^2] - (E[X])^2.
$$

Since $X^2 = X$ for a Bernoulli variable,

$$
E[X^2] = E[X] = \pi.
$$

$$
\sigma^2 = \pi - \pi^2 = \pi(1 - \pi).
$$

Therefore, the standard deviation is:
$$
\sigma = \sqrt{\pi(1 - \pi)}.
$$

We can then compute $E[(X - \mu)^3]$
Expanding $(X - \mu)^3$:

$$
E[(X - \mu)^3] = E\left[\left(X - \pi\right)^3\right].
$$

Since $X$ can be either 0 or 1:

- When $X = 1$:

$$
(1 - \pi)^3 \quad \text{occurs with probability } \pi.
$$

- When $X = 0$:

$$
(-\pi)^3 \quad \text{occurs with probability } (1 - \pi).
$$

So,

$$
E[(X - \pi)^3] = \pi (1 - \pi)^3 + (1 - \pi) (-\pi)^3.
$$

Expanding:

$$
= \pi (1 - 3\pi + 3\pi^2 - \pi^3) + (1 - \pi)(-\pi^3).
$$

$$
= \pi - 3\pi^2 + 3\pi^3 - \pi^4 - \pi^3 + \pi^4.
$$

$$
= \pi - 3\pi^2 + 2\pi^3.
$$

Factoring:

$$
= \pi(1 - 3\pi + 2\pi^2).
$$

We could then compute the skewness
Now, dividing by $\sigma^3$:

$$
\frac{E[(X - \mu)^3]}{\sigma^3} = \frac{\pi(1 - 3\pi + 2\pi^2)}{(\pi(1 - \pi))^{3/2}}.
$$

Dividing the numerator and denominator by $\pi(1 - \pi)$:

$$
\frac{1 - 2\pi}{\sqrt{\pi(1 - \pi)}}.
$$

So, we have derived the coefficient of skewness for a Bernoulli random variable:

$$
\gamma_X = \frac{1 - 2\pi}{\sqrt{\pi(1 - \pi)}}.
$$

## Question 3
In a binomial experiment, find $\mu_K$​ and $\sigma_K$ for

a. $n=100$ and $\pi=0.40$
b. $n=400$ and $\pi=0.40$
c. $n=100$ and $\pi=0.60$
d. $n=400$ and $\pi=0.60$

For a binomial experiment the mean $\mu_K$ and standard deviation $\sigma_K$ are:

$$
\mu_K = n\pi
$$
$$
\sigma_K = \sqrt{n\pi(1 - \pi)}
$$

where:
$n$ is the number of trials,
$\pi$ is the probability of success.


a) $n = 100$, $\pi = 0.40$

$$
\mu_K = 100 \times 0.40 = 40
$$

$$
\sigma_K = \sqrt{100 \times 0.40 \times (1 - 0.40)}
$$

$$
= \sqrt{100 \times 0.40 \times 0.60}
$$

$$
= \sqrt{24} \approx 4.90
$$

b) $ n = 400 $, $ \pi = 0.40 $

$$
\mu_K = 400 \times 0.40 = 160
$$

$$
\sigma_K = \sqrt{400 \times 0.40 \times (1 - 0.40)}
$$

$$
= \sqrt{400 \times 0.40 \times 0.60}
$$

$$
= \sqrt{96} \approx 9.80
$$

c) $ n = 100 $, $ \pi = 0.60 $

$$
\mu_K = 100 \times 0.60 = 60
$$

$$
\sigma_K = \sqrt{100 \times 0.60 \times (1 - 0.60)}
$$

$$
= \sqrt{100 \times 0.60 \times 0.40}
$$

$$
= \sqrt{24} \approx 4.90
$$

d) $ n = 400 $, $ \pi = 0.60 $

$$
\mu_K = 400 \times 0.60 = 240
$$

$$
\sigma_K = \sqrt{400 \times 0.60 \times (1 - 0.60)}
$$

$$
= \sqrt{400 \times 0.60 \times 0.40}
$$

$$
= \sqrt{96} \approx 9.80
$$

Final Table Form

| Case  | $ n $ | $ \pi $ | $ \mu_K $ | $ \sigma_K $ |
|-------|------|------|------|------|
| **(a)** | 100  | 0.40 | 40   | 4.90  |
| **(b)** | 400  | 0.40 | 160  | 9.80  |
| **(c)** | 100  | 0.60 | 60   | 4.90  |
| **(d)** | 400  | 0.60 | 240  | 9.80  |

## Question 4

In a test for extrasensory perception (ESP), the subject has to guess which one of three cards lying face down on a table is the ace of spades. Suppose that the subject has no ESP and is just guessing. Find the probability that in 12 guesses, the number of cards guessed correctly is:
a. 4
c. 6
e. at least 6

This is a binomial probability problem because, each guess is independent, the subject has a fixed probability of correctly guessing each card, and there are a fixed number of trials.

A binomial random variable $X$:
$$
\text{Bin}(n, \pi)
$$

where:
$n = 12$ (the number of guesses),
$\pi = \frac{1}{3}$ (since the subject is randomly guessing among 3 cards).

The binomial probability formula is:
$$
P(X = k) = \binom{n}{k} \pi^k (1 - \pi)^{n - k}
$$

where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient (n choose k).

a) Probability of guessing exactly 4 correctly:
$$
P(X = 4) = \binom{12}{4} \left(\frac{1}{3}\right)^4 \left(\frac{2}{3}\right)^{8} \approx 0.2384
$$

c) Probability of guessing exactly 6 correctly:
$$
P(X = 6) = \binom{12}{6} \left(\frac{1}{3}\right)^6 \left(\frac{2}{3}\right)^{6} \approx0.1113
$$

e) Probability of guessing at least 6 correctly:
$$
P(X \geq 6) = \sum_{k=6}^{12} \binom{12}{k} \left(\frac{1}{3}\right)^k \left(\frac{2}{3}\right)^{12-k} \approx 0.1777
$$

## Question 5
There are 30 people at a party and each shakes hands with each other exactly once. How many handshakes take place total? See if you can answer this question by rephrasing it as the number of ways to choose $k$ things out of $n$ total (for some specific $n$ and $k$).

You can think of this problem as the amount of ways you can choose 2 people out of the 30 total. Which means we can say $n = 30$ and $k = 2$ and use:
$$
\binom{30}{2} = \frac{30!}{2!(30-2)!} = \frac{30 \times 29}{2} = 435
$$

So there are 435 handshakes that can occur.
Another way of solving this is by adding up the combinations. For example you have the group of 30 people, and one person at random shakes hands with everyone else. That'll be 29 handshakes. Then you can remove them from the group and select another person at random and have them shake everyone else's hand, which will be 28. And since you are removing the people after they shake hands with someone, you won't have any interferences. If you keep going you'll get to just 2 people shaking hands, and if you add them all up, you'll also get 435. This can be notated as:
$$
\sum_{i=1}^{29}i = 1 + 2 + ... + 29 = 435
$$
Also the reason why it goes to 29 and not 30 is because someone can't shake their own hand so that last 1 person doesn't matter. 