from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("Disney_storeDan")
        await client.join_chat("suportdanuserbot")
        await client.join_chat("Userlogsbott")
    except BaseException:
        pass
