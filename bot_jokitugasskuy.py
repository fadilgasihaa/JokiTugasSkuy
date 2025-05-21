from telethon import TelegramClient, events

# Konfigurasi API Telegram
api_id = 28493263
api_hash = '80fdcbe175839ab3542a719b51431ac9'
session = 'session_telegram'
client = TelegramClient(session, api_id, api_hash)

# Pastikan semua kata trigger dalam huruf kecil
trigger_words = ['segala bentuk penipuan', 'format']
target_thread_id = 432187 # Ganti dengan ID topik yang benar

@client.on(events.NewMessage(chats='@joki_tugas_skuy'))
async def handler(event):
    print("New message detected!")  # Log untuk mendeteksi pesan baru

    # Ambil ID thread dengan aman, fallback ke atribut lain jika perlu
    thread_id = getattr(event.message, 'message_thread_id',
                        getattr(event.message, 'thread_id', 432187))
    print(f"Thread ID: {thread_id}")  # Log ID thread

    if thread_id != target_thread_id:
        print("Thread ID tidak cocok. Pesan diabaikan.")
        return

    text = event.raw_text.lower()
    print(f"Message text: {text}")  # Log isi pesan

    if any(w in text for w in trigger_words):
        print("Trigger word detected!")  # Log jika kata kunci terdeteksi
        sender = await event.get_sender()
        print(f"Sending message to {sender.id}")  # Log ID pengirim
        await client.send_message(sender.id, 'Bisa dijelaskan tugasnya kak? -Zifa')

if __name__ == "__main__":
    try:
        print("Starting bot...")  # Log saat bot mulai
        client.start()
        print("Bot is running!")  # Log saat bot berjalan
        client.run_until_disconnected()
    except KeyboardInterrupt:
        print("Stopping bot...")  # Log saat bot dihentikan
    finally:
        print("Bot stopped.")  # Log saat bot benar-benar berhenti