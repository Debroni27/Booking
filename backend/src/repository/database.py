import fastapi

from motor.motor_asyncio import AsyncIOMotorClient

from src.config.manager import settings


class AsyncMongoDriver:
    def __init__(self) -> None:
        self.mongodb_uri: str = f"mongodb://{settings.MONGODB_USENRAME}:{settings.MONGODB_PASSWORD}@mongodb:27017/{settings.MONGODB_DB_NAME}"
        self.client = AsyncIOMotorClient(self.mongodb_uri)

    async def connect(self, backend_app: fastapi.FastAPI) -> None:
        backend_app.state.client = self.client
        backend_app.state.db = backend_app.state.client[f"{settings.MONGODB_DB_NAME}"]

    async def close(self) -> None:
        self.client.close()


mongo_db: AsyncMongoDriver = AsyncMongoDriver()
