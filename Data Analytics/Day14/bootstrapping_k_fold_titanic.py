import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_val_predict
from sklearn.utils import resample
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = pd.read_csv('titanic.csv')

df = df[['survived', 'pclass', 'gender', 'age', 'sibsp', 'fare']].dropna()

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender']) 

X = df.drop('survived', axis=1)
y = df['survived']

# Bootstrapping
print("\n--- Bootstrapping Example ---")
n_iterations = 100  # Number of bootstrap samples (i.e., how many times to repeat)
n_size = int(len(X) * 0.80)  # Each bootstrap sample size (e.g., 80% of original data)
bootstrap_scores = []  # To store accuracy of each bootstrap iteration

for i in range(n_iterations):
    # Resample with replacement
    # Each sample may include repeated rows from the original dataset
    X_resample, y_resample = resample(X, y, n_samples=n_size, random_state=i)
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X_resample, y_resample, test_size=0.20, random_state=i)
    
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    bootstrap_scores.append(acc)

print(f'Average accuracy over {n_iterations} bootstrapped samples: {np.mean(bootstrap_scores):.3f}')

# K-Fold Cross-validation
print("\n--- K-Fold Cross-Validation ---")
# Default k fold: k-1 for training, 1 for test
kf = KFold(n_splits=5, shuffle=True, random_state=1) # 5 folds, default = 4 for training, 1 for test
# Use 40% data for test ... here we do not se the KFold class ... 
# kf = ShuffleSplit(n_splits=5, test_size=0.4, random_state=1) 
model = LogisticRegression(max_iter=500)


# Perform K-Fold CV
cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print(f'Accuracy scores for each fold: {cv_scores}')
print(f'Mean CV accuracy: {np.mean(cv_scores):.3f}')
