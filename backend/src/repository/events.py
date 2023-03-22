import fastapi
import loguru
from src.repository.database import mongo_db


async def initialize_db_connection(backend_app: fastapi.FastAPI) -> None:
    """Inittialize MongoDB via motor driver and set (db, client) to FastApi state"""

    loguru.logger.info("Database Connection --- Start Connection . . .")

    await mongo_db.connect(backend_app=backend_app)

    try:
        await mongo_db.client.admin.command("ping")
        loguru.logger.info("Connected to MongoDB database.")

    except Exception as e:
        loguru.logger.error(f"Error connecting to MongoDB database: {e}")
        await mongo_db.close()
        return

    loguru.logger.info("Database Connection --- Successfully Connect!")


async def dispose_db_connection() -> None:
    """Close connection with MngoDB after shutdown FastApi app"""

    loguru.logger.info("Database Connection --- Closing . . .")

    await mongo_db.close()

    loguru.logger.info("Database Connection --- Successfully Closed!")
