def send_whatsapp_twilio():
    """
    Send WhatsApp message using Twilio WhatsApp API
    Requires: pip install twilio
    """
    try:
        from twilio.rest import Client
        
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            body='Hello from Python! 🐍 This is an automated WhatsApp message.',
            from_='whatsapp:+14155238886',  # Twilio Sandbox number
            to='whatsapp:+1234567890'       # Recipient's WhatsApp number
        )
        
        print(f"WhatsApp message sent: {message.sid}")
        return message.sid
        
    except Exception as e:
        print(f"Error sending WhatsApp: {e}")
