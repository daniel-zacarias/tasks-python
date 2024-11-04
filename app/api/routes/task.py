from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.api.dependencies.database import get_db
from app.schemas.user import OutputTokenUserDto
from app.api.dependencies.security import get_current_user
from app.domain.services.task import create_task as service
from app.schemas.task import InputCreateTaskDto
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.task import TaskModel

router = APIRouter(prefix="/tasks")


@router.post("/")
async def create_task(
        input: InputCreateTaskDto,
        session: AsyncSession = Depends(get_db),
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
