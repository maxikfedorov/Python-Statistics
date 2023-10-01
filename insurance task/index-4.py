import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")

bmi_mean = data["bmi"].mean()
bmi_median = data["bmi"].median()
bmi_std = data["bmi"].std()

charges_mean = data["charges"].mean()
charges_median = data["charges"].median()
charges_std = data["charges"].std()

print("BMI:")
print("Mean =", bmi_mean)
print("Median =", bmi_median)
print("Standard deviation =", bmi_std)

print("\nCharges:")
print("Mean =", charges_mean)
print("Median =", charges_median)
print("Standard deviation =", charges_std)

plt.hist(data["bmi"], bins=30, alpha=0.5, color="blue")
plt.axvline(bmi_mean, color="red", linestyle="dashed", linewidth=2)
plt.axvline(bmi_median, color="green", linestyle="dashed", linewidth=2)
plt.axvline(bmi_mean + bmi_std, color="black", linestyle="dashed", linewidth=2)
plt.legend(["Mean", "Median", "Standard deviation"])
plt.title("BMI")
plt.show()

plt.hist(data["charges"], bins=30, alpha=0.5, color="blue")
plt.axvline(charges_mean, color="red", linestyle="dashed", linewidth=2)
plt.axvline(charges_median, color="green", linestyle="dashed", linewidth=2)
plt.axvline(charges_mean + charges_std, color="black", linestyle="dashed", linewidth=2)
plt.legend(["Mean", "Median", "Standard deviation"])
plt.title("Charges")
plt.show()
