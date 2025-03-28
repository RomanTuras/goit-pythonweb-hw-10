class Config:
    DB_URL = "postgresql+asyncpg://postgres:fE512@localhost:5432/contacts"
    JWT_SECRET = "44_02_76"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600

config = Config
