from typing import Any, Generic, Optional, TypeVar, Type
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, model_id: Any) -> Optional[ModelType]:
        return db.query(self.model).get(model_id)
