### goit-pythonweb-hw-10 (Fast API, auth, login)

`source $(poetry env info --path)/bin/activate`

`poetry add fastapi uvicorn asyncpg sqlalchemy alembic greenlet psycopg2-binary python-jose passlib libgravatar python-multipart bcrypt`


`docker run --name postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=fE512 -d postgres`


{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWxkZW4iLCJleHAiOjE3NDMxNzM4NTJ9.2Q7NAt4858nZS-Y9wAFyAP868hYZvlnY96eWsec9N4c",
    "token_type": "bearer"
}