from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4


class BaseModelWithID(BaseModel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._id = str(uuid4())

    @property
    def id(self) -> str:
        return self._id
    

# schemas for the planning stage
# TODO
class PlanItem(BaseModelWithID):
    pass
    
class Plan(BaseModelWithID):
    pass

class PlanGrading(BaseModelWithID):
    pass