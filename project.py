import pandas as pd
import pandas_profiling

# data = pd.read_csv('titanic.csv')
# profile = data.profile_report(title='Titanic Dataset')
# profile.to_file(output_file='result/titanic_report.html')


data = pd.read_csv('cosmic_feb.csv')
profile = data.profile_report(title='Cosmic figures Feb')
profile.to_file(output_file='result/cosmic_feb.html')