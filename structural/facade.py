'''
Facade

Provides a high-level, simplified interface that hides the complexities of the underlying system. It delegates client requests to appropriate objects within the subsystem but does not add any additional behaviour or functionality. It's purpose is to simplify access.

Facade vs Proxy:
- Facade provides a simplified interface to a complex subsystem, which can involve many classes and functions. It delegates but does not add any additional behaviours or functionality.
- Proxies generally control access to one other object and allow additional behaviour or restrictions to be applied when accessing the target. It's purpose is not to hide complexity, even if it might.

Example:
- Example 1 shows a class that has been created to handle files, abstracting away the complexities of the os module and providing simple, intuitive methods to manage the file.
- Example 2 shows a notification class, which ensures all the notification classes and their methods are called, without the user needing to know separate classes exist.
'''

import os

# Example 1


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def exists(self):
        return os.path.exists(self.file_path)

    def create(self):
        with open(self.file_path, 'w'):
            pass

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)

    def delete(self):
        os.remove(self.file_path)


# Example 2

class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class SMSService:
    def send_sms(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class PushNotificationService:
    def send_push_notification(self, recipient, message):
        print(f"Sending push notification to {recipient}: {message}")


class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
        self.push_notification_service = PushNotificationService()

    def send_notification(self, recipient, message):
        self.email_service.send_email(recipient, message)
        self.sms_service.send_sms(recipient, message)
        self.push_notification_service.send_push_notification(
            recipient, message)
