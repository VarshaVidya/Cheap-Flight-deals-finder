from twilio.rest import Client

TWILIO_SID = "ACdd0fc058f24761e08e831694e9d31fdf"
TWILIO_AUTH_TOKEN = "f16ee4f5b0e8238de1f195d4fdb64326"
TWILIO_VIRTUAL_NUMBER = +13203498250
TWILIO_VERIFIED_NUMBER = +6596488793


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
