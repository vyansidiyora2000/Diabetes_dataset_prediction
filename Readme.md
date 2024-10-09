# Diabetes Dataset Analysis

## Overview

This project focuses on performing **Exploratory Data Analysis (EDA)** on the **Pima Indians Diabetes Database**, a dataset that contains health-related information used to predict whether a person has diabetes. The aim is to better understand the relationships between various health metrics and diabetes, identify trends, and lay the foundation for predictive modeling.

Diabetes is a chronic condition that affects millions of people worldwide. Proper data analysis can reveal valuable insights, helping to inform healthcare decisions and highlight areas for further research.

## Dataset Description

The dataset contains 768 entries and 9 features. Each entry represents data collected from a female patient of Pima Indian heritage, aged 21 years or older. The dataset's target variable is **Outcome**, which indicates whether the patient has diabetes (1) or not (0).

### Features:
- **Pregnancies**: Number of times the patient has been pregnant.
- **Glucose**: Plasma glucose concentration after a 2-hour oral glucose tolerance test.
- **BloodPressure**: Diastolic blood pressure (mm Hg).
- **SkinThickness**: Triceps skinfold thickness (mm).
- **Insulin**: 2-Hour serum insulin (mu U/ml).
- **BMI**: Body mass index (weight in kg/(height in m)^2).
- **DiabetesPedigreeFunction**: A function that represents a patient's likelihood of diabetes based on family history.
- **Age**: Patient’s age in years.
- **Outcome**: The class label (0 for non-diabetic, 1 for diabetic).

### Dataset Summary:
- **Number of rows**: 768
- **Number of columns**: 9
- **Class balance**: 268 diabetic (1), 500 non-diabetic (0)

This dataset is crucial because it provides real-world health data that can be used for various forms of analysis, including machine learning models to predict the onset of diabetes.

## Objectives

The primary objectives of this project are:
1. **Data Loading and Exploration**: Understand the structure, characteristics, and summary statistics of the dataset.
2. **Data Cleaning**: Check for missing values, inconsistencies, and outliers, and handle them appropriately.
3. **Feature Analysis**: Explore individual features, such as blood pressure, glucose levels, and BMI, to understand how they relate to diabetes.
4. **Correlation Analysis**: Identify relationships between the features and determine which factors have the most influence on the outcome.
5. **Outcome Distribution**: Analyze the distribution of diabetic vs. non-diabetic patients in the dataset.
6. **Future Work**: Set the groundwork for predictive modeling, which could involve machine learning techniques like logistic regression, decision trees, or neural networks.

## Step-by-Step Breakdown

### 1. **Loading the Dataset**
The dataset is loaded using `pandas`, a powerful data manipulation library in Python. This step involves importing the dataset from a CSV file and displaying the first few rows to get an overview of its structure.

```python
import pandas as pd
d_diabetes = pd.read_csv('path_to_your_diabetes_dataset.csv')
print(d_diabetes.head())
```
### 2. Exploratory Data Analysis (EDA)

EDA is performed to understand the data distribution and identify potential patterns. For instance:

- **Row and Column Count**: Understanding the size of the dataset is crucial for further steps.
- **Data Types**: Ensuring all features have appropriate data types (e.g., numeric for quantitative features).
- **Outcome Analysis**: Analyzing the target variable, which in this case is whether or not the patient has diabetes.

```python
print(f"Dataset Dimensions: {d_diabetes.shape}")
print(f"Outcome Distribution:\n{d_diabetes['Outcome'].value_counts()}")
```

![Correlation Heatmap](https://github.com/vyansidiyora2000/Diabetes_dataset_prediction/blob/main/Assests/correlation.png)

### Count Plot
This is the count plot for age, glucose levels, and other key features:

![Count Plot](https://github.com/vyansidiyora2000/Diabetes_dataset_prediction/blob/main/Assests/Screenshot%202024-10-09%20141830.png)

## Dashboard
The dashboard generated from the analysis:

![Dashboard](relative/path/to/dashboard.png)
### 3. Feature Exploration

Each feature is analyzed for its distribution, spread, and possible impact on diabetes prediction. This analysis may involve:

- **Glucose Levels**: Observing trends in glucose levels for diabetic vs. non-diabetic patients.
- **BMI**: Analyzing the relationship between BMI and diabetes risk.
- **Insulin Levels**: Investigating how insulin levels vary between diabetic and non-diabetic individuals.

To explore these relationships, we will use various visualizations such as:

- **Histograms**: To observe the distribution of each feature.
- **Box Plots**: To analyze the spread and outliers for each feature.
- **Scatter Plots**: To investigate possible correlations between pairs of features (e.g., glucose vs. insulin).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Example for Glucose levels
sns.histplot(d_diabetes['Glucose'], kde=True, hue=d_diabetes['Outcome'])
plt.title('Glucose Levels Distribution for Diabetic vs. Non-Diabetic')
plt.show()

```
### 4. Model Accuracy
Once the features have been explored and analyzed, the next step would involve applying machine learning models for predicting diabetes. The models could include:

The Accuracy is: 0.7597402597402597

## YouTube Explanation Link:


For a detailed walkthrough of this project, including feature exploration, model implementation, and accuracy evaluation, you can watch the full YouTube video [here](https://www.youtube.com/watch?v=27svmiPkbeY&t=72s). The video provides an in-depth guide to each step of the analysis and predictive modeling.
