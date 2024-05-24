import os
import pandas as pd
from analysis.utils import load_jsonl


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sessions_path = os.path.join(current_dir, 'v3', 'sessions.jsonl')
    tracks_path = os.path.join(current_dir, 'v3', 'tracks.jsonl')
    users_path = os.path.join(current_dir, 'v3', 'users.jsonl')
    result_path = os.path.join(current_dir, 'final', 'initial.csv')

    nonexistent_paths = []
    if not os.path.exists(sessions_path):
        nonexistent_paths.append(sessions_path)
    if not os.path.exists(tracks_path):
        nonexistent_paths.append(tracks_path)
    if not os.path.exists(users_path):
        nonexistent_paths.append(users_path)
    if len(nonexistent_paths) > 0:
        raise FileNotFoundError(f"The following paths do not exist: {', '.join(nonexistent_paths)}")

    sessions_df = load_jsonl(sessions_path)
    tracks_df = load_jsonl(tracks_path)
    users_df = load_jsonl(users_path)

    tracks_df['release_year'] = pd.to_datetime(tracks_df['release_date'], format='mixed').dt.year
    tracks_df['mode'] = tracks_df['mode'].fillna(-1)

    tracks_df.drop(columns=['name'], inplace=True)
    users_df.drop(columns=['name', 'street'], inplace=True)

    merged_df = pd.merge(sessions_df, users_df, on='user_id', how='inner')
    merged_df = pd.merge(merged_df, tracks_df, left_on='track_id', right_on='id', how='inner')

    merged_df.to_csv(result_path, index=False)
    print(merged_df.columns)
    print(merged_df.head())


if __name__ == '__main__':
    main()
