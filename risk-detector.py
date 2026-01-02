# risk_detector.py - Detecting Anomalies for Operational Risk

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Create a synthetic dataset
rng = np.random.RandomState(42)
X_normal = 0.3 * rng.randn(100, 2)
X_train = np.r_[X_normal + 2, X_normal - 2]

# 2. Inject 'anomalies'
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
X_combined = np.r_[X_train, X_outliers]

# 3. Initialize and Fit the Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_combined)

# 4. Predict and Label Anomalies
predictions = model.predict(X_combined)

# 5. Save the results to 'results.txt' file
n_samples = len(X_combined) 
n_anomalies = list(predictions).count(-1) 

results_summary = f"""Total data points processed: {n_samples}
Number of detected operational risks (anomalies): {n_anomalies}"""

with open("results.txt", "w") as f:
    f.write(results_summary)

print("Results successfully saved to results.txt file.")

# Optionally: Visualize the results
plt.figure(figsize=(8, 6))
plt.scatter(X_combined[:, 0], X_combined[:, 1], c=predictions, cmap=plt.cm.coolwarm)
plt.title("Isolation Forest: Operational Risk Detection")
plt.show()
