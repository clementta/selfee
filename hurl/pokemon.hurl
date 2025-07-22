POST http://127.0.0.1:8000/api/login/
[Form]
username: test
password: test
HTTP 200
[Captures]
token: jsonpath "$['token']"

POST http://127.0.0.1:8000/api/group/poison/add
Authorization: Token {{token}}
HTTP 200

GET http://127.0.0.1:8000/api/pokemon
Authorization: Token {{token}}
HTTP 200
[Captures] 
poison_count: jsonpath "$['pokemon']" count
[Asserts]
jsonpath "$.pokemon" count == 102

GET http://127.0.0.1:8000/api/pokemon/bulbasaur
Authorization: Token {{token}}
HTTP 200
[Asserts]
jsonpath "$.name" == "bulbasaur"
jsonpath "$.id" == 1
jsonpath "$.types[1].type.name" == "poison"

GET http://127.0.0.1:8000/api/pokemon/4
Authorization: Token {{token}}
HTTP 404
[Asserts]

POST http://127.0.0.1:8000/api/group/fire/add
Authorization: Token {{token}}
HTTP 200

GET http://127.0.0.1:8000/api/pokemon
Authorization: Token {{token}}
HTTP 200
[Asserts]
jsonpath "$.pokemon" count >= {{ poison_count }}

GET http://127.0.0.1:8000/api/pokemon/4
Authorization: Token {{token}}
HTTP 200
[Asserts]
jsonpath "$.name" == "charmander"
jsonpath "$.id" == 4
jsonpath "$.types[0].type.name" == "fire"

POST http://127.0.0.1:8000/api/group/poison/remove
Authorization: Token {{token}}
HTTP 200

GET http://127.0.0.1:8000/api/pokemon/bulbasaur
Authorization: Token {{token}}
HTTP 404

POST http://127.0.0.1:8000/api/group/fire/remove
Authorization: Token {{token}}
HTTP 200
