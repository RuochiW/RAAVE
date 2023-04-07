# Written by: Vladislav Mazur
# Contains: Notification Class and NotificationController Class
from data.data_controller.notification_data_controller import write_notification, read_notification
from src.notifications import Notification


def read_user_notification(notify_id):
    notification = Notification("", "", 0, "", "")
    notification.notify_id = notify_id
    result = read_notification(notification)
    if result[0]:
        # update the notification object with the retrieved data
        notification.nType = result[1]
        notification.eventID = result[2]
        notification.accountID = result[3]
        notification.date = result[4]
        notification.info = result[5]
    return notification


class NotificationController:
    def __init__(self):
        self.notification = []

    # create a new notification object
    def create_notification(self, event, account, date, info):
        notification = Notification(None, event, account, date, info)
        result = write_notification(notification)
        if result[0]:
            self.notification.append(notification)
        return result

    # update an existing notification in the database
    def update_notification(self, notification):
        result = write_notification(notification)
        if result[0]:
            count = self.notification.index(notification)
            self.notification[count] = notification
        return result

    # Read a notification from the database

    # deletes a specific notification based on it's ID
    def delete_notification(self, notify_id):
        notification = Notification("", "", 0, "", "")
        notification.notify_id = notify_id
        for notification in self.notification:
            if notification.notify_id == notify_id:
                self.notification.remove(notification)
                break
