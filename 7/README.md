# Assignment 7
## Question 1
Use the sign test at the $ \alpha = 0.05 $ level of significance on the hypotheses

$$
H_0: Med = 25 \quad H_a: Med > 25
$$

for a population from which the following sample came:

26.8, 29.2, 27.6, 27.4, 20.9, 30.1, 23.7, 28.3, 25.0, 31.8

Hypotheses:
Null Hypothesis ($H_0$): The median ($Med$) is 25.
Alternative Hypothesis ($H_a$): The median ($Med$) is greater than 25.

Sample Data:
$$
26.8, 29.2, 27.6, 27.4, 20.9, 30.1, 23.7, 28.3, 25.0, 31.8
$$

1. Calculate Signs:
  '+' signs: 7 (values greater than 25)
  '-' signs: 2 (values less than 25)
  Value equal to 25 (excluded): 1

2. Test Statistic:
   The test statistic is the smaller of the counts of '+' or '-' signs:
   $$
   Test Statistic = \min(7, 2) = 2
   $$

3. Significance Level:
   $$
   \alpha = 0.05
   $$

4. p-value Calculation:
   Using the binomial distribution:
   $$
   p\text{-value} = 0.0898
   $$

At a 0.05 significance level, the p-value (0.0898) is greater than 0.05, meaning the result is not statistically significant.

We fail to reject the null hypothesis ($H_0: Med = 25$). There is not enough evidence to support the claim that the median is greater than 25.

## Question 2
A brochure claims that the average daily high temperature in Paris, France, is 18° Celsius in May. 

Suppose that last May the daily high temperature:
Exceeded 18°C on 8 of the 31 days of the month,
Equaled 18°C on 2 days, and
Fell short of 18°C on 21 days.

Test whether the temperature was significantly below the claimed average last May.  
Use α = 0.05.  

Is it appropriate to use a sign test here? Explain.

Claim: The average daily high temperature in Paris in May is 18°C.
Observed Data:
  Above 18°C: 8 days
  Equal to 18°C: 2 days
  Below 18°C: 21 days
  Total days: 31

Hypotheses:
Null Hypothesis ($H_0$): The median temperature is 18°C.
Alternative Hypothesis ($H_a$): The median temperature is below 18°C.

1. Calculate Signs:
  '+' signs: 8 (days above 18°C)
  '-' signs: 21 (days below 18°C)
  Excluded days (equal to 18°C): 2

2. Test Statistic:
   The test statistic is the smaller of the counts of '+' or '-' signs:
   $$
   Test Statistic = \min(8, 21) = 8
   $$

3. Significance Level:
   $$
   \alpha = 0.05
   $$

4. p-value Calculation:
   Using the binomial distribution:
   $$
   p\text{-value} = 0.0121
   $$

At a 0.05 significance level, the p-value (0.0121) is less than 0.05, meaning the result is statistically significant.

We reject the null hypothesis ($H_0: Med = 18°C$). There is sufficient evidence to support the claim that the median temperature was significantly below the claimed average of 18°C last May.

Yes, the sign test is appropriate here because:
We are comparing the median temperature to a specific value (18°C).
The test does not require the data to be normally distributed.
The sign test works well with the ordinal nature of the data (above, below, or equal to the reference value).

## Question 3
Are men more likely than women to be ambidextrous? In a study of 1000 men and 1000 women, 19 men and 7 women were classified as ambidextrous. Use the binomial exact test at the 1% level of significance."

Null Hypothesis (H0): The probability of being ambidextrous is the same for men and women. $ p_{men} = p_{women} $.
Alternative Hypothesis (H1): The probability of being ambidextrous is higher for men than for women. $ p_{men} > p_{women} $.

Men: 19 ambidextrous out of 1000, so $ p_{men} = \frac{19}{1000} = 0.019 $.
Women: 7 ambidextrous out of 1000, so $ p_{women} = \frac{7}{1000} = 0.007 $.

Perform the Binomial Exact Test

Combined Probability Under Null Hypothesis: 
$$
p_{null} = \frac{19 + 7}{1000 + 1000} = 0.013
$$

p-value Calculation: Using a binomial exact test for the alternative hypothesis $ p_{men} > p_{women} $.

p-value: 0.069


Since the p-value (0.069) is greater than the significance level (0.01), we fail to reject the null hypothesis.

There is not enough statistical evidence at the 1% significance level to conclude that men are more likely than women to be ambidextrous based on this study.

## Question 4
To test a new drug, a group of 10 matched pairs of volunteers is used. In each pair, one volunteer is treated with the drug while the other is treated with a placebo as a control. At the end of the double-blind experiment, a physician examines each pair and declares which of the two is healthier. 

Let K be the number of pairs in which the treated patient was declared healthier than the control. 

The null hypothesis ($H_0$) is that the drug is absolutely ineffective (neither good nor bad). It has been decided to reject $H_0$ whenever K > 8.

a. Find $\alpha$, the probability of falsely rejecting $H_0$.

b. Suppose that the drug is so effective that for each matched pair, the probability is 90% that the treated patient will be declared healthier.  
Find $\beta$, the probability of falsely retaining $H_0$.

(a): Find $ \alpha $, the probability of falsely rejecting $H_0$

The probability of falsely rejecting $H_0$ means rejecting the null hypothesis when it is actually true. Under $H_0$, the probability of success (treated patient healthier) is 0.5.

This follows a binomial distribution with:
n = 10 (pairs)
p = 0.5 (probability of success under $H_0$)

We need to calculate:
$$
P(K > 8) = P(K = 9) + P(K = 10)
$$

The binomial probability formula is:
$$
P(K = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

For $P(K = 9)$:
$$
P(K = 9) = \binom{10}{9} (0.5)^9 (0.5)^{10-9} = \binom{10}{9} (0.5)^{10}
$$

For $P(K = 10)$:
$$
P(K = 10) = \binom{10}{10} (0.5)^{10} = (0.5)^{10}
$$

Combining These:
$$
P(K > 8) = \binom{10}{9} (0.5)^{10} + (0.5)^{10}
$$

$$
P(K > 8) = \left[\binom{10}{9} + 1\right] (0.5)^{10}
$$

(b): Find $ \beta $, the probability of falsely retaining $H_0$

The probability of falsely retaining $H_0$ means failing to reject the null hypothesis when it is actually false.

If the drug is effective, then the probability of success (treated patient healthier) is 0.9.

We need to calculate the probability of not rejecting $H_0$, which means K ≤ 8:

$$
P(K \leq 8) = \sum_{k=0}^8 P(K = k)
$$

For a general k from 0 to 8:

$$
P(K = k) = \binom{10}{k} (0.9)^k (0.1)^{10-k}
$$

Combining all terms:

$$
P(K \leq 8) = \sum_{k=0}^8 \binom{10}{k} (0.9)^k (0.1)^{10-k}
$$

### Final Answer:
$\alpha$, the probability of falsely rejecting $H_0$:
$$
P(K > 8) = \left[\binom{10}{9} + 1\right] (0.5)^{10}
$$

$\beta$, the probability of falsely retaining $H_0$:
$$
P(K \leq 8) = \sum_{k=0}^8 \binom{10}{k} (0.9)^k (0.1)^{10-k}
$$
