from datetime import datetime

from pydantic import BaseModel


class NewsModel(BaseModel):
    """ Validate request data """
    title: str
    content: str


class NewsDetailsModel(NewsModel):
    """ Return response data """
    id: int
    created_at: datetime
    user_name: str
    likes: int
