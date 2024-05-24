### Skrypty

- **random_forest.ipynb** - Trenuje las losowy po raz pierwszy z dużą ilością estymatorów, na jego podstawie selekcjonowane są atrybuty. Zapisuje wyselekcjonowane i znormalizowane dane do `<root>/data/final/selected.csv`. Następnie trenuje drugi model z mniejszą ilością estymatorów na wyselekcjonowanych danych. Oba modele są zapisywane do `<root>/models/trained` jako `rf_model.joblib` i `rf_selected_model.joblib`.

- **xgboost.ipynb** - Trenuje dwa modele XGBoost: jeden na wszystkich danych, drugi na wyselekcjonowanych danych. Oba modele są zapisane w `<root>/models/trained` jako `xgb_model.joblib` i `xgb_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.

- **neural_network.ipynb** - Trenuje model sztucznej sieci neuronowej na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/nn_selected_model.joblib`.

- **svm.ipynb** - Trenuje model SVM na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/svm_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.


w folderze client app znajduję się skrypt pythona pozwalający na łatwierze wysłanie polecenia CURl
odpalane z folderu projektu przy uzyciu:

   *python3 ./clientapp/clientapp.py --filename ./data/final/selected.csv*

klasyfikatory można również odpalić bezpośrednio poleceniem:

    **curl -X POST -H "Content-Type:application/json" -d '{"key1":1, "key2":2}' http://localhost:8080/predictionB*