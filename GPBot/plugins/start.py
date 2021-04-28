from GPBot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for @epusthakalaya_bots and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("🎛HELP & COMMANDS🎛", data="help")],
        [Button.url("🗳SUPPORT US🗳", "https://t.me/epusthakalaya_bots")]])
       return

    if event.is_group:
       await event.reply("**I am alive 24/7!**")
       return
