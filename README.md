# Dat4-BI-MP3

## Mini Project 3: Machine Learning for Prediction by Regression

### Group:

- Lasse - Github: **[kotteletfisk](https://github.com/kotteletfisk)**
- Oskar - Github: **[cph-oo221](https://github.com/cph-oo221)**

## Project Description

This project is the thrid mini project with focus on machine learning for prediction by regression. In this task we are using data (.csv) from property market in King County, USA. The primary goal is to training a regression model that can predict the prices of properties.

## Project Content

#### **1. [MP3 - Solution (ipynb)](./MP3%20-%20machine%20learning%20by%20regression.ipynb)**

#### **2. [Questions / Answers](#questions)**

#### **3. [util folder (python files)](./util)**

#### **4. [Data folder (csv files)](./data)**

#### **5. [Stored model (pkl files)](./deploy)**

## Questions

- **What type/s of regression have you applied?**

  - Linear
  - Multiple linear
  - Multiple Linear with polynomial features
  - Linear trained with principal components

- **Which were the challenges?**

  A challenging task was to clean the data sufficiently to make the patterns in the data the most reliable.
  We spent a lot of time, trying to reduce noise in the dataset, by reducing the amount of features. We had different appraoches to this by first trying to
  identify the most correlating features and focusing on them. When that didn't help the models accuracy, we tried condensing the X matrix features into principal components.
  Both solutions ended up not working well, and we ended up going with the first model.

- **How accurate is your solution?**

  After applying the three regression models: Linear, Multiple linear & Polynomial, can we conclude that the best result when trying these models are
  Multiple linear regression (containing all slightly relevant features) with a $r^2$ of 55%.

- **What could be done for further improvement of the accuracy?**
- 
  After trying to condense the data we had with no luck, we think what would help the model most could be a more strict cleansing of the dataset.
  for example, by having a lower tolerance to outliers.
