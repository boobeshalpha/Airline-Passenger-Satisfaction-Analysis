✈️ Airline Passenger Satisfaction Analysis
📌 Project Overview

This project analyzes an airline passenger satisfaction dataset to identify key factors that influence customer satisfaction.
We perform data cleaning, exploratory data analysis (EDA), and visualization to uncover insights.

📂 Dataset Details

File: airline_passenger_satisfaction.csv

Rows: ~130,000

Columns: Passenger demographics, travel details, service ratings, delays, and satisfaction label.

Example Columns:

Gender – Male/Female

Age – Passenger age

Customer Type – Loyal / Disloyal

Type of Travel – Business / Personal

Class – Business, Economy, Economy Plus

Flight Distance – Distance of flight

Departure Delay, Arrival Delay – Delay in minutes

In-flight Wifi Service, Seat Comfort, Cleanliness, etc.

Satisfaction – Target variable (Satisfied / Neutral or Dissatisfied)

🛠 Data Cleaning

Handled missing values

Filled missing Arrival Delay with 0.

Converted it to integer type.

Fixed data types

Converted categorical columns (e.g., Gender, Class, Satisfaction) to category.

Removed duplicates

Dropped duplicate rows for data consistency.

📊 Exploratory Data Analysis (EDA)
🔹 Univariate Analysis

Satisfaction Distribution:
Most passengers are Neutral or Dissatisfied.

Age Distribution:
Majority of passengers are between 20–50 years old.

🔹 Bivariate Analysis

Gender vs Satisfaction: No major difference between male and female satisfaction.

Class vs Satisfaction: Business class passengers are significantly more satisfied.

Wifi vs Satisfaction: Higher wifi ratings → more satisfaction.

Arrival Delay vs Satisfaction: Longer delays reduce satisfaction.

Customer Type vs Satisfaction: Loyal customers report more satisfaction.

🔹 Grouped Insights
print(df.groupby("Satisfaction")["Flight Distance"].mean())


Satisfied passengers fly longer distances.

print(df.groupby("Class")["Satisfaction"].value_counts(normalize=True))


Business class → ~70% satisfied

Economy → only ~19% satisfied

🔹 Correlation Heatmap

Strongest correlation: Service ratings (Seat Comfort, Wifi, Cleanliness) with satisfaction.

Weak correlation: Age, Gender.
