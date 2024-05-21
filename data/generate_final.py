import os
import pandas as pd


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    initial_path = os.path.join(current_dir, 'final', 'initial.csv')
    result_path = os.path.join(current_dir, 'final', 'final.csv')

    if not os.path.exists(initial_path):
        print("Run 'python -m data.init_data' in root directory")
        return

    initial_df = pd.read_csv(initial_path)
    print(initial_df.columns)
    print(initial_df.head())

    unique_users = initial_df['user_id'].nunique()

    def calculate_metrics(group):
        skip_count = (group['event_type'] == 'Skip').sum()
        play_count = (group['event_type'] == 'Play').sum()
        like_count = (group['event_type'] == 'Like').sum()

        return pd.Series({
            'favourite_genres': group['favourite_genres'].iloc[0],
            'premium_user': group['premium_user'].iloc[0],
            'popularity_mean': group['popularity'].mean(),
            'duration_ms_mean': group['duration_ms'].mean(),
            'explicit_ratio': group['explicit'].mean(),
            'danceability_mean': group['danceability'].mean(),
            'energy_mean': group['energy'].mean(),
            'loudness_mean': group['loudness'].mean(),
            'speechiness_mean': group['speechiness'].mean(),
            'acousticness_mean': group['acousticness'].mean(),
            'instrumentalness_mean': group['instrumentalness'].mean(),
            'liveness_mean': group['liveness'].mean(),
            'valence_mean': group['valence'].mean(),
            'tempo_mean': group['tempo'].mean(),
            'key_median': group['key'].median(),
            'release_year_median': group['release_year'].median(),
            'unique_artist_count': group['artist_id'].nunique(),
            'unique_track_count': group['track_id'].nunique(),
            'city_frequency': group['city'].count() / unique_users,
            'skip_play_ratio': skip_count / play_count,
            'like_play_ratio': like_count / play_count
        })

    initial_df = initial_df.groupby('user_id').apply(calculate_metrics, include_groups=True)
    initial_df.reset_index(inplace=True)

    initial_df.to_csv(result_path, index=False)
    print(initial_df.columns)
    print(initial_df.head())


if __name__ == '__main__':
    main()
