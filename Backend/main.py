from fastapi import FastAPI, HTTPException
from track_data import track_instance

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "backend",
    }

tracks = {
    "1": track_instance(
        id="1",
        source="YouTube",
        source_id="abc123",
        title="Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)",
        artist_or_channel="Rick Astley",
        duration=213,
        external_url="https://youtu.be/dQw4w9WgXcQ?si=qDKboURQ8BaBU8eb"
    ),
    "2": track_instance(
        id="2",
        source="YouTube",
        source_id="def456",
        title="Mr. Bombastic",
        artist_or_channel="Chuck Norris",
        duration=67,
        external_url="https://youtu.be/DWzL4VhRvZI?si=NVphcwiWi4HAVZRv"
    )
}

@app.get("/tracks/{track_id}")
def get_tracks(track_id: str):
    if track_id not in tracks:
        raise HTTPException(status_code=404, detail="Track is not found")
    return tracks[track_id]

@app.get("/playlists")
def get_playlists():
    return [
        {"id":"1","name":"Favorites","Track Count":"4"},
        {"id": "2", "name": "Workout Mix","Track Count": "5"}
    ]