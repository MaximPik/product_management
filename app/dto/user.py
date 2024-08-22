# Использовуется для организации структур данных, которые служат промежуточными объектами
# для передачи данных между различными слоями приложения

from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int