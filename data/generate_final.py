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

    def calculate_metrics(group: pd.DataFrame):
        skip_count = (group['event_type'] == 'Skip').sum()
        play_count = (group['event_type'] == 'Play').sum()
        like_count = (group['event_type'] == 'Like').sum()

        group['timestamp'] = pd.to_datetime(group['timestamp'])

        timestamp_diff = group['timestamp'].diff().astype('int64')
        daily_activity = group.groupby(group['timestamp'].dt.date).size().reset_index(name='daily_activity')
        weekly_activity = group.groupby(group['timestamp'].dt.to_period('W')).size().reset_index(name='weekly_activity')
        monthly_activity = group.groupby(group['timestamp'].dt.to_period('M')).size().reset_index(name='monthly_activity')

        return pd.Series({
            'favourite_genres': group['favourite_genres'].iloc[0],
            'premium_user': group['premium_user'].iloc[0],
            'popularity_mean': group['popularity'].mean(),
            'popularity_std': group['popularity'].std(),
            'popularity_mode': group['popularity'].mode().iloc[0],
            'popularity_median': group['popularity'].median(),
            'popularity_min': group['popularity'].min(),
            'popularity_max': group['popularity'].max(),
            'duration_ms_mean': group['duration_ms'].mean(),
            'duration_ms_std': group['duration_ms'].std(),
            'duration_ms_mode': group['duration_ms'].mode().iloc[0],
            'duration_ms_median': group['duration_ms'].median(),
            'duration_ms_min': group['duration_ms'].min(),
            'duration_ms_max': group['duration_ms'].max(),
            'explicit_ratio': group['explicit'].mean(),
            'explicit_count': group['explicit'].sum(),
            'explicit_min': group['explicit'].min(),
            'explicit_max': group['explicit'].max(),
            'danceability_mean': group['danceability'].mean(),
            'danceability_std': group['danceability'].std(),
            'danceability_mode': group['danceability'].mode().iloc[0],
            'danceability_median': group['danceability'].median(),
            'danceability_min': group['danceability'].min(),
            'danceability_max': group['danceability'].max(),
            'energy_mean': group['energy'].mean(),
            'energy_std': group['energy'].std(),
            'energy_mode': group['energy'].mode().iloc[0],
            'energy_median': group['energy'].median(),
            'energy_min': group['energy'].min(),
            'energy_max': group['energy'].max(),
            'loudness_mean': group['loudness'].mean(),
            'loudness_std': group['loudness'].std(),
            'loudness_mode': group['loudness'].mode().iloc[0],
            'loudness_median': group['loudness'].median(),
            'loudness_min': group['loudness'].min(),
            'loudness_max': group['loudness'].max(),
            'speechiness_mean': group['speechiness'].mean(),
            'speechiness_std': group['speechiness'].std(),
            'speechiness_mode': group['speechiness'].mode().iloc[0],
            'speechiness_median': group['speechiness'].median(),
            'speechiness_min': group['speechiness'].min(),
            'speechiness_max': group['speechiness'].max(),
            'acousticness_mean': group['acousticness'].mean(),
            'acousticness_std': group['acousticness'].std(),
            'acousticness_mode': group['acousticness'].mode().iloc[0],
            'acousticness_median': group['acousticness'].median(),
            'acousticness_min': group['acousticness'].min(),
            'acousticness_max': group['acousticness'].max(),
            'instrumentalness_mean': group['instrumentalness'].mean(),
            'instrumentalness_std': group['instrumentalness'].std(),
            'instrumentalness_mode': group['instrumentalness'].mode().iloc[0],
            'instrumentalness_median': group['instrumentalness'].median(),
            'instrumentalness_min': group['instrumentalness'].min(),
            'instrumentalness_max': group['instrumentalness'].max(),
            'liveness_mean': group['liveness'].mean(),
            'liveness_std': group['liveness'].std(),
            'liveness_mode': group['liveness'].mode().iloc[0],
            'liveness_median': group['liveness'].median(),
            'liveness_min': group['liveness'].min(),
            'liveness_max': group['liveness'].max(),
            'valence_mean': group['valence'].mean(),
            'valence_std': group['valence'].std(),
            'valence_mode': group['valence'].mode().iloc[0],
            'valence_median': group['valence'].median(),
            'valence_min': group['valence'].min(),
            'valence_max': group['valence'].max(),
            'tempo_mean': group['tempo'].mean(),
            'tempo_std': group['tempo'].std(),
            'tempo_mode': group['tempo'].mode().iloc[0],
            'tempo_median': group['tempo'].median(),
            'tempo_min': group['tempo'].min(),
            'tempo_max': group['tempo'].max(),
            'key_mode': group['key'].mode().iloc[0],
            'key_median': group['key'].median(),
            'key_min': group['key'].min(),
            'key_max': group['key'].max(),
            'mode_mode': group['mode'].mode().iloc[0],
            'mode_median': group['mode'].median(),
            'mode_min': group['mode'].min(),
            'mode_max': group['mode'].max(),
            'release_year_mean': group['release_year'].mean(),
            'release_year_std': group['release_year'].std(),
            'release_year_mode': group['release_year'].mode().iloc[0],
            'release_year_median': group['release_year'].median(),
            'release_year_min': group['release_year'].min(),
            'release_year_max': group['release_year'].max(),
            'time_signature_mean': group['time_signature'].mean(),
            'time_signature_std': group['time_signature'].std(),
            'time_signature_mode': group['time_signature'].mode().iloc[0],
            'time_signature_median': group['time_signature'].median(),
            'time_signature_min': group['time_signature'].min(),
            'time_signature_max': group['time_signature'].max(),
            'unique_artist_count': group['artist_id'].nunique(),
            'unique_track_count': group['track_id'].nunique(),
            'city_frequency': group['city'].count() / unique_users,
            'skip_play_ratio': skip_count / play_count,
            'like_play_ratio': like_count / play_count,
            'skip_like_ratio': skip_count / like_count,
            'skip_count': skip_count,
            'like_count': like_count,
            'play_count': play_count,
            'session_count': group['user_id'].count(),
            'timestamp_diff_mean': timestamp_diff.mean(),
            'timestamp_diff_std': timestamp_diff.std(),
            'timestamp_diff_mode': timestamp_diff.mode().iloc[0],
            'timestamp_diff_median': timestamp_diff.median(),
            'timestamp_diff_min': timestamp_diff.min(),
            'timestamp_diff_max': timestamp_diff.max(),
            'timestamp_min': group['timestamp'].min().timestamp(),
            'timestamp_max': group['timestamp'].max().timestamp(),
            'time_range': (group['timestamp'].max() - group['timestamp'].min()).total_seconds(),
            'daily_activity': daily_activity['daily_activity'].mean(),
            'weekly_activity': weekly_activity['weekly_activity'].mean(),
            'monthly_activity': monthly_activity['monthly_activity'].mean(),
            'daily_activity_max': daily_activity['daily_activity'].max(),
            'weekly_activity_max': weekly_activity['weekly_activity'].max(),
            'monthly_activity_max': monthly_activity['monthly_activity'].max(),
            'daily_activity_min': daily_activity['daily_activity'].min(),
            'weekly_activity_min': weekly_activity['weekly_activity'].min(),
            'monthly_activity_min': monthly_activity['monthly_activity'].min(),
        })

    initial_df = initial_df.groupby('user_id').apply(calculate_metrics)
    initial_df.reset_index(inplace=True)

    initial_df.to_csv(result_path, index=False)
    print(initial_df.columns)
    print(initial_df.head())


if __name__ == '__main__':
    main()
