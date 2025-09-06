✈️ Airline Passenger Satisfaction Analysis
📌 Project Overview
This project analyzes an airline passenger satisfaction dataset to uncover the key factors influencing customer satisfaction. Using data cleaning, exploratory data analysis (EDA), and visualizations, we highlight the service aspects that drive passenger happiness and identify areas for improvement.

📂 Dataset Details
File: airline_passenger_satisfaction.csv

Size: ~130,000 rows

Columns: Passenger demographics, travel details, service ratings, delays, and satisfaction label

Example Features:

Demographics: Gender, Age, Customer Type

Travel Details: Type of Travel, Class, Flight Distance

Service Ratings: In-flight Wifi, Seat Comfort, Cleanliness, etc.

Operational Data: Departure Delay, Arrival Delay

Target Variable: Satisfaction (Satisfied / Neutral or Dissatisfied)

🛠 Data Cleaning
Handled missing values:

Filled missing Arrival Delay with 0 and converted to integer.

Fixed data types:

Converted categorical features (Gender, Class, Satisfaction) into category type.

Removed duplicates for consistency.

📊 Exploratory Data Analysis (EDA)
🔹 Univariate Analysis
Satisfaction distribution: Majority are Neutral or Dissatisfied.

Age distribution: Most passengers are between 20–50 years old.

🔹 Bivariate Analysis
Gender vs Satisfaction: No significant difference.

Class vs Satisfaction: Business class passengers are much more satisfied.

Wifi vs Satisfaction: Better wifi ratings strongly increase satisfaction.

Delays vs Satisfaction: Longer delays → lower satisfaction.

Customer Type vs Satisfaction: Loyal customers report more satisfaction.

🔹 Grouped Insights
Satisfied passengers tend to fly longer distances.

Business class → ~70% satisfied.

Economy class → only ~19% satisfied.

🔹 Correlation Heatmap
Strongest correlations: Seat Comfort, Wifi, Cleanliness with satisfaction.

Weak correlations: Age, Gender.

📈 Key Insights
Service-related factors (comfort, wifi, cleanliness) are the strongest drivers of satisfaction.

Operational performance (delays) negatively impacts customer experience.

Demographics (age, gender) have minimal effect on how satisfied passengers are.

Business and loyal customers are significantly more satisfied on average.

🛎️ Future Work
Build predictive models to classify passenger satisfaction.

Perform feature importance analysis using machine learning.

Create interactive dashboards for airline decision-making.

📌 Tech Stack
Python (Pandas, NumPy, Matplotlib, Seaborn)

Jupyter Notebook for analysis

Scikit-learn (planned for predictive modeling)

