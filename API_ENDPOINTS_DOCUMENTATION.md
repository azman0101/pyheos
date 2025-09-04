# HEOS CLI API Endpoints Used in PyHeos

## Overview

PyHeos is a Python library that controls HEOS (Denon's multi-room audio system) devices using the HEOS CLI Protocol. This document provides a comprehensive listing of all API endpoints used by the library.

## Connection Details

- **Protocol**: HEOS CLI Protocol over TCP connection
- **Base URI**: `heos://`
- **Port**: `1255` (CLI_PORT constant)
- **Command Format**: `heos://<command>?<parameters>`
- **Connection Method**: Direct TCP socket connection to HEOS devices on the local network
- **Response Format**: JSON

## API Command Categories

### 1. Browse Commands
Commands for discovering and browsing music sources and content.

| Endpoint | Purpose | Parameters |
|----------|---------|------------|
| `browse/get_music_sources` | Get available music sources (Spotify, Pandora, etc.) | None |
| `browse/browse` | Browse a music source or container | `sid` (source_id), `cid` (container_id), `range` |
| `browse/play_input` | Play the specified input source | `pid` (player_id), `spid` (source_player_id), `input` |
| `browse/play_preset` | Play a preset by 1-based index | `pid` (player_id), `preset` |
| `browse/play_stream` | Play a stream from URL | `pid` (player_id), `url` |
| `browse/add_to_queue` | Add container or track to queue | `pid` (player_id), `sid` (source_id), `cid` (container_id), `aid` (add_queue_option), `mid` (media_id) |

### 2. Player Commands
Commands for controlling individual HEOS players.

| Endpoint | Purpose | Parameters |
|----------|---------|------------|
| `player/get_players` | Get all available players | None |
| `player/get_player_info` | Get player information | `pid` (player_id) |
| `player/get_play_state` | Get player's current play state | `pid` (player_id) |
| `player/set_play_state` | Set player's play state (play/pause/stop) | `pid` (player_id), `state` |
| `player/get_now_playing_media` | Get currently playing media info | `pid` (player_id) |
| `player/get_volume` | Get player volume level | `pid` (player_id) |
| `player/set_volume` | Set player volume level (0-100) | `pid` (player_id), `level` |
| `player/get_mute` | Get player mute state | `pid` (player_id) |
| `player/set_mute` | Set player mute state | `pid` (player_id), `state` (on/off) |
| `player/volume_up` | Increase volume by step | `pid` (player_id), `step` (1-10) |
| `player/volume_down` | Decrease volume by step | `pid` (player_id), `step` (1-10) |
| `player/toggle_mute` | Toggle mute state | `pid` (player_id) |
| `player/get_play_mode` | Get repeat and shuffle modes | `pid` (player_id) |
| `player/set_play_mode` | Set repeat and shuffle modes | `pid` (player_id), `repeat`, `shuffle` |
| `player/clear_queue` | Clear player's queue | `pid` (player_id) |
| `player/get_queue` | Get player's queue contents | `pid` (player_id), `range` |
| `player/save_queue` | Save queue as playlist | `pid` (player_id), `name` |
| `player/play_next` | Skip to next track | `pid` (player_id) |
| `player/play_previous` | Skip to previous track | `pid` (player_id) |
| `player/play_quickselect` | Play a quick select preset | `pid` (player_id), `id` (1-6) |
| `player/set_quickselect` | Set a quick select preset | `pid` (player_id), `id` (1-6) |
| `player/get_quickselects` | Get all quick select presets | `pid` (player_id) |

### 3. Group Commands
Commands for controlling HEOS player groups (multi-room audio).

| Endpoint | Purpose | Parameters |
|----------|---------|------------|
| `group/get_groups` | Get all player groups | None |
| `group/set_group` | Create, modify, or ungroup players | `pid` (comma-separated player_ids) |
| `group/get_volume` | Get group volume level | `gid` (group_id) |
| `group/set_volume` | Set group volume level | `gid` (group_id), `level` |
| `group/get_mute` | Get group mute state | `gid` (group_id) |
| `group/set_mute` | Set group mute state | `gid` (group_id), `state` |
| `group/toggle_mute` | Toggle group mute state | `gid` (group_id) |
| `group/volume_up` | Increase group volume | `gid` (group_id), `step` |
| `group/volume_down` | Decrease group volume | `gid` (group_id), `step` |

### 4. System Commands
Commands for system-level operations and account management.

| Endpoint | Purpose | Parameters |
|----------|---------|------------|
| `system/register_for_change_events` | Enable/disable event notifications | `enable` (on/off) |
| `system/heart_beat` | Send heart beat to keep connection alive | None |
| `system/check_account` | Check if HEOS account is signed in | None |
| `system/sign_in` | Sign in to HEOS account | `un` (username), `pw` (password) |
| `system/sign_out` | Sign out of HEOS account | None |

## Event Types
The API also supports real-time events that are received automatically:

### Player Events
- `event/player_state_changed` - Player play state changed
- `event/player_now_playing_changed` - Currently playing media changed  
- `event/player_now_playing_progress` - Playback progress updates
- `event/player_volume_changed` - Player volume changed
- `event/player_playback_error` - Playback error occurred
- `event/player_queue_changed` - Player queue changed
- `event/repeat_mode_changed` - Repeat mode changed
- `event/shuffle_mode_changed` - Shuffle mode changed

### Group Events
- `event/group_volume_changed` - Group volume changed

### HEOS System Events
- `event/sources_changed` - Available music sources changed
- `event/players_changed` - Available players changed
- `event/groups_changed` - Player groups changed
- `event/user_changed` - User account status changed

## Music Sources
The API supports various music services and sources:

| Source ID | Service Name |
|-----------|--------------|
| 1 | Pandora |
| 2 | Rhapsody |
| 3 | TuneIn |
| 4 | Spotify |
| 5 | Deezer |
| 6 | Napster |
| 7 | iHeartRadio |
| 8 | SiriusXM |
| 9 | SoundCloud |
| 10 | Tidal |
| 13 | Amazon Music |
| 1024 | Local Music |
| 1025 | Playlists |
| 1026 | History |
| 1027 | AUX Input |
| 1028 | Favorites |

## Input Sources
Supported physical input types for HEOS devices:

- AUX inputs (aux_in_1, aux_in_2, etc.)
- Line inputs (line_in_1, line_in_2, etc.) 
- HDMI inputs (hdmi_in_1, hdmi_in_2, etc.)
- Digital inputs (coax_in_1, optical_in_1, etc.)
- Analog inputs (analog_in_1, phono, etc.)
- Media inputs (cd, tuner, dvd, etc.)

## Example Command Usage

```python
import pyheos

# Connect to a HEOS device
heos = pyheos.Heos('192.168.1.100')
await heos.connect()

# Get all players - calls heos://player/get_players
players = await heos.get_players()

# Set volume - calls heos://player/set_volume?pid=123456789&level=50
await players[player_id].set_volume(50)

# Play Spotify - calls heos://browse/browse?sid=4
sources = await heos.get_music_sources()
spotify = sources[4]  # Spotify source ID
content = await spotify.browse()

await heos.disconnect()
```

## Connection Implementation Details

The library establishes a persistent TCP connection to port 1255 on the HEOS device and:
1. Sends commands as URI strings terminated with `\r\n`
2. Receives JSON responses with matching command names
3. Uses sequence numbers to match requests with responses
4. Automatically handles reconnection and heartbeat
5. Processes real-time events for device state changes

This comprehensive API enables full control of HEOS multi-room audio systems including playback control, volume management, grouping, and content browsing from various music services.