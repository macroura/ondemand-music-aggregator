# ondemand-music-aggregator
Web app that aggregates Spotify and YouTube music metadata into unified playlists.

## Month 5 Project Scope

### What the system does (If User has the supported platforms: Spotify & YouTube):
  - Create an account, with the ability to log in and log out
  - Connect Spotify and/or YouTube account-
  - Read user’s music meta data from those platforms, which includes:
      * Song Title
      * Artist Name (or YouTube channel)
      * Length of track
      * Platform ID
      * Link to where the track lives (either Spotify or YouTube)
  - Rewrite either platform track’s meta data into a singular format so each track’s meta data is consistent setup
  - Store user-associated track references 
      * Each track will not be stored music but pointing to the original platforms track
  - Create playlists that can include songs from those platforms
  - Add songs from either platform
  - Concatenate playlists from either platform into one larger playlist
  - Embed playback using official platform players (Spotify Web Playback SDK, YouTube iframe player). Each track plays on its native platform with user-initiated playback controls.
      * When a user plays a track, it plays on the platform that the track belongs to.
          ^ Example: Spotify track on the aggregated playlist is played on Spotify’s platform, but the interface is showing our platform.
  - Suggest tracks based on existing playlist content

### What the system does not:
  - Stream, host, download, cache, or store audio or video files
  - Provide automated playback transitions between Spotify and YouTube
      * Moving from a Spotify track to a YouTube track (or vice versa) requires explicit user action
  - Create a unified playback queue that automatically spans multiple platforms
  - Modify, write back to, or automatically sync changes to external platform playlists
      * Playlist imports are snapshot-based; changes on Spotify/YouTube do not automatically propagate
  - Control, skip, inject, or remove advertisements on external platforms
  - Train custom machine learning models or analyze raw audio/video data
      * AI suggestions use metadata-driven heuristics and existing platform APIs
  - Include offline support
  - Guarantee production-grade uptime, data permanence, or enterprise-level security
  - Support platforms beyond Spotify and YouTube in the current version

## Project Scope (Week 1 Lock)

### Supported Platforms
- Spotify
- Youtube
- (Potentially Apple Music)

### Included Features
- Metadata aggregation only
- Playlist creation using external links
- Unified Track model

### Explicitly Out of Scope
- Audio playback
- Playback controls
- AI-generated recommendations
- Additional music platforms (e.g., Apple Music)
