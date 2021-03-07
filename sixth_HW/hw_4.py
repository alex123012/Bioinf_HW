import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv('TCGA-COAD.tsv', sep='\t'))

df71 = df.loc[:, ('Gene', 'TCGA-A6-2671-11A')]
df75 = df.loc[:, ('Gene', 'TCGA-A6-2675-11A')]

df75_100 = df75.sort_values('TCGA-A6-2675-11A', ascending=False).iloc[:100]
df71_100 = df71.sort_values('TCGA-A6-2671-11A', ascending=False).iloc[:100]

set_75 = set(df75_100.Gene)
set_71 = set(df71_100.Gene)
inter = set_75.intersection(set_71)

print(inter)

df.set_index('Gene', inplace=True)

df_plot = df.loc[inter, ('TCGA-A6-2671-11A', 'TCGA-A6-2675-11A')]
print(df_plot.shape)
sns.scatterplot(data=df_plot, x="TCGA-A6-2675-11A", y="TCGA-A6-2671-11A")
plt.tight_layout()
plt.show()
