from pydantic import BaseModel

class Message(BaseModel):
    """Schema para a mensagem de boas-vindas."""
    message: str