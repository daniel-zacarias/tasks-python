from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: Optional[int] = Field(None, description="Id da tarefa")
    name: str = Field(..., description="Nome/titulo da tarefa")
    description: Optional[str] = Field(None, description="Descrição da tarefa")
    start_date: Optional[datetime] = Field(None, description="Data de inicio da tarefa")
    end_date: Optional[datetime] = Field(None, description="Data de finalização da tarefa")


class InputCreateTaskDto(BaseModel):
    name: str = Field(..., description="Nome/titulo da tarefa")
    description: Optional[str] = Field(None, description="Descrição da tarefa")
    start_date: Optional[datetime] = Field(None, description="Data de inicio da tarefa")
    end_date: Optional[datetime] = Field(None, description="Data de finalização da tarefa")


class OutputCreateTaskUserDto(BaseModel):
    id: int = Field(..., description="Id do usuário que criou a tarefa")
    name: str = Field(...,  description="Nome do usuário que criou a tarefa")


class OutputCreateTaskDto(BaseModel):
    name: str = Field(..., description="Nome/titulo da tarefa")
    description: Optional[str] = Field(None, description="Descrição da tarefa")
    start_date: Optional[datetime] = Field(None, description="Data de inicio da tarefa")
    end_date: Optional[datetime] = Field(None, description="Data de finalização da tarefa")
    user: OutputCreateTaskUserDto = Field(..., description="Usuário")
