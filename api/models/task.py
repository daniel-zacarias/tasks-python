from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class TaskModel(BaseModel):
    id: Optional[int] = Field(None, description="Id da tarefa")
    name: str = Field(..., description="Nome/titulo da tarefa")
    description: Optional[str] = Field(None, description="Descrição da tarefa")
    start_date: Optional[datetime]  = Field(None, description="Data de inicio da tarefa")
    end_date: Optional[datetime]  = Field(None, description="Data de finalização da tarefa")