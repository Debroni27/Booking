import fastapi

from .routers.user_routers import router as user_router

router = fastapi.APIRouter()

router.include_router(router=user_router)
