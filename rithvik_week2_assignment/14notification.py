from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("email notification")
class SmsNotification(Notification):
    def send(self):
        print("SMS Notification")
email_notification=EmailNotification()
email_notification.send()
Sms_Notification=SmsNotification()
Sms_Notification.send()
