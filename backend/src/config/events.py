import typing

import fastapi
import loguru

from repository.events import dispose_db_connection, initialize_db_connection


def execute_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    @loguru.logger.catch
    async def launch_backend_server_events() -> None:
        await initialize_db_connection(backend_app=backend_app)

    return launch_backend_server_events


def terminate_backend_server_event_handler() -> typing.Any:
    @loguru.logger.catch
    async def stop_backend_server_events() -> None:
        await dispose_db_connection()

    return stop_backend_server_events
