from pydantic import BaseModel

class track_instance(BaseModel):
    id: str
    source: str #spotify or youtube
    source_id: str
    title: str
    artist_or_channel: str
    duration: int #in seconds
    external_url: str