# Written by: Vladislav Mazur
# Contains: Notification Class and NotificationController Class
from data.data_controller.notification_data_controller import write_notification, read_notification


# connect to data.py to use its functions

# write classes

class Notification:
    id_count = 0

    # removed notification ID param due to it being
    # set in the initial constructor
    def __init__(self, event, account, notify_date, info):

        # make sure all inputs are valid
        if not isinstance(event, int):
            raise TypeError("Event ID must be an integer")
        if not isinstance(account, int):
            raise TypeError("Account ID must be an integer")
        # date being checked as string since there is no "time" format
        if not isinstance(notify_date, str) or len(notify_date) != 10:
            raise ValueError("Date must be a string in format yyyy-mm-dd")
        if not isinstance(info, str) or len(info) > 1000:
            raise ValueError("Info must be a string less than 1000 characters long")

        # if valid, initialize
        self.notify_id = Notification.genNoteID()
        self.event = event
        self.account = account
        self.notify_date = notify_date
        self.info = info

    # methods for notification class

    # Generate and get methods for the notification ID
    @classmethod
    def genNoteID(cls):
        cls.id_count += 1  # Increment ID counter for each new object
        return f"{cls.id_count}"  # Use ID counter to generate unique ID

    def getNoteID(self):
        return self.notify_id

    # grabs the event ID passed to it
    def getEventID(self):
        return self.event

    # grabs the account ID of the user
    def getAccountID(self):
        return self.account

    # grabs the date
    def getDate(self):
        return self.notify_date

    # grabs the info
    def getInfo(self):
        return self.info

    # if event id is an int, set event id
    def setEventID(self, eventID):
        if isinstance(eventID, int):
            self.event = eventID
        else:
            raise TypeError("Event ID must be an integer")

    # if account id is an int, set account id
    def setAccountID(self, accountID):
        if isinstance(accountID, int):
            self.account = accountID
        else:
            raise TypeError("Account ID must be an integer")

    # if date is a string with form "yyyy-mm-dd", set date
    def setDate(self, date):
        if isinstance(date, str) and len(date) == 10:
            self.notify_date = date
        else:
            raise ValueError("Date must be a string in format yyyy-mm-dd")

    # if info is a string and under 1000 characters, set info
    def setInfo(self, info):
        if isinstance(info, str) and len(info) < 1000:
            self.info = info
        else:
            raise ValueError("Info must be a string less than 1000 characters long")


class NotificationController:
    def __init__(self):
        self.notification = []

    # create a new notification object
    def createNotification(self, eventID, accountID, date, info):
        newNotification = Notification(eventID, accountID, date, info)
        result = write_notification(newNotification)
        if result[0]:
            self.notification.append(newNotification)
        return result

    # update an existing notification in the database
    def updateNotification(self, notification):
        result = write_notification(notification)
        if result[0]:
            count = self.notification.index(notification)
            self.notification[count] = notification
        return result

    # Read a notification from the database
    def readNotification(self, notificationID):
        notification = Notification("", 0, "", "")
        notification.notificationID = notificationID
        result = read_notification(notification)
        if result[0]:
            # update the notification object with the retrieved data
            notification.nType = result[1]
            notification.eventID = result[2]
            notification.accountID = result[3]
            notification.date = result[4]
            notification.info = result[5]
        return result, notification

    # deletes a specific notification based on it's ID
    def deleteNotification(self, notificationID):
        notification = Notification("", 0, "", "")
        notification.notificationID = notificationID
        for n in self.notification:
            if n.notificationID == notificationID:
                self.notification.remove(n)
                break
