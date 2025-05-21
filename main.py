import os
from telethon import TelegramClient, events
from keep_alive import keep_alive

# Mulai web server health-check
keep_alive()

# Baca konfigurasi dari env vars
api_id      = int(os.getenv('TELEGRAM_API_ID', '0'))
api_hash    = os.getenv('TELEGRAM_API_HASH', '')
session     = os.getenv('TELEGRAM_SESSION', 'session_telegram')
trigger_raw = os.getenv('TRIGGER_WORDS', 'segala bentuk penipuan,format')
target_thread_id = int(os.getenv('TARGET_THREAD_ID', '32187'))

# Split comma-separated kata trigger jadi list
trigger_words = [w.strip().lower() for w in trigger_raw.split(',')]

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(chats='@joki_tugas_skuy'))
async def handler(event):
    thread_id = getattr(event.message, 'message_thread_id',
                        getattr(event.message, 'thread_id', target_thread_id))
    if thread_id != target_thread_id:
        return
    text = event.raw_text.lower()
    if any(w in text for w in trigger_words):
        sender = await event.get_sender()
        await client.send_message(sender.id, 'Bisa dijelaskan tugasnya kak? -Zifa')

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
