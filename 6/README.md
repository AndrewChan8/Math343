# Assignment 6
## Question 1
The St. Louis encephalitis virus is also spread by mosquitoes. The probability that a person infected with the virus gets encephalitis is 1 in 150. But of the 70 who developed St. Louis encephalitis in and around Monroe, La., in 2001 three died. Using 3/70 as the probability of a sick person dying from the disease, find the probability that in a sample of 10 independent cases:

a. all will recover
b. exactly 9 persons will recover
c. at least 9 persons recover

Probability that a person with encephalitis dies:  
$$ P(\text{die}) = \frac{3}{70} $$
Probability that a person recovers:  
  $$ P(\text{recover}) = 1 - \frac{3}{70} = \frac{67}{70} $$
We have 10 independent cases. The number of recoveries follows a binomial distribution:  
$$
  P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}
$$
Where:
$ n = 10 $ (total cases),
$ p = \frac{67}{70} $ (probability of recovery),
$ k $ is the number of recoveries.

a) Probability that all will recover $ P(X = 10) $:
$$
P(X = 10) = \left(\frac{67}{70}\right)^{10}
$$

$$
P(X = 10) \approx 0.6453 \quad (64.53\%)
$$

b) Probability that exactly 9 persons will recover $ P(X = 9) $:
$$
P(X = 9) = \binom{10}{9} \left(\frac{67}{70}\right)^9 \left(\frac{3}{70}\right)^1
$$

$$
= 10 \times \left(\frac{67}{70}\right)^9 \times \left(\frac{3}{70}\right)
$$

$$
P(X = 9) \approx 0.2889 \quad (28.89\%)
$$

c) Probability that at least 9 persons recover $ P(X \geq 9) $:
$$
P(X \geq 9) = P(X = 9) + P(X = 10)
$$

$$
P(X \geq 9) \approx 0.9343 \quad (93.43\%)
$$

Final probabilities:

a) All recover: 0.6453 (64.53%)
b) Exactly 9 recover: 0.2889 (28.89%)
c) At least 9 recover: 0.9343 (93.43%)

## Question 2
A speedrunner is trying to get a world record in Super Mario Bros. 3 in the “any% warpless” category. However, near the end of the run, there are 3 independent coin flips such that if any are heads, a hand will pull you down to play an extra level, which takes up additional time. For a world record to be possible, the speedrunner needs a “no hands run”, where all 3 flips are tails.

(a) What is the probability that the speedrunner will get a “no hands run” in at least one of their first 3 attempts?

(b) What is the standard deviation of the number of attempts until the first “no hands run”?

(c) Suppose that after 500 attempts, they have had 43 “no hands runs”. What is the expected number of additional attempts until the next “no hands run”?

There are 3 independent coin flips.
Each flip lands on tails with probability:  
  $$
  P(T) = \frac{1}{2}
  $$
For a "no hands run", all 3 flips must be tails:
  $$
  P(\text{"no hands run"}) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}
  $$
The probability of not getting a "no hands run" is:
  $$
  P(\text{failure}) = 1 - \frac{1}{8} = \frac{7}{8}
  $$

a) Probability of at least one "no hands run" in the first 3 attempts
Using the complement rule:
$$
P(\text{at least one success}) = 1 - P(\text{all failures})
$$

Since the probability of failure in one attempt is \( \frac{7}{8} \), the probability of failing 3 times in a row is:

\[
P(\text{all failures}) = \left(\frac{7}{8}\right)^3
\]

Thus, the probability of at least one success is:

\[
P(\text{at least one "no hands run"}) = 1 - \left(\frac{7}{8}\right)^3
\]

\[
P(\text{at least one success}) \approx 0.3301 \quad (33.01\%)
\]

b) Standard deviation of the number of attempts until the first "no hands run"
The number of attempts until the first success follows a geometric distribution:

\[
X \sim \text{Geom}(p)
\]

where \( p = \frac{1}{8} \) is the probability of a "no hands run" in one attempt.

The standard deviation of a geometric distribution is given by:

\[
\sigma = \frac{\sqrt{1 - p}}{p}
\]

\[
\sigma \approx 7.4833
\]


c) Expected number of additional attempts until the next "no hands run"
From the problem statement:
500 attempts have resulted in 43 "no hands runs".
The empirical probability of a "no hands run" is:

\[
\hat{p} = \frac{43}{500}
\]

Since the number of attempts until the next success is geometrically distributed with probability \( \hat{p} \), the expected number of additional attempts is:

\[
E[X] = \frac{1}{\hat{p}}
\]

\[
E[X] \approx 11.63
\]

Final Answers:
a) Probability of at least one "no hands run" in the first 3 attempts: 0.3301 (33.01%)  
b) Standard deviation of attempts until first "no hands run": 7.4833
c) Expected number of additional attempts until next "no hands run": 11.63

## Question 3
Show that if \( X \) is a discrete random variable, and \( a \) and \( b \) are constants, then  

\[
E(aX + b) = aE(X) + b \quad \text{and} \quad \text{var}(aX + b) = a^2 \text{var}(X).
\]