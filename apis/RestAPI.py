import ssl

import requests

print(ssl.OPENSSL_VERSION)

api_url = "http://localhost:8080/notification/updateTodaysFeed"


class NotificationModel:
    def __init__(self, feedId, headline, content):
        self.feedId = feedId
        self.headline = headline
        self.content = content

    def __str__(self):
        return f"{self.feedId}({self.headline})({self.content})"


notificationList = [{"headline": "CR7", "content": "won the world cup"}]

response = requests.post(url=api_url, json=notificationList, verify=False,
                         headers={"Content-Type": "application/json"})
print(response.json())

for x in response.json():
    del x['lastEditedDate']
    print(NotificationModel(**x))
# x = json.loads(response.json(), object_hook=lambda d: SimpleNamespace(**d))
# print(x)
