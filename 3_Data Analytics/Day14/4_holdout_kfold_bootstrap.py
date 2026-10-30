# How reliable is one accuracy number? Hold-out split vs k-fold cross validation vs bootstrapping
# (Slides: Resampling Problem, Bootstrapping vs K-Fold Cross Validation)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, LeaveOneOut, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('titanic.csv')
df['age'] = df['age'].fillna(df['age'].median())
df['is_female'] = (df['gender'] == 'female').astype(int)
X = df[['pclass', 'is_female', 'age', 'sibsp', 'parch', 'fare']]
y = df['survived']

def new_model():
    return make_pipeline(StandardScaler(), LogisticRegression())

# ------------------------------------------------------------
# 1) One hold-out split: the result depends on WHICH rows land in the test set
# ------------------------------------------------------------
scores = []
for seed in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    scores.append(new_model().fit(X_train, y_train).score(X_test, y_test))
print(f"20 different hold-out splits: accuracy from {min(scores):.3f} to {max(scores):.3f}")

# ------------------------------------------------------------
# 2) k-fold cross validation: every row is used for testing exactly once
# ------------------------------------------------------------
# Split into k = 5 folds; train on 4, test on the 5th; repeat 5 times; average
kf = KFold(n_splits=5, shuffle=True, random_state=1)
for i, (train_idx, test_idx) in enumerate(kf.split(X)):
    print(f"fold {i + 1}: train rows {len(train_idx)}, test rows {len(test_idx)}")
cv_scores = cross_val_score(new_model(), X, y, cv=kf, scoring='accuracy')
print("Accuracy per fold:", cv_scores.round(3))
print(f"Mean k-fold accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# Leave-one-out: k = number of rows (each test set is ONE passenger) - thorough but slow
small = X.sample(150, random_state=0)
loo_scores = cross_val_score(new_model(), small, y.loc[small.index], cv=LeaveOneOut())
print(f"Leave-one-out on 150 rows: {len(loo_scores)} models, accuracy {loo_scores.mean():.3f}")

# ------------------------------------------------------------
# 3) Bootstrapping: sample rows WITH replacement; test on the rows never picked (out-of-bag)
# ------------------------------------------------------------
rng = np.random.default_rng(0)
boot_scores = []
n = len(X)
for _ in range(100):
    idx = rng.integers(0, n, n)                          # n rows with replacement (some twice, some never)
    oob = np.setdiff1d(np.arange(n), idx)                # about 37% of rows are never picked
    model = new_model().fit(X.iloc[idx], y.iloc[idx])
    boot_scores.append(model.score(X.iloc[oob], y.iloc[oob]))
low, high = np.percentile(boot_scores, [2.5, 97.5])
print(f"Bootstrap (100 rounds): mean accuracy {np.mean(boot_scores):.3f}, 95% range {low:.3f} to {high:.3f}")

plt.hist(boot_scores, bins=20, alpha=0.6, label='Bootstrap (out-of-bag)')
plt.hist(scores, bins=10, alpha=0.6, label='Different hold-out splits')
plt.axvline(cv_scores.mean(), color='red', label='5-fold CV mean')
plt.xlabel('Accuracy')
plt.legend()
plt.title('One split gives one number; resampling shows the spread')
plt.show()

# Summary
#   Hold-out   : fast, but one lucky/unlucky split can mislead
#   k-fold     : every row tested once, no overlap between test folds; standard choice
#   Bootstrap  : sampling with replacement; gives a distribution (uncertainty) of the score
