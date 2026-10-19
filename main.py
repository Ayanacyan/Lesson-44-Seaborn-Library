import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
df=df.dropna()
print("First five rows")
print(df.head())

print()
print(df.info())
print()
print(df.describe())
print()
print("species:",df['species'].unique())
print("islands:",df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=20, color='steelblue')
plt.title('Distribution of penguin body mass')
plt.xlabel('Bodymass in grams')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length + Species')
plt.xlabel('FLipper Length')
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='coral')
plt.title('Flipper Length + Histogram with kde curve')
plt.xlabel('FLipper Length')
plt.ylabel('Count')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper Length vs Body mass')
plt.xlabel('FLipper Length')
plt.ylabel('Body Mass')
plt.show()

corr=df.corr(numeric_only=True)
print("Correlation Table")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()