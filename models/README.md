### Skrypty

- **random_forest.ipynb** - Trenuje las losowy po raz pierwszy z dużą ilością estymatorów, na jego podstawie selekcjonowane są atrybuty. Zapisuje wyselekcjonowane i znormalizowane dane do `<root>/data/final/selected.csv`. Następnie trenuje drugi model z mniejszą ilością estymatorów na wyselekcjonowanych danych. Oba modele są zapisywane do `<root>/models/trained` jako `rf_model.joblib` i `rf_selected_model.joblib`.

- **xgboost.ipynb** - Trenuje dwa modele XGBoost: jeden na wszystkich danych, drugi na wyselekcjonowanych danych. Oba modele są zapisane w `<root>/models/trained` jako `xgb_model.joblib` i `xgb_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.

- **neural_network.ipynb** - Trenuje model sztucznej sieci neuronowej na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/nn_selected_model.joblib`.

- **svm.ipynb** - Trenuje model SVM na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/svm_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.