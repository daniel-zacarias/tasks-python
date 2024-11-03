from sqlalchemy.ext.asyncio import AsyncSession

from api.dto.task import OutputCreateTaskDto, OutputCreateTaskUserDto
from api.entities.task import Task
from api.models.task import TaskModel
from api.models.user import UserModel


async def create_task(task: TaskModel, user: UserModel, session: AsyncSession):
    insert_task = Task(
        name=task.name,
        description=task.description,
        start_date=task.start_date,
        end_date=task.end_date,
        user_id=user.id
    )
    dto_user = OutputCreateTaskUserDto(
        id=user.id,
        name=user.name
    )
    session.add(insert_task)
    await session.commit()
    await session.refresh(insert_task)
    return OutputCreateTaskDto(
        name=insert_task.name,
        description=insert_task.description,
        start_date=insert_task.start_date,
        end_date=insert_task.end_date,
        user=dto_user
    )
