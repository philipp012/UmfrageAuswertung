import matplotlib
import pandas as pd
from jedi.api.refactoring import inline
from matplotlib.pyplot import pie, axis, show
%matplotlib inline

df = pd.read_csv ('../partyDistribution.csv')

sums = df.groupby(df["Product Name;"])["Number Of Bugs"].sum()
axis('equal');
pie(sums, labels=sums.index);
show()