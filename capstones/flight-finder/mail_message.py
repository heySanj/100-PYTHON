import smtplib

class Email():
    """Create an Email object"""   
            
    def __init__(self, username="", password="", smtp_server="smtp.gmail.com", port=587, sender="", recipient="", subject="", message=""):
        
        # Login Details and recipient
        self.username = username 
        self.password = password # Might need to generate an app password with your Email provider
        self.smtp_server = smtp_server
        self.port = port
        self.sender = sender
        self.recipient = recipient
        
        # Message
        self.subject = subject
        self.message_text = message
        
    def send(self):
        # Create Message from all the different parts
        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (self.sender, self.recipient, self.subject, self.message_text)
        
        try:
            with smtplib.SMTP(self.smtp_server, port=self.port) as connection: # Establish connection
                connection.starttls() # Encryption of the email
                connection.login(user=self.username,password=self.password) # Login
                connection.sendmail(from_addr=self.username, to_addrs=self.recipient, msg=msg) # Send the email
                connection.close()  # Close the connection
                print("The email was sent successfully.")
        except Exception as error:
            print(f"Could not send the email. \nError: {error}")