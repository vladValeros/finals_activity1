import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Load data
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
df.columns = df.columns.str.strip()

# Drop rows with missing values
df = df.dropna()

# Separate features and target BEFORE encoding
X = df.drop(columns=['Sleep Disorder'])
y = df['Sleep Disorder']

# Encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

dump(model, 'sleep_model.joblib')
print("Model trained and saved as sleep_model.joblib")
