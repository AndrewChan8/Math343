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
In a Newsweek poll, 250 adults under the age of 30 and 500 over the age of 30 were asked:

"Do you believe Americans today are as willing to work hard at their jobs to get ahead as they were in the past?"

Conduct a binomial exact test at the α = 5% level to test whether fewer adults under 30 feel that Americans are as willing to work hard to get ahead than they were in the past. Use π = 1/3.

|             | Yes | No | Row total |
|-------------|----------|---------|---------------|
| Under 30 |    58    |   192   |       250       |
| Over 30  |   145    |   355   |       500       |
| Column total |   203    |   547   |       750       |

Number of "Yes" responses under 30: 58  
Total respondents under 30: 250  
Hypothesized proportion ($\pi$): $\frac{1}{3} \approx 0.333$  
Significance level ($\alpha$): 0.05  

$$
P(X \leq 58) = \sum_{k=0}^{58} \binom{250}{k} (0.333)^k (1-0.333)^{250-k}
$$

$$
P(X \leq 58) \approx 0.00031
$$

The p-value for the binomial exact test is approximately 0.00031.  

Since the p-value (0.00031) is much smaller than the significance level (0.05), we reject the null hypothesis.

This result suggests that significantly fewer adults under 30 feel that Americans are as willing to work hard to get ahead as they were in the past, compared to the hypothesized proportion of $\pi = \frac{1}{3}$.

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
