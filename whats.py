import threading
from twilio.rest import Client

def send_whatsapp():
    account_sid = "your_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello! This is a threaded message.',
        to='whatsapp:+91_number'
    )
    print(f"Sent! SID: {message.sid}")

threading.Thread(target=send_whatsapp).start()
