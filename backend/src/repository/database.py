from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..config.manager import settings


class AsyncMongoDB:
    def __init__(self) -> None:
        self.mongodb_uri: str = f"mongodb://{settings.MONGODB_USENRAME}:{settings.MONGODB_PASSWORD}@localhost:27017/{settings.MONGODB_DB_NAME}"
        self.client: AsyncIOMotorClient(self.mongodb_uri)

    @property
    def database(self) -> AsyncIOMotorDatabase:
        database: AsyncIOMotorDatabase = self.client[f"{settings.MONGODB_DB_NAME}"]
        return database


mongo_db: AsyncMongoDB = AsyncMongoDB()
