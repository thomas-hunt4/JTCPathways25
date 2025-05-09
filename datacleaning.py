import pandas as pd
import numpy as np

data = {
'date': pd.date_range('2023-02-01', periods=7),
'temperature': [29.5, np.nan, 30.3, 28.8, np.nan, 29.1, 30.7],
'humidity': [75, 72, np.nan, 74, 71, np.nan, 73],
'precipitation': [0.0, 0.2, 0.0, np.nan, 0.4, 0.0, 0.2]
}

df = pd.DataFrame(data)
# print(df)


# print(df.isna().sum())

# print(df.isna().mean() * 100)

# # print(df.dropna())

# print(df.fillna(value=df.mean()))

# print(df.max())
# print(df.min())

# df_ffill = df.fillna(method='ffill')
# print(df_ffill)


# messy['date'] = pd.to_datetime(messy['date'], errors='coerce')


# def standardize

# Sample data with inconsistent types
data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', '32°C', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}

messy_df = pd.DataFrame(data)
# print("Original messy DataFrame:")
print(messy_df)
# print("\nData types:")
# print(messy_df.dtypes)

# Convert date column to datetime
messy_df['date'] = pd.to_datetime(messy_df['date'], errors='coerce')
print("After date conversion:")
print(messy_df)

# def my_funky_function(value):
#     if pd.isna(value):
#         return np.nan
#     elif isinstance(value, (int, float)):
#         return float(value)
#     else:
#         import re 
#         match = re.search(r'(\d+\.?\d*)', str(value))
#         if match:
#             return float(match.group(1))
#     return np.nan

# this_thing = messy_df['date'].apply(my_funky_function())

# print(this_thing)

def clean_humidity(data):
    for key, values in data.items():
        if 'humidity' in key:
            clean = values.stripe('%\,percent')
            return clean 
        
print(clean_humidity(data))





    
# messy_df['temperature numerical']=






