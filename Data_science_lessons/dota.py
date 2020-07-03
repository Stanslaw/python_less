import pandas as pd
import seaborn as sns

dotka = pd.read_csv('dota_hero_stats.csv')

print(dotka.loc[:, ['localized_name', 'legs']])
