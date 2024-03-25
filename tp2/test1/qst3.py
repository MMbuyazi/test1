# 3.2
last_7_rows = df.tail(7)
print(last_7_rows)

# 3.3.1
print(df[['Nationality', 'Club']].head())

# 3.3.2
print(df.iloc[9])

# 3.3.3
print(df.loc[100:110, ['Goals', 'Appearances']])

# 3.3.4
df['Goals per Appearance'] = df['Goals'] / df['Appearances']
print(df.head())

# 3.3.5
arsenal_players = df[df['Club'] == 'Arsenal']
print(arsenal_players)

# 3.3.6
high_scorers = df[df['Goals'] > 5]
print(high_scorers)

# 3.4
# Command to upgrade pandas module
pip install --upgrade pandas

# 3.5

git add .
git commit -m "Pushing changes for TP2 test 1"
git push origin main
