# Assignment 2 - Andrew Chan
## Question 1

Write out all 70 possibilities:  
1: OOOOXXXX
2: OOOXOXXX
3: OOOXXOXX
4: OOOXXXOX
5: OOOXXXXO
6: OOXOOXXX
7: OOXOXOXX
8: OOXOXXOX
9: OOXOXXXO
10: OOXXOOXX  
11: OOXXOXOX
12: OOXXOXXO
13: OOXXXOOX
14: OOXXXOXO
15: OOXXXXOO
16: OXOOOXXX
17: OXOOXOXX
18: OXOOXXOX
19: OXOOXXXO
20: OXOXOOXX  
21: OXOXOXOX
22: OXOXOXXO
23: OXOXXOOX
24: OXOXXOXO
25: OXOXXXOO
26: OXXOOOXX
27: OXXOOXOX
28: OXXOOXXO
29: OXXOXOOX
30: OXXOXOXO  
31: OXXOXXOO
32: OXXXOOOX
33: OXXXOOXO
34: OXXXOXOO
35: OXXXXOOO
36: XOOOOXXX
37: XOOOXOXX
38: XOOOXXOX
39: XOOOXXXO
40: XOOXOOXX  
41: XOOXOXOX
42: XOOXOXXO
43: XOOXXOOX
44: XOOXXOXO
45: XOOXXXOO
46: XOXOOOXX
47: XOXOOXOX
48: XOXOOXXO
49: XOXOXOOX
50: XOXOXOXO  
51: XOXOXXOO
52: XOXXOOOX
53: XOXXOOXO
54: XOXXOXOO
55: XOXXXOOO
56: XXOOOOXX
57: XXOOOXOX
58: XXOOOXXO
59: XXOOXOOX
60: XXOOXOXO  
61: XXOOXXOO
62: XXOXOOOX
63: XXOXOOXO
64: XXOXOXOO
65: XXOXXOOO
66: XXXOOOOX
67: XXXOOOXO
68: XXXOOXOO
69: XXXOXOOO
70: XXXXOOOO

## Question 2
##### Consider the raw data of men’s heights of Example 2.5 on page 27.

a. The mean is **69.148** and the standard deviation is **2.587**

b. Compare the raw data to the three common rules.
The data seems to follow a bell shape distribution. 
68% of the data falls within 1 standard deviation. 
$ 69.148 \pm 2.587 => [66.561, 71.735]$ 
95% of the data falls within 2 stand deviations. 
$ 69.148 \pm 2(2.587) => [63.974, 74.322]$ 
And 99.7% of the data falls within 3 standard deviations. 
$ 69.148 \pm 3(2.587) => [61.387, 76.909]$

c. If one of the men were to be randomly selected and you had to estimate his height, your best guess would be **69.148** inches; your estimate would differ from his actual height by approximately **2.587** inches or so.

d. Compute the estimated standard error.

$$
SE = \frac{s}{\sqrt{n}} = \frac{2.587}{\sqrt{33}} \approx \frac{2.587}{\sqrt{5.744}} \approx 0.4504
$$
Where $s$ is the sample standard deviation and $n$ is the sample size
e. The population mean μ is approximately **69.148** give or take **0.4504** or so.

## Question 3
If a fair die is rolled three times, find the probabilities of the following events:

a. All of the rolls show an even number of dots.
There are 3 even numbers so the chance of rolling an even number once is 3/6 = 1/2. Since we are looking at all three rolls and they are independent of each other, we can multiply the chances all together. 
$ P(\text{all rolls even}) = (\frac{1}{2})^3 = \frac{1}{8}$

b. The last two rolls show an even number of dots.
Using the previous logic the probability for the last 2 rolls are just multiplied together to get
$ \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} $
And since the first roll doesn't matter, it stays as 1/4.

c. The third roll shows an even number of dots.
Only the last roll matters
$ P(\text{last roll even}) = \frac{1}{2} $

d. Every roll shows a single dot.
The probability of rolling a single dot, aka a 1, is 1/6. And since they are all independent we can mutiply all 3 rolls together.
$ P(\text{all single dot}) = (\frac{1}{6})^3 = \frac{1}{216} $

e. Every roll shows the same number of dots.
Since they all have to match and are being rolled one at a time, the means that the first die can be anything. Since it can be anything, it won't effect the probability. So, we can just say that the last two rolls will have a 1/6 chance of matching the first roll, whatever it may be. We can notate it like this
$ P(\text{all rolls match}) = (\frac{1}{6})^2 = \frac{1}{36}$