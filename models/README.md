### Skrypty

- **random_forest.ipynb** - Trenuje las losowy po raz pierwszy z dużą ilością estymatorów, na jego podstawie selekcjonowane są atrybuty. Zapisuje wyselekcjonowane i znormalizowane dane do `<root>/data/final/selected.csv`. Następnie trenuje drugi model z mniejszą ilością estymatorów na wyselekcjonowanych danych. Oba modele są zapisywane do `<root>/models/trained` jako `rf_model.joblib` i `rf_selected_model.joblib`.

- **xgboost.ipynb** - Trenuje dwa modele XGBoost: jeden na wszystkich danych, drugi na wyselekcjonowanych danych. Oba modele są zapisane w `<root>/models/trained` jako `xgb_model.joblib` i `xgb_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.

- **neural_network.ipynb** - Trenuje model sztucznej sieci neuronowej na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/nn_selected_model.joblib`.

- **svm.ipynb** - Trenuje model SVM na wyselekcjonowanych danych i zapisuje go do `<root>/models/trained/svm_selected_model.joblib`. **Uwaga:** Zawiera sekcję strojenia parametrów, która może zająć trochę czasu.


# Uruchamianie 


w pliku selected.csv znajdują się przykładowe dane utworzone z dostarczonych danych użytkowników. Należy zastąpić do nowymi danymi dla których chcemy uzyskać predykcję posiadania statusu premium

Aby uzyskać predykcję należy uruchomić microserwi:

W celu uruchomienia microserwisu należy w folderze app uruchomić program app.py poprzez wywołanie polecenia *python3 app.py*

a następnie podać dane dla klasyfikatorów AB poprzez polecenie:

*curl -X POST -F "file=@data/final/selected.csv" http://localhost:8080/prediction*

w folderze client app znajduję się również skrypt pythona pozwalający na łatwiejsze wysłanie polecenia CURl
odpalane z folderu projektu przy uzyciu:

*python3 ./clientapp/clientapp.py --filename ./data/final/selected.csv*

Test AB odbywa się poprzez losowe wybranie przez microserwis jednego ze sprawdzanych modeli (RF - Random Forest lub XGB)

Wyniki każdego z nich zostają zapisane w oddzielnych plikach loggera w podfolderze *app/logs*.
Znajduje się tam ID użytkownika który został przeanalizowany oraz wynik predykcji danego modelu w celu ułatwienia późniejszej analizy skuteczności.




