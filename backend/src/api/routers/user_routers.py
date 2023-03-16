import fastapi

from repository.base import BaseCRUDRepository
from models.base import ResponseModel

router = fastapi.APIRouter(prefix="/users", tags=["users"])


@router.get(
    path="",
    name="users: get current user",
    response_model=ResponseModel,
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_root_message() -> ResponseModel:
    test_response = BaseCRUDRepository()
    return test_response.get()
