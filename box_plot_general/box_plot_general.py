# 5.1
# This program creates a box plot comparing the average reading times of the original and nonce sentences.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
original_reading_speed = [
    611.25, 594.74, 514.53, 732.01, 674.95, 652.36, 592.55, 541.29, 734.56, 736.82, 613.16, 1207.47, 504.14, 591.32,
    678.25, 644.61, 672.06, 629.63, 264.80, 673.55, 515.83, 549.09, 645.56, 752.47, 536.15, 421.55, 675.70]


nonce_reading_speed = [
    678.64, 816.71, 920.67, 873.89, 742.04, 631.67, 731.38, 898.63, 610.29, 713.94, 1365.18, 682.30, 596.05, 771.14,
    630.21, 765.65, 747.91, 575.20, 823.43, 829.00, 693.62, 976.18, 962.12, 655.40, 242.64, 938.31, 229.50,
    729.80, 704.23, 715.46, 666.72, 1318.49]  # 4613.00: we took this value out because it was an outlier

# Creating DataFrame
data = {
    'Sentence Type': ['Original'] * len(original_reading_speed) + ['Nonce'] * len(nonce_reading_speed),
    'ms/word': original_reading_speed + nonce_reading_speed
}

df = pd.DataFrame(data)

# Creating the box plot
plt.figure(figsize=(10, 10))
sns.boxplot(x='Sentence Type', y='ms/word', hue='Sentence Type', legend=False, data=df, width=0.6, palette='Set1')
plt.xticks([0, 1], ['Original', 'Nonce'])
plt.title('Reading Times: Original vs Nonce Sentences')
plt.xlabel('Sentence Type')
plt.ylabel('Average reading speed (ms/word)')
# plt.show()
plt.savefig('box_plot_general.png', dpi=800)


nonce_reading_speed = [
    678.64, 816.71, 920.67, 873.89, 742.04, 631.67, 731.38, 898.63, 610.29, 713.94, 1365.18, 682.30, 596.05, 771.14,
    630.21, 765.65, 747.91, 575.20, 823.43, 829.00, 693.62, 976.18, 962.12, 655.40, 242.64, 938.31, 229.50,
    729.80, 704.23, 715.46, 666.72, 1318.49, 4613.00]

# Calculate average reading speed for each sentence type
original_avg = sum(original_reading_speed) / len(original_reading_speed)
nonce_avg = sum(nonce_reading_speed) / len(nonce_reading_speed)
print('Original average reading speed: ', original_avg)
print('Nonce average reading speed: ', nonce_avg)
