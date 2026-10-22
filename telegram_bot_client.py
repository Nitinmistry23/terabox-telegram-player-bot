#!/usr/bin/env python3
"""
TeraVideo Telegram Bot Integration Client
Connects to @TeraVideoPlayBot ecosystem.
Website: https://teravideo.in/
"""

BOT_HANDLE = "@TeraVideoPlayBot"
BOT_WEB_PLAYER = "https://teravideo.in/telegram-player/"

def print_bot_info():
    print("=" * 60)
    print("🤖 TeraVideo Telegram Player Bot:", BOT_HANDLE)
    print("🌐 Dedicated Web Player Page   :", BOT_WEB_PLAYER)
    print("=" * 60)
    print("How to use:")
    print("1. Open Telegram and search for", BOT_HANDLE)
    print("2. Send any TeraBox / 1024Tera / TeraShare link.")
    print("3. Receive instant in-browser streaming player link.")
    print("=" * 60)

if __name__ == "__main__":
    print_bot_info()\n