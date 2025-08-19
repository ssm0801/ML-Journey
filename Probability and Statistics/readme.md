## Statistics

It is a field that deals with collection, organization, analysis, interpretation and presentation of data

Goal : Understand the data and make decision

## Types of Statistics

1. Descriptive
   - It consists of organizing and summaring of data
   - Measure of Central Tendency
     - Mean
     - Median
     - Mode
   - Measure of Dispersion
     - Variance
     - Standard Deviation
2. Inferential
   - Conclusion or Inferences of other data (population data) from collected data (sample data) by using some experiments like z test, t test, etc.

## Population vs Sample Data

- Population
  - Notation : N
  - Total dataset you have
- Sample
  - Notation : n
  - Smaller portion of that dataset

## Measure of Central Tendency

- Mean
  - Simple average
  - Population Mean (μ) = Sum of all numbers / N
  - Sample Mean (x̄) = Sum of numbers in sample / n
  - Outliers can affect a Mean a lot
- Median
  - Find near to avg, helps to fight outlier
  - First sort the numbers
  - If odd numbers then Median = middle number
  - If even numbers then Median = middle two numbers / 2
- Mode
  - Helps to fight against outlier
  - We select the element which has maximum frequency as Mode

## Measure of Dispersion

Factor to distinguish the distributions when their Mean is same based on spread. Spread ∝ Variance

- Variance
  - Gives you the spread / dispersion
  - Population Variance (σ²) = (∑ (xᵢ - μ)^2) / N
  - Sample Variance (s²) = (∑ (xᵢ - x̄)^2) / (n - 1)
  - Why n-1 in Sample Variance ?
  - When we take denominator as only n, it will underestimate the true population variance
  - So n-1, also it is called as Bessel's Correction
- Standard Deviation
  - Tells how far a data point is away from mean
  - Population Standard Deviation (σ) = Square root of Population Variance
  - Sample Standard Deviation (s) = Square root of Sample Variance

## Variable and Types

Property that can take up any value

- Quantitative variables
  - Discrete quantitative variables : integer values
  - Continuous quantitative variables : decimal values
- Qualitative / Categorical variables : fixed number of values

## Random variables

Function whose values are derived from different process or experiments. Notation (X)

- Discrete Random Variables
  - Int or Categorical values
  - Example : Tossing a coin, Rolling a dice
- Continuous Random Variables
  - Decimal values
  - Example : Tomorrow how many inches of rain going to happen

## Histogram

- Define number of bins
- Each bar defines number of elements in each bin
- Probability Density Function PDF (line graph) which is smootheing the histogram using Kernal Density Estimation

## Percentiles and Quartiles

- Percentage
  - Number or ratio expressed out of 100
  - (Value/Total) \* 100
- Percentile
  - It says how many percentage of distribution is less than x
  - (No. of values below x / n) \* 100
  - Value = (p Percentile/100) \* (n+1)
  - If value is not present then take average of (floor(value) + ceil(value)) / 2
  - This says that p percentage of entire distribution is less than value
- Quartile
  - Distributon must be sorted
  - position = (p Percentile/100) \* (n+1)
  - 25% percentile = 1st Quartile
  - 50% percentile = 2nd Quartile
  - 75% percentile = 3rd Quartile

## 5 Number Summary

Used to draw Box plot

- Minimum
- 1st Quartile (25% Percentile) : Q1
- Median
- 3rd Quartile (75% Percentile) : Q3
- Maximum

## Step to remove outliers

- Define lower fence and higher fence
- Calcualte Inter Quartile Range (IQR) = Q3 - Q1
- lower fence = Q1 - (1.5 \* IQR)
- higher fence = Q3 + (1.5 \* IQR)
- Anything less than lower fence and higher than higher fence are outlier, so can be removed

## Covariance and Correlation

- Two statistical measures used to determine relationship between two variables. Both are used to understand how changes in one variable is associated with changes in another variable
- Covariance
  - It measures how much two random variables change together
  - If variables tend to increase or decrease together, then covariance is positive
  - If one tends to increase when the other decreases, then covariance is negative
  - Covariance(x,y) = (∑ (xᵢ - x̄)(yᵢ - ȳ)) / (n - 1)
  - Covariance(x,x) = (∑ (xᵢ - x̄)^2) / (n - 1) = Variance(x)
  - Pros
    - Quantify the relationship between x and y
  - Cons
    - Covariance doesn't have specific limit values
    - It can range from -∞ to ∞
- Correlation
  - Pearson Correlation Coefficient
    - It limits the values between -1 to 1
    - ρ(x,y) = Cov(x,y) / σ(x).σ(y)
    - The more the value towards +1 the more +ve correlated x and y are, vice versa
    - Cons : Wont be able to capture correlation properly for non linear data
  - Spearman Rank Correlation
    - rₛ = Cov(R(x),R(y)) / σ(R(x)).σ(R(y))

## Probability

It is about determining the likelihood of an event.
Probability = Chance

Probability of event = (Number of favorable outcomes) / (Total number of possible outcomes)

## Mutual Exclusive Event

Two events are mutual exclusive if they can not occur at same time.
E.g. Toss a coin - cant get H and T at same time

P(A or B) = P(A) + P(B)

i.e Additive Rule for Mutual Exclusive Event

## Non Mutual Exclusive Event

Two events are non mutual exclusive if they can occur at same time.
E.g. Drawing card from deck - you can get king or heart - possible to get both in form of king of hearts

P(A or B) = P(A) + P(B) - P(A and B)

i.e Additive Rule for Non Mutual Exclusive Event

## Independent Event

Two events are independent if they do not affect one another
E.g. Toss a coin - first toss result wont afect the probability of second result

P(A and B) = P(A) * P(B)

i.e Multiplication Rule for Independent Event

## Dependent Event

Two events are dependent if and only if they affect each other
E.g. Take a king card from deck and then quen card from the deck - After drawing kind card it will affect the probability of drawing the quen card

P(A and B) = P(A) * P(B/A)

i.e Multiplication Rule for Dependent Event

Also called as Conditional Probability

## Probability Distribution Functions

It descrives how probabilities are distributed over values of random variable

- Probability Mass Function (PMF)
- Cumulative Distribution Function (CDF)
- Probability Density Function (PDF)

## Probability Mass Function

PMF give probability of each value in distribution.

E.g. Rolling a dice
X-axis = 1,2,3,4,5,6
Y-axis = 1/6, 2/6, 3/6, 4/6, 5/6, 6/6
So for all values its always 1/6

## Cumulative Density Function

Whereas CDF is cumulative (combine) of all probabilities till that point

E.g. Rolling a dice
X-axis = 1,2,3,4,5,6
Y-axis = 1/6, 2/6, 3/6, 4/6, 5/6, 6/6
Here P(x<3) = P(1) + P(2) + P(3)

For
x=1, y=1/6
x=2, y=2/6
and so on...

## Probability Density Function

From CDF, probability density (gradien/slope) of each point is calculated, and plotted on other graph as y-axis that is nothing but PDF

PDF = Gradient of CDF

E.g. Distrbution of ages
So P(x<=40) = Area under the curve of PDF for x in [0,40]

Properties:
- Non negativity f(x)>=0 for all x
- Total aread under PDF curve is 1
  ∫ of -∞ to ∞ f(x).dx = 1
- f(x) will change based on different distribution types