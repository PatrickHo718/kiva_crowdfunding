# Kiva Crowdfunding Income Group Prediction

## Project Overview

This project focuses on predicting the income group of borrowers and days to fund on the Kiva crowdfunding platform using machine learning. The goal is to analyze borrower profiles and loan features to classify borrowers into income categories, which can help in understanding financial accessibility and risk patterns.

The dataset used is from this site on here [Kiva Data Science for Good competition on Kaggle](https://www.kaggle.com/datasets/kiva/data-science-for-good-kiva-crowdfunding)

## Data

- Loan data from Kiva, including borrower information, loan amounts, funding speed, repayment intervals, and country's economic indicators like GDP per capita.
- The dataset was preprocessed to handle missing values, encode categorical variables, and balance classes for model training.

## Methodology

- Used Python and scikit-learn to build a Random Forest model to predict target variables.
- Features, including loan attributes and borrower demographics, are all properly encoded.
- Model evaluation was performed using precision, recall, F1-score, and confusion matrices to evaluate its performance.
- Studied funding time (`days_to_fund`) as a proxy for lender hesitation and perceived borrower risk.

## Key Findings

- The model predicts income groups with reasonable to moderate accuracy, highlighting distinctions between borrower segments.
- Lower-income groups tend to have longer funding times, suggesting barriers in access to capital and funding.
- Loan size and repayment intervals vary across predicted income groups, offering insights into borrower behavior.

## Usage

- The trained model can be applied to new loan data to predict income groups.
- Visualizations such as confusion matrices and boxplots aid in understanding model performance and borrower characteristics.

## Tools & Libraries

- Python (pandas, numpy, matplotlib, seaborn)
- scikit-learn (RandomForest, LabelEncoder)
- Joblib 
