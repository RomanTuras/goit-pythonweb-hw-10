### goit-pythonweb-hw-10 (Fast API, auth, login, email verification)

`source $(poetry env info --path)/bin/activate`

`poetry add fastapi uvicorn asyncpg sqlalchemy alembic greenlet psycopg2-binary python-jose passlib libgravatar 
python-multipart bcrypt aiosmtplib pydantic-settings jinja2 python-dotenv`
`poetry add 'pydantic[email]'`

`docker run --name postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=fE512 -d postgres`
