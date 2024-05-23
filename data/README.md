### Skrypty

- **init_data.py** - Dokonuje INNER JOIN tabel `sessions.jsonl`, `tracks.jsonl`, `users.jsonl`, odrzucając mniej użyteczne kolumny. Zapisuje wyniki operacji do `<root>/data/final/initial.csv`.

- **generate_final.py** - Dokonuje grupowania rekordów po `user_id` i wylicza wiele statystyk jako późniejsze atrybuty dla modeli. Zapisuje wyniki operacji do `<root>/data/final/final.csv`.

- **generate_selected.py** - Generuje dane z `<root>/data/final/final.csv` na podstawie wygenerowanych przez `random_forest` `<root>/data/final/selected.csv`. Ma za zadanie aktualizować rekordy `<root>/data/final/selected.csv` na wypadek dodania nowych danych. Zapisuje wyniki operacji do `<root>/data/final/selected_updated.csv`.

- **final/check_similarity.py** - Sprawdza podobieństwo między `<root>/data/final/selected.csv` a `<root>/data/final/selected_updated.csv`. Informuje o różnicach w kolumnach i rekordach.