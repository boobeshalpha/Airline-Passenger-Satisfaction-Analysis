import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("Output", exist_ok=True)

# Load the dataset (use raw string for path)
df = pd.read_csv(r"C:\Users\keert\OneDrive\Desktop\airline_satisfication\airline_passenger_satisfaction.csv")

# Shape and basic info
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nColumns:", df.columns.tolist())
print("\nFirst 100 rows:")
print(df.head(100))
print("\nSummary Statistics:")
print(df.describe(include="all"))

print("=" * 80)
print("data cleaning")
print("=" * 80 )
 
 #check missing value
print("\nMissing values:\n", df.isnull().sum())
#drop nill values of arival delay
df['Arrival Delay'] = df['Arrival Delay'].fillna('0')
df['Arrival Delay'] = df['Arrival Delay'].astype(int)
#fix data types
for col in df.select_dtypes("object").columns:
    df[col] = df[col].astype("category")

#remove duplicates
df.drop_duplicates(inplace=True)

print(df.shape)
print(df.isnull().sum())
print(df.info())

print("=" * 80)     
print("feature engineering")
print("=" * 80)  
# Groupby examples
print(df.groupby("Satisfaction", observed=True)["Flight Distance"].mean())
print(df.groupby("Class", observed=True)["Satisfaction"].value_counts(normalize=True))


print('=' *80)
print("Exploratory Data Analysis")
print('=' *80)

#traget variable distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Satisfaction', hue='Satisfaction', palette='Set2')
plt.title('Distribution of Satisfaction')
plt.xlabel('Satisfaction')
plt.ylabel('Count')

# Make sure the folder exists
full_path = os.path.join("Output", "Satisfaction_distribution.png")
plt.savefig(full_path)
print(f"💾 Full figure saved at: {full_path}")

#hsitogram for age
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')

full_path = os.path.join("Output", "Age_distribution.png")
plt.savefig(full_path)   
print(f"💾 Full figure saved at: {full_path}")

# satisfiaction vs gender
plt.figure(figsize=(8, 6))
sns.countplot(x="Gender", hue="Satisfaction", data=df)
plt.title('Satisfaction')
plt.xlabel("gender")
plt.ylabel("satisfaction count")

full_path = os.path.join("output", "Satisfaction vs gender.png")
plt.savefig(full_path)
print(f"💾 Full figure saved at: {full_path}")

# Correlation Heatmap (numerical only)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

full_path = os.path.join("output", "heatmap.png")
plt.savefig("Output/correlation_heatmap.png")       
print(f"💾 Full figure saved at: {full_path}")

# Wifi vs Satisfaction
plt.figure(figsize=(10, 6))
sns.countplot(x="Satisfaction", hue="In-flight Wifi Service", data=df)
plt.title("Wifi Service vs Satisfaction")
plt.xlabel("Satisfaction")
plt.ylabel("Count")

fullpath=os.path.join("Output/wifi vs satisfaction.png")
plt.savefig(fullpath)
print(f"💾 Full figure saved at: {full_path}")

#class inpact
sns.countplot(x="Class", hue="Satisfaction", data=df)
plt.title("Inflight Wifi vs Satisfaction")
plt.xlabel("Satisfaction")
plt.ylabel("Class")
 
fullpath=os.path.join("output/Class vs satisfaction.png")
plt.savefig(fullpath)
print(f"💾 Full figure saved at: {full_path}")

#delay effect 
sns.barplot(x="Satisfaction", y="Arrival Delay", data=df)
plt.title("Arrival delay vs satisfaction")
plt.xlabel("Satisfication")
plt.ylabel("Arrival Delay")

fullpath=os.path.join("output/Arrival delay vs satisfaction.png")
plt.savefig(fullpath)
print(f"💾 Full figure saved at: {full_path}")

#loyalty
sns.countplot(x="Customer Type", hue="Satisfaction", data=df)
plt.title("loyalty of customer")
plt.xlabel("customer type")
plt.ylabel("Satisfaction")

fullpath=os.path.join("output/customer type vs  satisfaction.png")
plt.savefig(fullpath)
print(f"💾 Full figure saved at: {full_path}")