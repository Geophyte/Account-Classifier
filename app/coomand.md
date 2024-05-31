python3 app/app.py

then

curl -X POST -H "Content-Type:application/json" -d '{"key1":1, "key2":2, "key3":3, "key4":4, "key5":5}' http://localhost:8080/predictionA


curl -X POST -H "Content-Type:application/json" -d '{"key1":1, "key2":2}' http://localhost:8080/prediction