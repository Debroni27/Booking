import fastapi
from models.base import BaseResponseModel
from repository.base import BaseCRUDRepository

router = fastapi.APIRouter(prefix="/users", tags=["users"])


@router.get(
    path="",
    name="users: get current user",
    response_model=BaseResponseModel,
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_root_message() -> BaseResponseModel:
    test_response = BaseCRUDRepository()
    return test_response.get()
