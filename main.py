from webserver import keep_alive
import requests

channelID = 976715801631526912
headers = {
    "authorization":
    "OTc2NzE1ODAxNjMxNTI2OTEy.GI-gfz.v-WezM5sLeaOahba8lpeW5GK4-P9tk5q0UC4Yo"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
