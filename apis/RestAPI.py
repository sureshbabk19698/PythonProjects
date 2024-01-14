import requests
import ssl

print(ssl.OPENSSL_VERSION)

api_url = "http://localhost:8080/notification/updateTodaysFeed"


class NotificationModel:
    def __init__(self, headline, content):
        self.headline = headline
        self.content = content


notificationList = [{"headline": "CR7", "content": "won the world cup"}]

response = requests.post(url=api_url, json=notificationList, verify=False,
                         headers={"Content-Type": "application/json"})
print(response.json())
