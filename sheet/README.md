General Formulas for Discrete Random Variables
$
E[X] = \sum_{x} x P(X = x)
$  
$
\text{Var}(X) = E[X^2] - (E[X])^2
$  
Where:
$
E[X^2] = \sum_{x} x^2 P(X = x)
$  
$
\sigma = \sqrt{\text{Var}(X)}
$
Bernoulli Distribution: A random variable with only two outcomes: success (1) with probability \(p\) and failure (0) with probability \(1-\pi\).  
$
P(X = x) = \pi^x (1-\pi)^{1-x} \quad \text{for} \quad x \in \{0, 1\}
$  
$
E[X] = \pi
$  
$
\text{Var}(X) = \pi(1-\pi)
$  
$
\text{SD}(X) = \sqrt{\pi(1-\pi)}
$  
Binomial Distribution: Represents the number of successes in $n$ independent Bernoulli trials with success probability $\pi$.  
4 rules, the number of Bernoulli trials $n$ is predetermined. The random variable $K$ is the number of successes in the $n$ trials. The trials are independent. The probability of success $\pi$ is the same for every trial.  
$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \quad \text{for} \quad k = 0, 1, \ldots, n
$  
$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$  
$
E[K] = n\pi
$  
$
\text{Var}(K) = n\pi(1-\pi)
$  
$
\text{SD}(K) = \sqrt{n\pi(1-\pi)}
$  
A waiting time for repeated Bernoulli trials is a memoryless process in the sense that a long string of failures does not make the next ace come sooner.  
$
Pr(T > s + t | T > s) = Pr(T > t)
$  
Geometric Distribution: Models the number of trials until the first success in a sequence of independent Bernoulli trials with success probability $p$.  
$
P(T = t) = (1-\pi)^{t-1} \pi \quad \text{for} \quad t = 1, 2, 3, \ldots
$  
$
E[T] = \frac{1}{\pi}
$  
$
\text{Var}(T) = \frac{1-\pi}{\pi^2}
$  
Discrete Uniform Distribution: Each of the $n$ discrete outcomes has an equal probability of occurring.
$
P(U = u) = \frac{1}{n} \quad \text{for} \quad u = 1, 2, \ldots, u
$  
$
E[U] = \frac{u+1}{2} = \Sigma_{\text{all u}}uP(U=u)
$  
$
\text{Var}(U) = E(U^2) - E^2(U)
$  
Null Hypothesis (H₀) vs. Alternative Hypothesis (Hₐ)  
Null Hypothesis (H₀): The default assumption, often representing "no effect" or "no difference."  
Alternative Hypothesis (Hₐ): The hypothesis the researcher aims to support, suggesting a significant effect or difference.  
Type I Error (False Positive): Rejecting the null hypothesis when it is actually true. Denoted by: α (Alpha)
Type II Error (False Negative): Failing to reject the null hypothesis when the alternative hypothesis is true. Denoted by: β (Beta)  
The sign test is used to test a hypothesis for the median of a population. Data points are marked + or - depending on whether they are above or below the proposed MEDIAN. Then, the number of + signs is used as a test statistic in a binomial test.  
$
\text{p-value} = Pr(K \geq k_s) = 1 - Pr(K \leq k_s)
$  
The Binomial Exact Test is used to determine whether the observed proportion of successes in a binary outcome experiment is consistent with a specified probability under the null hypothesis. It is ideal when sample sizes are small or when the normal approximation to the binomial is not suitable. Testing if the proportion of successes $p$ matches a hypothesized proportion $p_0$. Suitable for binary outcomes.