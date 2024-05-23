import pandas as pd
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer


def prepare_final(final_df: pd.DataFrame) -> pd.DataFrame:
    final_df.drop(columns=['user_id'], inplace=True)

    mlb = MultiLabelBinarizer()
    encoded_genres = pd.DataFrame(mlb.fit_transform(final_df['favourite_genres']), columns=mlb.classes_, index=final_df.index)
    final_df = pd.concat([final_df.drop('favourite_genres', axis=1), encoded_genres], axis=1)

    numeric_columns = final_df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    scaler = StandardScaler()
    final_df[numeric_columns] = scaler.fit_transform(final_df[numeric_columns])

    return final_df
