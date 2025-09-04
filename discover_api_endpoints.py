#!/usr/bin/env python3
"""
Script to demonstrate how to find and use HEOS API endpoints in PyHeos.

This script shows all the API endpoints used by the PyHeos library
and provides examples of how they are constructed and used.
"""

import sys
import os

# Add the pyheos package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyheos'))

from pyheos import const
from pyheos.connection import _encode_query


def print_section(title):
    """Print a section header."""
    print(f"\n{'=' * 60}")
    print(f" {title}")
    print('=' * 60)


def print_api_endpoints():
    """Print all API endpoints used in PyHeos."""
    
    print_section("HEOS CLI API ENDPOINT DISCOVERY")
    
    print(f"\n🔗 BASE CONNECTION INFO:")
    print(f"   Protocol: TCP")
    print(f"   Port: {const.CLI_PORT}")
    print(f"   Base URI: {const.BASE_URI}")
    print(f"   Command Format: {const.BASE_URI}<command>?<parameters>")
    
    print_section("BROWSE COMMANDS")
    browse_commands = [
        (const.COMMAND_BROWSE_GET_SOURCES, "Get available music sources"),
        (const.COMMAND_BROWSE_BROWSE, "Browse music source/container"),
        (const.COMMAND_BROWSE_PLAY_INPUT, "Play input source"),
        (const.COMMAND_BROWSE_PLAY_PRESET, "Play preset"),
        (const.COMMAND_BROWSE_PLAY_STREAM, "Play stream URL"),
        (const.COMMAND_BROWSE_ADD_TO_QUEUE, "Add to queue"),
    ]
    
    for command, description in browse_commands:
        print(f"   📁 {command:<35} - {description}")
    
    print_section("PLAYER COMMANDS")
    player_commands = [
        (const.COMMAND_GET_PLAYERS, "Get all players"),
        (const.COMMAND_GET_PLAYER_INFO, "Get player info"),
        (const.COMMAND_GET_PLAY_STATE, "Get play state"),
        (const.COMMAND_SET_PLAY_STATE, "Set play state"),
        (const.COMMAND_GET_NOW_PLAYING_MEDIA, "Get now playing"),
        (const.COMMAND_GET_VOLUME, "Get volume"),
        (const.COMMAND_SET_VOLUME, "Set volume"),
        (const.COMMAND_GET_MUTE, "Get mute state"),
        (const.COMMAND_SET_MUTE, "Set mute state"),
        (const.COMMAND_VOLUME_UP, "Volume up"),
        (const.COMMAND_VOLUME_DOWN, "Volume down"),
        (const.COMMAND_TOGGLE_MUTE, "Toggle mute"),
        (const.COMMAND_GET_PLAY_MODE, "Get play mode"),
        (const.COMMAND_SET_PLAY_MODE, "Set play mode"),
        (const.COMMAND_CLEAR_QUEUE, "Clear queue"),
        (const.COMMAND_GET_QUEUE, "Get queue"),
        (const.COMMAND_SAVE_QUEUE, "Save queue"),
        (const.COMMAND_PLAY_NEXT, "Play next"),
        (const.COMMAND_PLAY_PREVIOUS, "Play previous"),
        (const.COMMAND_PLAY_QUICK_SELECT, "Play quick select"),
        (const.COMMAND_SET_QUICK_SELECT, "Set quick select"),
        (const.COMMAND_GET_QUICK_SELECTS, "Get quick selects"),
    ]
    
    for command, description in player_commands:
        print(f"   🎵 {command:<35} - {description}")
    
    print_section("GROUP COMMANDS")
    group_commands = [
        (const.COMMAND_GET_GROUPS, "Get all groups"),
        (const.COMMAND_SET_GROUP, "Create/modify group"),
        (const.COMMAND_GET_GROUP_VOLUME, "Get group volume"),
        (const.COMMAND_SET_GROUP_VOLUME, "Set group volume"),
        (const.COMMAND_GET_GROUP_MUTE, "Get group mute"),
        (const.COMMAND_SET_GROUP_MUTE, "Set group mute"),
        (const.COMMAND_GROUP_TOGGLE_MUTE, "Toggle group mute"),
        (const.COMMAND_GROUP_VOLUME_UP, "Group volume up"),
        (const.COMMAND_GROUP_VOLUME_DOWN, "Group volume down"),
    ]
    
    for command, description in group_commands:
        print(f"   👥 {command:<35} - {description}")
    
    print_section("SYSTEM COMMANDS")
    system_commands = [
        (const.COMMAND_REGISTER_FOR_CHANGE_EVENTS, "Register for events"),
        (const.COMMAND_HEART_BEAT, "Heart beat"),
        (const.COMMAND_ACCOUNT_CHECK, "Check account"),
        (const.COMMAND_SIGN_IN, "Sign in"),
        (const.COMMAND_SIGN_OUT, "Sign out"),
    ]
    
    for command, description in system_commands:
        print(f"   ⚙️  {command:<35} - {description}")


def demonstrate_command_construction():
    """Demonstrate how HEOS commands are constructed."""
    
    print_section("COMMAND CONSTRUCTION EXAMPLES")
    
    # Example 1: Simple command with no parameters
    command1 = const.COMMAND_GET_PLAYERS
    params1 = {}
    uri1 = f"{const.BASE_URI}{command1}"
    print(f"   Simple command:")
    print(f"   Command: {command1}")
    print(f"   Full URI: {uri1}")
    
    # Example 2: Command with parameters
    command2 = const.COMMAND_SET_VOLUME
    params2 = {"pid": 123456789, "level": 50}
    query2 = _encode_query(params2)
    uri2 = f"{const.BASE_URI}{command2}?{query2}"
    print(f"\n   Command with parameters:")
    print(f"   Command: {command2}")
    print(f"   Parameters: {params2}")
    print(f"   Full URI: {uri2}")
    
    # Example 3: Command with special encoding
    command3 = const.COMMAND_BROWSE_PLAY_STREAM
    params3 = {"pid": 123456789, "url": "http://stream.example.com/radio"}
    query3 = _encode_query(params3)
    uri3 = f"{const.BASE_URI}{command3}?{query3}"
    print(f"\n   Command with URL parameter:")
    print(f"   Command: {command3}")
    print(f"   Parameters: {params3}")
    print(f"   Full URI: {uri3}")


def show_music_sources():
    """Show available music sources."""
    
    print_section("SUPPORTED MUSIC SOURCES")
    
    music_sources = [
        (const.MUSIC_SOURCE_PANDORA, "Pandora"),
        (const.MUSIC_SOURCE_RHAPSODY, "Rhapsody"),
        (const.MUSIC_SOURCE_TUNEIN, "TuneIn"),
        (const.MUSIC_SOURCE_SPOTIFY, "Spotify"),
        (const.MUSIC_SOURCE_DEEZER, "Deezer"),
        (const.MUSIC_SOURCE_NAPSTER, "Napster"),
        (const.MUSIC_SOURCE_IHEARTRADIO, "iHeartRadio"),
        (const.MUSIC_SOURCE_SIRIUSXM, "SiriusXM"),
        (const.MUSIC_SOURCE_SOUNDCLOUD, "SoundCloud"),
        (const.MUSIC_SOURCE_TIDAL, "Tidal"),
        (const.MUSIC_SOURCE_AMAZON, "Amazon Music"),
        (const.MUSIC_SOURCE_LOCAL_MUSIC, "Local Music"),
        (const.MUSIC_SOURCE_PLAYLISTS, "Playlists"),
        (const.MUSIC_SOURCE_HISTORY, "History"),
        (const.MUSIC_SOURCE_AUX_INPUT, "AUX Input"),
        (const.MUSIC_SOURCE_FAVORITES, "Favorites"),
    ]
    
    for source_id, name in music_sources:
        print(f"   🎶 {source_id:<4} - {name}")


def show_event_types():
    """Show supported event types."""
    
    print_section("REAL-TIME EVENT TYPES")
    
    print(f"   👤 PLAYER EVENTS:")
    for event in const.PLAYER_EVENTS:
        print(f"      • {event}")
    
    print(f"\n   👥 GROUP EVENTS:")
    print(f"      • {const.GROUP_EVENTS}")
    
    print(f"\n   🏠 HEOS SYSTEM EVENTS:")
    for event in const.HEOS_EVENTS:
        print(f"      • {event}")


def main():
    """Main function."""
    print("🎯 PYHEOS API ENDPOINT ANALYSIS")
    print("=" * 60)
    print("This script analyzes the PyHeos library to discover all")
    print("HEOS CLI API endpoints used for controlling HEOS devices.")
    
    print_api_endpoints()
    demonstrate_command_construction()
    show_music_sources()
    show_event_types()
    
    print_section("SUMMARY")
    print("   ✅ PyHeos uses the HEOS CLI Protocol over TCP")
    print(f"   ✅ Connects to port {const.CLI_PORT} on HEOS devices")
    print(f"   ✅ Uses base URI: {const.BASE_URI}")
    print("   ✅ Supports 4 main command categories:")
    print("      • Browse commands (6 endpoints)")
    print("      • Player commands (22 endpoints)")  
    print("      • Group commands (9 endpoints)")
    print("      • System commands (5 endpoints)")
    print("   ✅ Supports real-time events for device state changes")
    print("   ✅ Integrates with 16+ music services and local sources")
    
    print(f"\n📖 For complete documentation, see: API_ENDPOINTS_DOCUMENTATION.md")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()