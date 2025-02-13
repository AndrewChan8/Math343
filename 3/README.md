# Assignment 3 - Andrew Chan
## Question 1
The American Cancer Society as well as the medical profession recommend that people have themselves checked annually for any cancerous growths. If a person has cancer, then the probability is 0.99 that it will be detected by a test. Furthermore, the probability that the test results will be positive when no cancer actually exists is 0.10. Government records indicate that 8% of the population in the vicinity of a paint manufacturing plant has some form of cancer. Find $PV^+$ and $PV^-$

$ PV^+ = P(\text{Cancer}|\text{Positive Test})$
$ PV^- = P(\text{No Cancer}|\text{Negative Test})$
$ P(\text{Cancer}) = 0.08 $ (8% of the population has cancer)
$ P(\text{No Cancer}) = 1 - P(\text{Cancer}) = 0.92$
Sensitivity $ P(\text{Positive Test | Cancer}) = 0.99 $
False positive rate $ P(\text{Positive Test | No Cancer}) = 0.10 $
Specificity $ P(\text{Negative Test}|\text{No Cancer}) = 1 - \text{False Positive Rate} = 0.90 $

#### Using Bayes' Theorem for $PV^+$:
$$
PV^+ = \frac{P(\text{Positive Test | Cancer}) \cdot P(\text{Cancer})}{P(\text{Positive Test})}
$$
Use the law of total probability to find $P(\text{Positive Test})$:
$
P(\text{Positive Test}) = P(\text{Positive Test | Cancer}) \cdot P(\text{Cancer}) + P(\text{Positive Test | No Cancer})\cdot P(\text{No Cancer})
$
Substitute the values:
$ P(\text{Positive Test})=(0.99⋅0.08)+(0.10⋅0.92)=0.0792+0.092=0.1712 $
Calculate $PV^+$:
$$
PV^+ = \frac{0.99 \cdot 0.08}{0.1712} = \frac{0.0792}{0.1712} \approx 0.4626 \, (46.26\%)
$$
#### Using Bayes' Theorem for $PV^-$:
$$
PV^- = \frac{P(\text{Negative Test | No Cancer}) \cdot P(\text{No Cancer})}{P(\text{Negative Test})}
$$
Use the law of total probability to find $P(\text{Negative Test})$:
$$
P(\text{Negative Test}) = P(\text{Negative Test | Cancer}) \cdot P(\text{Cancer}) + P(\text{Negative Test | No Cancer}) \cdot P(\text{No Cancer})
$$
Substitute the values:
$
P(\text{Negative Test | Cancer}) = 1 - P(\text{Positive Test | Cancer}) = 1 - 0.99 = 0.01
$
$
P(\text{Negative Test}) = (0.01 \cdot 0.08) + (0.90 \cdot 0.92) = 0.0008 + 0.828 = 0.8288
$

Calculate $PV^-$:
$$
PV^- = \frac{0.90 \cdot 0.92}{0.8288} = \frac{0.828}{0.8288} \approx 0.999 \, (99.9\%)
$$

## Question 2
Let A and B be events with nonzero probability of occurring. Prove that A and B are independent if and only if A and B′ are independent.

Events $A$ and $B$ are independent if:
$ P(A \cap B) = P(A) \cdot P(B) $
$B'$ is the complement of $B$, so $P(B') = 1 - P(B)$.

Forward Direction: If $A$ and $B$ are independent, then $A$ and $B'$ are independent.

Assume $A$ and $B$ are independent:
$P(A \cap B) = P(A) \cdot P(B)$

Using the complement rule:
$P(A \cap B') = P(A) - P(A \cap B)$

Substitute $P(A \cap B) = P(A) \cdot P(B)$:
$P(A \cap B') = P(A) - P(A) \cdot P(B)$

Factorize $P(A)$:
$P(A \cap B') = P(A) \cdot (1 - P(B))$

Since $1 - P(B) = P(B')$, we have:
$P(A \cap B') = P(A) \cdot P(B')$

Therefore, $A$ and $B'$ are independent.

---

Reverse Direction: If $A$ and $B'$ are independent, then $A$ and $B$ are independent.
Assume:
$P(A \cap B') = P(A) \cdot P(B')$

Using the complement rule:
$P(A \cap B) = P(A) - P(A \cap B')$

Substitute $P(A \cap B') = P(A) \cdot P(B')$:
$P(A \cap B) = P(A) - P(A) \cdot P(B')$

Factorize $P(A)$:
$P(A \cap B) = P(A) \cdot (1 - P(B'))$

Since $1 - P(B') = P(B)$, we have:
$P(A \cap B) = P(A) \cdot P(B)$

Thus, $A$ and $B$ are independent.

We have shown that:
1. If $A$ and $B$ are independent, then $A$ and $B'$ are independent.
2. If $A$ and $B'$ are independent, then $A$ and $B$ are independent.

Therefore, $A$ and $B$ are independent and $A$ and $B'$ are independent.

## Question 3
You go to a beach party. Two of you are bringing coolers with sandwiches. Your cooler contains 10 ham sandwiches and 5 cheese sandwiches. Your friend's cooler has 6 ham and 9 cheese sandwiches. At the beach, someone takes a sandwich at random from one of the coolers. It turns out to be a ham sandwich. What is the probability that the sandwich came from your cooler? First, sketch a tree diagram. Then use Bayes' method to compute the probability.

Bayes' Theorem States:
$$P(M | H) = \frac{P(H | M) \cdot P(M)}{P(H)}$$

$P(M∣H)$: Probability the ham sandwich came from your cooler.
$P(H∣M)$: Probability of picking a ham sandwich from your cooler.
$P(M)$: Probability of picking a sandwich from your cooler.
$P(H)$: Total probability of picking a ham sandwich.

![sandwich](sandwich.png)
$P(M) = P(F) = \frac{1}{2} $
$P(H|M) = \frac{10}{15} = \frac{2}{3}$
$P(H|F) = \frac{6}{15} = \frac{2}{5}$

Using the law of total probability:
$P(H) = P(H∣M) \cdot P(M)+P(H∣F) \cdot P(F)$
Substitute the values:
$P(H) = (\frac{2}{3} \cdot \frac{1}{2}) + (\frac{2}{5} \cdot \frac{1}{2})$
$P(H) = \frac{1}{3} + \frac{1}{5} = \frac{5}{15} + \frac{3}{15} = \frac{8}{15}$

Substitute into Bayes' Theorem:
$P(M | H) = \frac{P(H | M) \cdot P(M)}{P(H)}$
$P(M | H) = \frac{\frac{2}{3} \cdot \frac{1}{2}}{\frac{8}{15}}$

Simplify:
$\frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3}$
$P(M | H) = \frac{\frac{1}{3}}{\frac{8}{15}} = \frac{1}{3} \cdot \frac{15}{8} = \frac{15}{24} = \frac{5}{8}$

Final answer:
$P(M | H) = \frac{5}{8} = 0.625 \, (62.5\%)$

## Question 4
Consider the outcome set corresponding to a roll of two fair six-sided dice (one blue and one green). Define 3 events, A, B, and C, such that the events are pairwise independent but not mutually independent.

Each outcome can be represented as an ordered pair $(x,y)$, where $x$ is the result on the blue die and $y$ is the result on the green die. The sample space has $6×6=36$ outcomes.


Define the events $A$, $B$, and $C$:
1. $A = \{(x, y) \mid x + y \text{ is even}\}$:
- The event $A$ corresponds to all outcomes where the sum of the dice is even. This happens when both dice show even numbers or both show odd numbers.

2. $B = \{(x, y) \mid x \text{ is even}\}$:
- The event $B$ corresponds to all outcomes where the blue die shows an even number ($x = 2, 4, 6$).

3. $C = \{(x, y) \mid y \text{ is even}\}$:
- The event $C$ corresponds to all outcomes where the green die shows an even number ($y = 2, 4, 6$).


Two events $E_1$ and $E_2$ are independent if:
$P(E_1 \cap E_2) = P(E_1) \cdot P(E_2)$
1. $P(A)$: Half of the outcomes have an even sum ($x + y$), so:
$P(A) = \frac{18}{36} = \frac{1}{2}$
2. $P(B)$: Half of the outcomes have an even number on the blue die, so:
$P(B) = \frac{18}{36} = \frac{1}{2}$
3. $P(C)$: Half of the outcomes have an even number on the green die, so:
$P(C) = \frac{18}{36} = \frac{1}{2}$

Checking Pairwise Independence
1. $ A $ and $ B $:
- $ A \cap B $: Both dice have even numbers, so $ x + y $ is even, and the blue die is even. This corresponds to 9 outcomes:  
$ (2,2), (2,4), \dots, (6,6) $.

$P(A \cap B) = \frac{9}{36} = \frac{1}{4}$

$P(A) \cdot P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$

Since $ P(A \cap B) = P(A) \cdot P(B) $, events $ A $ and $ B $ are independent.
2. $ A $ and $ C $:
- Similar reasoning shows:
$P(A \cap C) = \frac{1}{4}, \quad P(A) \cdot P(C) = \frac{1}{4}$

Thus, $ A $ and $ C $ are independent.
3. $ B $ and $ C $:
- Both dice are even, so:

$P(B \cap C) = \frac{1}{4}, \quad P(B) \cdot P(C) = \frac{1}{4}$

Thus, $ B $ and $ C $ are independent.


Step 3: Verify Not Mutually Independent
Three events $ A $, $ B $, and $ C $ are mutually independent if:

$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$

Compute $ P(A \cap B \cap C) $:
- For $ A \cap B \cap C $, both dice must be even. There are 9 outcomes where this happens.

$P(A \cap B \cap C) = \frac{9}{36} = \frac{1}{4}$


Compute $ P(A) \cdot P(B) \cdot P(C) $:
$P(A) \cdot P(B) \cdot P(C) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$

Since:
$P(A \cap B \cap C) \neq P(A) \cdot P(B) \cdot P(C)$

The events $ A $, $ B $, and $ C $ are **not** mutually independent.

Therefore, the events $ A = \{ x + y \text{ is even} \} $, $ B = \{ x \text{ is even} \} $, and $ C = \{ y \text{ is even} \} $ are **pairwise independent** but **not mutually independent**.

## Question 5
Suppose $E$ and $F$ are disjoint events with
$P(E)=0.20$ and $P(F)=0.50$.

a. Find the probability that both $E$ and $F$ occur.
Since $E$ and $F$ are disjoint, the probability that both occur $P(E \cap F)$ is:
$P(E \cap F) = 0$

b. Find the probability that either $E$ or $F$ occurs.
The probability that either $E$ or $F$ occurs is $P(E \cup F)$. For disjoint events:
$P(E \cup F) = P(E) + P(F)$
Substitute the values:
$P(E \cup F) = 0.20 + 0.50 = 0.70$

c. Find the probability that $F$ occurs and $E$ does not occur.
Since $E$ and $F$ are disjoint, $F$ occurring means $E$ does not occur. The probability is simply:
$P(F \cap E') = P(F)$
Substitute the value:
$P(F \cap E') = 0.50$

d. Find the probability that neither occurs.
The probability that neither $E$ nor $F$ occurs is $P((E \cup F)')$, which is the complement of $P(E \cup F)$. Use:
$P((E \cup F)') = 1 - P(E \cup F)$
Substitute the value:
$P((E \cup F)') = 1 - 0.70 = 0.30$

a. $P(E \cap F) = 0$  
b. $P(E \cup F) = 0.70$  
c. $P(F \cap E') = 0.50$  
d. $P((E \cup F)') = 0.30$  


## Question 6
Suppose $E$ and $F$ are independent events with
$P(E)=0.20$ and $P(F)=0.50$.

a. Find the probability that both $E$ and $F$ occur.
Since $E$ and $F$ are independent:
$P(E \cap F) = P(E) \cdot P(F)$
Substitute the values:
$P(E \cap F) = 0.20 \cdot 0.50 = 0.10$


b. Find the probability that either $E$ or $F$ occur.
The probability that either $E$ or $F$ occurs is $P(E \cup F)$, which is given by:
$P(E \cup F) = P(E) + P(F) - P(E \cap F)$
Substitute the values:
$P(E \cup F) = 0.20 + 0.50 - 0.10 = 0.60$

c. Find the probability that FF occurs and $E$ does not occur.
The probability that $F$ occurs and $E$ does not occur is $P(F \cap E')$, which is:
$P(F \cap E') = P(F) - P(F \cap E)$
Since $P(F \cap E) = P(E \cap F)$, substitute the values:
$P(F \cap E') = 0.50 - 0.10 = 0.40$

d. Find the probability that neither occurs.
The probability that neither $E$ nor $F$ occurs is $P((E \cup F)')$, which is the complement of $P(E \cup F)$:
$P((E \cup F)') = 1 - P(E \cup F)$
Substitute the value:
$P((E \cup F)') = 1 - 0.60 = 0.40$

a. $P(E \cap F) = 0.10$  
b. $P(E \cup F) = 0.60$  
c. $P(F \cap E') = 0.40$  
d. $P((E \cup F)') = 0.40$  

## Question 7
A box contains 2 red and 3 white balls, and a second box contains 2 red and 4 white balls. A ball is chosen randomly from each box. Find probabilities of the following events:

a. That both balls are red.
This is the probability of choosing a red ball from Box 1 and a red ball from Box 2:
$P(\text{Both Red}) = P(\text{Red (Box 1)}) \cdot P(\text{Red (Box 2)})$
Substitute the values:
$P(\text{Both Red}) = \frac{2}{5} \cdot \frac{1}{3} = \frac{2}{15}$

b. That both are white.
This is the probability of choosing a white ball from Box 1 and a white ball from Box 2:
$P(\text{Both White}) = P(\text{White (Box 1)}) \cdot P(\text{White (Box 2)})$
Substitute the values:
$P(\text{Both White}) = \frac{3}{5} \cdot \frac{2}{3} = \frac{6}{15} = \frac{2}{5}$

c. That both are the same color.
$P(\text{Same Color}) = P(\text{Both Red}) + P(\text{Both White})$
Substitute the values:
$P(\text{Same Color}) = \frac{2}{15} + \frac{6}{15}$
Convert to a common denominator:
$P(\text{Same Color}) = \frac{8}{15}$

d. That the balls are different colors.
The probability of different colors is the complement of the probability of the same color:
$P(\text{Different Color}) = 1 - P(\text{Same Color})$
Substitute the value:
$P(\text{Different Color}) = 1 - \frac{8}{15} = \frac{7}{15}$

a. $P(\text{Both Red}) = \frac{2}{15}$  
b. $P(\text{Both White}) = \frac{2}{5}$  
c. $P(\text{Same Color}) = \frac{8}{15}$  
d. $P(\text{Different Color}) = \frac{7}{15}$

## Question 8
#### Part a
A string of 20 Christmas lights is wired in series (that is, if one bulb fails, then the entire string fails to light). If the probability of any particular bulb failing sometime during the holiday season is 0.005, and if the failures are independent events, what is the probability that the lights will fail sometime during the holiday season?

Step 1: Probability that a single bulb does not fail

The probability that a single bulb does not fail is:
$P(\text{No Failure for a bulb}) = 1 - P(\text{Failure for a bulb}) = 1 - 0.005 = 0.995$

Step 2: Probability that all 20 bulbs do NOT fail

Since the bulbs are independent, the probability that all 20 bulbs do not fail is:
$P(\text{No Failure for all 20 bulbs}) = \left(P(\text{No Failure for a bulb})\right)^{20}$

Substitute the values:
$P(\text{No Failure for all 20 bulbs}) = (0.995)^{20}$

Step 3: Calculate the probability

We calculate $ (0.995)^{20} $:
$(0.995)^{20} \approx 0.904$

So, the probability that all 20 bulbs do not fail is approximately $ 0.904 $.

Step 4: Probability that at least one bulb fails

The probability that at least one bulb fails is the complement of the probability that all bulbs do not fail:
$P(\text{At least one bulb fails}) = 1 - P(\text{No Failure for all 20 bulbs})$

Substitute the value:
$P(\text{At least one bulb fails}) = 1 - 0.904 = 0.096$

So, the probability that the lights will fail sometime during the holiday season is approximately:
$P(\text{Lights Fail}) = 0.096 \, (9.6\%)$
#### Part b
Do you think that the independence assumption is reasonable for this problem? Why or why not?

I think that the independence assumption in this problem might not be entirely reasonable because of how they can be manufactured. For example, if the bulbs are produced in the same batch or under similar conditions, the failure of one bulb could indicate defects or quality issues that correspond with the other bulbs which makes the failures correlated rather than independent. Another thing to consider are the environmental factors. For example, the surge protectors that they are plugged into or even the temperature and humidity can affect how the bulbs function. Since these factors can cause multiple bulbs to fail simultaneously we can also that they are not independent. In conclusion, the independence assumption might not fully be valid since there are many real world factors such as manufacturing issues and environmental conditions which would lead to correlations between failures. However, it still would be a useful approximation if such factors are minimal. 