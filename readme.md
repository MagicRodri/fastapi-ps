## A test app with a simple REST API written in Python using FastAPI and SQLAlchemy
## To run the app, you need to have Docker installed on your machine
## 1. Clone the repo
```bash
git clone https://github.com/MagicRodri/fastapi-ps.git
```
## 2. cd into the src folder and create a .env file with the following content:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=db
```
## 3. Run docker-compose up --build
## 4. The app will be available at http://localhost:8000

# Description
## The app has 2 main endpoints for two tasks:
## 1. /api/v1/quizzes/random - POST returns a list of random quizzes with detail from https://jservice.io/api/ . The number of quizzes is specified in the request body.
Example request:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/quizzes/random' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 3
}'
```
example response:
```json
[
    {
        "id":120010,
        "question":"Sousa was instrumental in the design of the sousaphone, a bass one of these with an upright bell",
        "answer":"a tuba","created_at":"2022-12-30T19:54:27.779000"
    },
    {
        "id":132555,
        "question":"Old-world monkeys, like our friend the patas, don't have prehensile these, many new-world monkeys do",
        "answer":"tails","created_at":"2022-12-30T20:11:33.615000"
    },
    {
        "id":151330,
        "question":"Wrecking Crew drummer Hal Blaine used tire chains to lay down the crashing sounds on this Simon & Garfunkel No. 1",
        "answer":"\"Bridge Over Troubled Water\"","created_at":"2022-12-30T20:37:25.632000"
    }
]
```

## 2. /api/v1/users - POST creates a new user. The request body should contain the username. Returns the created user with a basic uuid4 token.
Example request:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testuser"
}'
```
example response:
```json
{
    "id": 1,
    "username": "testuser",
    "token": "a0e0e0e0-0e0e-0e0e-0e0e-0e0e0e0e0e0e",
    "is_active": true
}
```

## 3. /api/v1/users/records/ - POST creates a new record for the user. The request body should contain the user payload consisting of the user id and the token and the record file in wav format. Returns the created record's url for download.
Example request:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/users/records' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'payload={
  "id": 2,
  "access_token": "95e491a7-7553-44f6-a9ed-fa5334140cbd"
}' \
  -F 'file=@test.wav;type=audio/x-wav'
```
example response:
```json
{
    "url": "/api/v1/users/records/642fab15-a143-4ee9-86cf-e7861476d3e1/2"
}
```

## 4. /api/v1/users/records/<uuid:id>/<int:user_id> - Download the record file.
Example request:
```bash
curl -O "http://127.0.0.1:8000/api/v1/users/records/642fab15-a143-4ee9-86cf-e7861476d3e1/2"
```