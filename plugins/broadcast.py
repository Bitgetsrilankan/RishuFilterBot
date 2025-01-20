
import datetime, time, asyncio
from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def pm_broadcast(bot, message):
    b_msg = await bot.ask(chat_id = message.from_user.id, text = "🎙️ Nᴏᴡ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ")
    try:
        users = await db.get_all_users()
        sts = await message.reply_text('🔁 Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Yᴏᴜʀ Mᴇssᴀɢᴇs..')
        start_time = time.time()
        total_users = await db.total_users_count()
        done = 0
        blocked = 0
        deleted = 0
        failed = 0
        success = 0
        async for user in users:
            if 'id' in user:
                pti, sh = await broadcast_messages(int(user['id']), b_msg)
                if pti:
                    success += 1
                elif pti == False:
                    if sh == "Blocked":
                        blocked += 1
                    elif sh == "Deleted":
                        deleted += 1
                    elif sh == "Error":
                        failed += 1
                done += 1
                if not done % 20:
                    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss:\n\nTᴏᴛᴀʟ Usᴇʀs: {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇss: {success}\nBʟᴏᴄᴋᴇᴅ: {blocked}\nDᴇʟᴇᴛᴇᴅ: {deleted}")    
            else:
                # Handle the case where 'id' key is missing in the user dictionary 
                done += 1
                failed += 1
                if not done % 20:
                    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss:\n\nTᴏᴛᴀʟ Usᴇʀs: {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇss: {success}\nBʟᴏᴄᴋᴇᴅ: {blocked}\nDᴇʟᴇᴛᴇᴅ: {deleted}")    
    
        time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
        await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ:\nCᴏᴍᴘʟᴇᴛᴇᴅ Iɴ {time_taken} Sᴇᴄᴏɴᴅs.\n\nTᴏᴛᴀʟ Usᴇʀs: {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇss: {success}\nBʟᴏᴄᴋᴇᴅ: {blocked}\nDᴇʟᴇᴛᴇᴅ: {deleted}")
    except Exception as e:
        print(f"error: {e}")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS))
async def broadcast_group(bot, message):
    b_msg = await bot.ask(chat_id = message.from_user.id, text = "🎙️ Nᴏᴡ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ")
    groups = await db.get_all_chats()
    sts = await message.reply_text(
        text='🔁 Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Yᴏᴜʀ Mᴇssᴀɢᴇs Tᴏ Gʀᴏᴜᴘs...'
    )
    start_time = time.time()
    total_groups = await db.total_chat_count()
    done = 0
    failed = 0

    success = 0
    async for group in groups:
        pti, sh = await broadcast_messages_group(int(group['id']), b_msg)
        if pti:
            success += 1
        elif sh == "Error":
                failed += 1
        done += 1
        if not done % 20:
            await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss:\n\nTᴏᴛᴀʟ Gʀᴏᴜᴘs: {total_groups}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_groups}\nSᴜᴄᴄᴇss: {success}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ:\nCᴏᴍᴘʟᴇᴛᴇᴅ Iɴ {time_taken} Sᴇᴄᴏɴᴅs.\n\nTᴏᴛᴀʟ Gʀᴏᴜᴘs: {total_groups}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_groups}\nSᴜᴄᴄᴇss: {success}")
        
