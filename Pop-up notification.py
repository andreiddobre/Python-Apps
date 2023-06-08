#pip install time

import time
from plyer import notification

if __name__ == '__main__':
        while True:
                notification.notify(
                        title = "ALERT!",
                        message = "Time to take a break!",
                        timeout = 10
                        )
                time.sleep(3600)

#original code inspired by clcoding.com
