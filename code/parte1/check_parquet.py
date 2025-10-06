import pandas as pd

# Read the integrated file
df = pd.read_parquet('bronze/medals_integrated_1896_2024.parquet')

print(f"Total records: {len(df)}")
print(f"\nColumns: {df.columns.tolist()}")

# Check USA
usa = df[df['country_noc'] == 'USA']
print(f"\nUSA total records: {len(usa)}")

# Check for 2024
usa_2024 = usa[usa['year'] == 2024]
print(f"\nUSA 2024 records: {len(usa_2024)}")
if len(usa_2024) > 0:
    print(usa_2024[['year', 'edition', 'season', 'gold', 'silver', 'bronze', 'total']])

# Check USA Summer
usa_summer = usa[usa['season'] == 'Summer']
print(f"\nUSA Summer total records: {len(usa_summer)}")
print(f"Gold: {int(usa_summer['gold'].sum())}")
print(f"Silver: {int(usa_summer['silver'].sum())}")
print(f"Bronze: {int(usa_summer['bronze'].sum())}")
print(f"Total: {int(usa_summer['total'].sum())}")

# Check USA Winter
usa_winter = usa[usa['season'] == 'Winter']
print(f"\nUSA Winter total records: {len(usa_winter)}")
print(f"Gold: {int(usa_winter['gold'].sum())}")
print(f"Silver: {int(usa_winter['silver'].sum())}")
print(f"Bronze: {int(usa_winter['bronze'].sum())}")
print(f"Total: {int(usa_winter['total'].sum())}")
