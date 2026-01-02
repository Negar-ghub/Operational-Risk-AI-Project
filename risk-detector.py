# risk_detector.py - Detecting Anomalies for Operational Risk

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Create a synthetic dataset (Simulated 'normal' data points)
rng = np.random.RandomState(42)
X_normal = 0.3 * rng.randn(100, 2)
X_train = np.r_[X_normal + 2, X_normal - 2] 

# 2. Inject 'anomalies' (Outliers simulating operational risks)
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
X_combined = np.r_[X_train, X_outliers] 

# 3. Initialize and Fit the Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_combined)

# 4. Predict and Label Anomalies
predictions = model.predict(X_combined)

# 5. Output the results
print("Total data points processed:", len(X_combined))
print("Number of detected operational risks (anomalies):", list(predictions).count(-1))

# Optionally: Visualize the results (if you run the code)
plt.figure(figsize=(8, 6))
plt.scatter(X_combined[:, 0], X_combined[:, 1], c=predictions, cmap=plt.cm.coolwarm) 
plt.title("Isolation Forest: Operational Risk Detection")
plt.show()
