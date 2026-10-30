import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 1. Load and prepare data
df = pd.read_csv('titanic.csv').dropna(subset=['age', 'pclass', 'fare'])
X = df[['age', 'pclass', 'fare']]
y = df['survived']

# 2. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# 3. Apply Random Over-Sampling (Non-SMOTE) to the training set only
ros = RandomOverSampler(random_state=42)
X_train_res, y_train_res = ros.fit_resample(X_train, y_train)

# 4. Train model on oversampled training data and evaluate on the test set
model = LogisticRegression(max_iter=1000)
model.fit(X_train_res, y_train_res)

print("Classification Report (With Random Non-SMOTE Oversampling):")
print(classification_report(y_test, model.predict(X_test), digits=3))