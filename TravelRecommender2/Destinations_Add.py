import pandas as pd

df = pd.read_csv('destinations_new.csv', na_values='N/A', encoding='latin1')

days_to_stay_values = ['4-6 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '4-6 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '4-6 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '4-6 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '4-6 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '4-6 days', '1-3 days', '1-3 days',
                       '1-3 days', '4-6 days', '4-6 days', '4-6 days', '7+ days', '1-3 days', '4-6 days', '4-6 days', '1-3 days', '4-6 days', '4-6 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '4-6 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '4-6 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days',
                       '1-3 days', '1-3 days', '1-3 days', '1-3 days', '1-3 days']

df['Days to Travel'] = days_to_stay_values

df.to_csv('destinations2.csv', index=False)