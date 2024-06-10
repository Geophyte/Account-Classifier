# Uruchamianie 

### Dane

w pliku selected.csv znajdują się przykładowe dane utworzone z dostarczonych danych użytkowników. Jest ich bardzo dużo dlatego proces predykcji zajmuje stosunkowo dużo czasu. Należy zastąpić go nowymi danymi dla których chcemy uzyskać predykcję posiadania statusu premium.

Dane możemy wygenrować za pomocą zawartych w folderze /dane skryptów opsianych w tamtejszym README.md

### Mikroserwis

Aby uzyskać predykcję należy uruchomić microserwis:

W celu uruchomienia microserwisu należy w folderze app uruchomić program app.py poprzez wywołanie polecenia *python3 app.py*

a następnie podać dane dla klasyfikatorów AB poprzez polecenie:

*curl -X POST -F "file=@data/final/selected.csv" http://localhost:8080/prediction*

w folderze client app znajduję się również skrypt pythona pozwalający na łatwiejsze wysłanie polecenia CURL
odpalane z folderu projektu przy uzyciu:

*python3 ./clientapp/clientapp.py --filename ./data/final/selected.csv*

Test AB odbywa się poprzez losowe wybranie przez microserwis jednego ze sprawdzanych modeli (RF - Random Forest lub XGBoost)

Wyniki każdego z nich zostają zapisane w oddzielnych plikach loggera w podfolderze *app/logs*.
Znajduje się tam ID użytkownika który został przeanalizowany oraz wynik predykcji danego modelu w celu ułatwienia późniejszej analizy skuteczności.
