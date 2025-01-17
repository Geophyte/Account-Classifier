import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
selected_path = os.path.join(current_dir, 'final', 'selected.csv')
final_path = os.path.join(current_dir, 'final', 'final.csv')
result_path = os.path.join(current_dir, 'final', 'selected_updated.csv')

selected_columns_df = pd.read_csv(selected_path)
selected_columns = set(selected_columns_df.columns)

final_df = pd.read_csv(final_path)

filtered_df = final_df[list(selected_columns.intersection(final_df.columns))]

columns_to_normalize = [col for col in filtered_df.columns if col != 'user_id']
scaler = StandardScaler()
normalized_data = scaler.fit_transform(filtered_df[columns_to_normalize])

normalized_df = pd.DataFrame(normalized_data, columns=columns_to_normalize)
normalized_df['user_id'] = filtered_df['user_id']

normalized_df.to_csv(result_path, index=False)

print(f"Normalization complete and saved to '{result_path}'.")
