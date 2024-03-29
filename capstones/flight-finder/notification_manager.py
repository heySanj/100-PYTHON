from twilio.rest import Client
import os
from mail_message import Email

# from twilio.http.http_client import TwilioHttpClient
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ.get("TWILIO_SID")
        auth_token = os.environ.get("TWILIO_AUTH")

        self.SEND_NUMBER = os.environ.get("TWILIO_NUMBER")
        self.TO_NUMBER = os.environ.get("PH_NUM")

        self.client = Client(account_sid, auth_token)
        
        self.EMAIL_USER = os.environ.get("EMAIL_USER")
        self.EMAIL_PASS = os.environ.get("EMAIL_PASS")
        self.SENDER = ""
        

    def send_sms(self, message):

        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        # client = Client(account_sid, auth_token, http_client=proxy_client)

        message = self.client.messages \
                    .create(
                            body=message,
                            from_= self.SEND_NUMBER,
                            to= self.TO_NUMBER
                        )
        print(message.status)
        
    def send_email(self, recipient, subject, message):    
        new_email = Email(
            username=self.EMAIL_USER,
            password=self.EMAIL_PASS,
            sender=self.SENDER,
            recipient=recipient,
            subject=subject,
            message=message
        )    
        # Send it
        new_email.send()