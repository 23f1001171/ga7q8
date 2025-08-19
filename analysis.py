import matplotlib.pyplot as plt

# Calculate average CAC
avg_cac = df['cac'].mean()
print(f"Average CAC: {avg_cac:.2f}")

# Calculate required reduction
reduction_needed = (avg_cac - industry_target) / avg_cac * 100
print(f"Reduction needed to hit target: {reduction_needed:.1f}%")

# Plot
plt.figure(figsize=(6,4))
plt.plot(df['quarter'], df['cac'], marker='o', label='CAC')
plt.axhline(industry_target, linestyle='--', color='red', label='Industry Target')
plt.title('Customer Acquisition Cost (CAC) - 2024 Quarterly')
plt.xlabel('Quarter')
plt.ylabel('CAC')
plt.legend()
plt.tight_layout()
plt.savefig("cac_trend.png", dpi=200)
plt.show()
