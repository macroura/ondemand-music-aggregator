from fastapi import FastAPI
from track_data import track_instance

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/tracks")
def get_tracks():
    sample_track = track_instance(
        id="1",
        source="YouTube",
        source_id="abc123",
        title="Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)",
        artist_or_channel="Rick Astley",
        duration=213,
        external_url="https://youtu.be/dQw4w9WgXcQ?si=qDKboURQ8BaBU8eb"
    )
    return [sample_track]