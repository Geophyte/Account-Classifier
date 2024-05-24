import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

df1 = pd.read_csv(os.path.join(current_dir, 'selected.csv'))
df2 = pd.read_csv(os.path.join(current_dir, 'selected_updated.csv'))

columns1 = set(df1.columns)
columns2 = set(df2.columns)

if columns1 == columns2:
    print("Both CSV files have the same columns.")

    if df1.equals(df2):
        print("Both CSV files have the same data.")
    else:
        merged_df = df1.merge(df2, how='outer', indicator=True)

        diff_rows = merged_df[merged_df['_merge'] != 'both']
        num_diff_rows = len(diff_rows)

        print(f"The number of differing rows between the two files is: {num_diff_rows}")
else:
    diff1 = columns1 - columns2
    diff2 = columns2 - columns1

    print("The columns are different.")
    if diff1:
        print(f"Columns in file1.csv but not in file2.csv: {diff1}")
    if diff2:
        print(f"Columns in file2.csv but not in file1.csv: {diff2}")

