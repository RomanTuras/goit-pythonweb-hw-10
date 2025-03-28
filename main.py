from fastapi import FastAPI

from src.api import utils, contacts, auth, users

app = FastAPI()

app.include_router(utils.router, prefix="/api/v1")
app.include_router(contacts.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)

