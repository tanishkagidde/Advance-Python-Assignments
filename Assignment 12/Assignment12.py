# Customer Churn Dataset - Exploratory Data Analysis (EDA)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------
df = pd.read_csv("customer_churn.csv")
print("First 5 records:")
print(df.head())

# --------------------------------------------------
# 2. Basic information about the dataset
# --------------------------------------------------
print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

# --------------------------------------------------
# 3. Check missing values
# --------------------------------------------------
print("\nMissing values in each column:")
print(df.isnull().sum())

# --------------------------------------------------
# 4. Remove duplicate records
# --------------------------------------------------
print("\nNumber of duplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

# --------------------------------------------------
# 5. Handle missing values
# --------------------------------------------------
# Fill missing numerical values with mean
numeric_columns = df.select_dtypes(include=np.number).columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Summary statistics
# --------------------------------------------------
print("\nSummary Statistics:")
print(df.describe())

# --------------------------------------------------
# 7. Find average monthly charges
# --------------------------------------------------
print("\nAverage Monthly Charges:")
print(np.mean(df["MonthlyCharges"]))

# --------------------------------------------------
# 8. Find average customer tenure
# --------------------------------------------------
print("\nAverage Customer Tenure:")
print(np.mean(df["Tenure"]))

# --------------------------------------------------
# 9. Count customers who churned
# --------------------------------------------------
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

# --------------------------------------------------
# 10. Churn percentage
# --------------------------------------------------
churn_percentage = df["Churn"].value_counts(normalize=True) * 100
print("\nChurn Percentage:")
print(churn_percentage)

# --------------------------------------------------
# 11. Visualization - Churn Count
# --------------------------------------------------
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 12. Visualization - Monthly Charges
# --------------------------------------------------
plt.hist(df["MonthlyCharges"], bins=10)
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 13. Visualization - Tenure
# --------------------------------------------------
plt.hist(df["Tenure"], bins=10)
plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 14. Churn based on Contract
# --------------------------------------------------
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
print("\nChurn based on Contract:")
print(contract_churn)

contract_churn.plot(kind="bar")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

# --------------------------------------------------
# 15. Average Monthly Charges for Churned and Non-Churned Customers
# --------------------------------------------------
average_charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("\nAverage Monthly Charges by Churn:")
print(average_charges)

average_charges.plot(kind="bar")
plt.title("Average Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.show()

# --------------------------------------------------
# 16. Correlation between numerical variables
# --------------------------------------------------
correlation = df[numeric_columns].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Matrix")
plt.show()

'''
OUTPUT :

First 5 records:
  CustomerID  Gender   Age  Tenure  MonthlyCharges  TotalCharges        Contract InternetService Churn
0    CUST001    Male  35.0      32           60.45       1902.06  Month-to-month     Fiber optic    No
1    CUST002  Female  43.0      71          108.78       7557.37        Two year             DSL   Yes
2    CUST003    Male  61.0      59          105.09       6373.08  Month-to-month     Fiber optic    No
3    CUST004    Male  51.0      28          113.56       3030.42  Month-to-month     Fiber optic   Yes
4    CUST005    Male  27.0      66           98.53       6438.35        One year     Fiber optic    No

Shape of dataset:
(102, 9)

Column names:
Index(['CustomerID', 'Gender', 'Age', 'Tenure', 'MonthlyCharges',
       'TotalCharges', 'Contract', 'InternetService', 'Churn'],
      dtype='str')

Dataset information:
<class 'pandas.DataFrame'>
RangeIndex: 102 entries, 0 to 101
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   CustomerID       102 non-null    str    
 1   Gender           102 non-null    str    
 2   Age              101 non-null    float64
 3   Tenure           102 non-null    int64  
 4   MonthlyCharges   100 non-null    float64
 5   TotalCharges     102 non-null    float64
 6   Contract         102 non-null    str    
 7   InternetService  100 non-null    str    
 8   Churn            102 non-null    str    
dtypes: float64(3), int64(1), str(5)
memory usage: 7.3 KB
None

Missing values in each column:
CustomerID         0
Gender             0
Age                1
Tenure             0
MonthlyCharges     2
TotalCharges       0
Contract           0
InternetService    2
Churn              0
dtype: int64

Number of duplicate records:
2

Missing values after cleaning:
CustomerID         0
Gender             0
Age                0
Tenure             0
MonthlyCharges     0
TotalCharges       0
Contract           0
InternetService    0
Churn              0
dtype: int64

Summary Statistics:
              Age      Tenure  MonthlyCharges  TotalCharges
count  100.000000  100.000000      100.000000    100.000000
mean    43.939394   36.610000       70.256939   2622.314900
std     14.410867   22.585816       28.791512   2159.684502
min     18.000000    1.000000       20.520000      0.000000
25%     31.750000   19.000000       48.282500    920.927500
50%     43.969697   37.000000       68.615000   2260.040000
75%     56.000000   57.250000       94.507500   3508.445000
max     70.000000   72.000000      119.460000   8175.240000

Average Monthly Charges:
70.25693877551019

Average Customer Tenure:
36.61

Customer Churn Count:
Churn
No     60
Yes    40
Name: count, dtype: int64

Churn Percentage:
Churn
No     60.0
Yes    40.0
Name: proportion, dtype: float64
'''
