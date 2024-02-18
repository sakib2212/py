import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Choose an appropriate backend
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data
X = np.array([99, 85, 86, 71, 82, 95, 108, 87, 89, 89, 78, 86])

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Create a boxplot using Seaborn
sns.boxplot(x=X, orient="v", width=0.2, palette="Set2", ax=axes[0])
axes[0].set_title('Boxplot')

# Display the probability plot
stats.probplot(X, plot=axes[1])
axes[1].set_title('Probability Plot')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()





