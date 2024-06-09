# Raport Końcowy
## Klasyfikacja użytkowników premium w serwisie streamingu muzyki

- Ignacy Dąbkowksi
- Milan Wróblewski

## Założenia wstępne i cel projektu

Podstawowym celem projektu było wykonanie systemu oceny i analizy użytkowników systemu streamingu muzyki. Analiza polegała na przewidzeniu ich skłonności do posiadania/zakupu statusu premium w usłudze zleceniodawcy.
Oczekiwana była dokładność przekraczająca 75% skuteczności w stawianych przewidywaniach.

## Dane wejściowe
 W celu wykonania zlecenia, ostatecznie, otrzymaliśmy między innymi dane 30 tysięcy użytkowników oraz prawie 15 milionów zapisów interakcji tych użytkowników z serwisem. 

## Wykonanie projektu
W ramach wykonania projektu przygotowane zostały różne modele uczenia maszynowego z różnymi efektami końcowymi. Ostatecznie wykorzystane zostały dwa o najlepszej dokładności pracując na odpowiednio wybranych kategoriach danych. 
- Random Forest
- XGBoost
Oba z tych modeli znacznie przekroczyły oczekiwania i założenia postawione na początku projektu osiągając ROC Accuracy na poziomie **~87%** oraz Recall w zakresie **70-65%**.
Oba z wytrenowanych modeli spełniają warunek sukcesu projektu i zostają załączone wraz z całą dokumentacją w ramach rozwiązania zadania.

## Test AB
Badania *"laboratoryjne"* (mimo bardzo dużej ilości danych historycznych) często mogę nie pokrywać się ze stanem rzeczy w dynamicznych sytuacjach prawdziwego życia. Dlatego własnie został przygotowany dla zleceniodawcy microserwis pozwalający na uzyskanie predykcji dotyczącej nowych użytkowników poprzez losowanie modelu który tę klasyfikacje wykona. Microserwis następnie w zależności od wybranego modelu przygotowuje 2 pliki w których, oddzielnie dla każdego modelu, zapisane zostaną ID użytkownika oraz jego klasyfikacja. 

Pozwoli to aby w perspektywie czasu podjąć decyzję który z modeli zostanie wykorzystany w celu trwałej implementacji w systemie zleceniodawcy, na podstawie skuteczności wybranej strategii marketingowej oraz jej korelacji z każdym z modeli. 

## Podsumowanie
Dzieki dużej ilości dostępnych danych historycznych udało się przygotować dwa modele znacznie przekraczające kryterium sukcesu założone na początku projektu. Wierzymy, że wykorzystanie ślepego testu AB pozwoli zleceniodawcy na świadome wybranie jak najlepszego rozwiązania który w następstwie w czasie rzeczywistym będzie pomagał przyjąć optymalną strategię marketingową i w efekcie zwiększenie zysków i zadowolenia użytkowników których doświadczenia będą lepiej dopasowane do ich oczekiwań. 
