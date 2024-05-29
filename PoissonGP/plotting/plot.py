import numpy as np
import matplotlib.pyplot as plt

def plot_predictions(x, y, mean, variance, confidence=1.96):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'kx', mew=2, label='Observed data')
    plt.plot(x, np.exp(mean), 'b', lw=2, label='Predictive mean')
    plt.fill_between(x.flatten(), np.exp(mean - confidence * np.sqrt(variance)).flatten(),
                     np.exp(mean + confidence * np.sqrt(variance)).flatten(), color='blue', alpha=0.2,
                     label=f'{int(100 * confidence)}% confidence interval')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Gaussian Process Predictions with Poisson Likelihood')
    plt.show()

# Example Usage:
#from my_package.plotting import plot_predictions
# mean, variance = model.predict(X_new)
# plot_predictions(X_new, np.exp(mean), variance)
