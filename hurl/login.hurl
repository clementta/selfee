POST http://127.0.0.1:8000/api/login/
[Form]
username: test
password: test
HTTP 200
[Captures]
token: jsonpath "$['token']"

POST http://127.0.0.1:8000/api/group/normal/add
Authorization: Token {{token}}
HTTP 200

POST http://127.0.0.1:8000/api/group/notatype/add
Authorization: Token {{token}}
HTTP 400

POST http://127.0.0.1:8000/api/group/normal/remove
Authorization: Token {{token}}
HTTP 200

POST http://127.0.0.1:8000/api/group/normal/remove
Authorization: Token {{token}}
HTTP 200

POST http://127.0.0.1:8000/api/group/notatype/remove
Authorization: Token {{token}}
HTTP 400

POST http://127.0.0.1:8000/api/group/poison/add
Authorization: Token {{token}}
HTTP 200

GET http://127.0.0.1:8000/api/user/me
Authorization: Token {{token}}
HTTP 200
[Asserts]
jsonpath "$.username" exists
jsonpath "$.email" exists
jsonpath "$.pokemon_types" contains "poison"

POST http://127.0.0.1:8000/api/group/poison/remove
Authorization: Token {{token}}
HTTP 200
