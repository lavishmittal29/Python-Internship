from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("Email Sent Successfully.")
class SMSNotification(Notification):
    def send(self):
        print("SMS Sent Successfully.")
class WhatsAppNotification(Notification):
    def send(self):
        print("WhatsApp Message Sent Successfully.")

email=EmailNotification()
sms=SMSNotification()
whatsapp=WhatsAppNotification()

email.send()
sms.send()
whatsapp.send()