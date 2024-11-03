from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from api.dto.user import OutputTokenUserDto
from api.security.token import get_current_user
from api.services.task import create_task as service
from api.connectors.db_connection_session import Database
from api.dto.task import InputCreateTaskDto
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.task import TaskModel

router = APIRouter(prefix="/tasks")


@router.post("/")
async def create_task(
        input: InputCreateTaskDto,
        session: AsyncSession = Depends(Database().session),
        current_user: OutputTokenUserDto = Depends(get_current_user)):
    task_model = TaskModel(
        name=input.name,
        description=input.description,
        start_date=input.start_date,
        end_date=input.end_date
    )
    output = await service(task_model, current_user, session)
    return JSONResponse(
        status_code=201,
        content=output.model_dump()
    )
