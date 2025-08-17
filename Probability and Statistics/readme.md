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