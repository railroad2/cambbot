import os
import logging
import slack
import ssl as ssl_lib
import certifi
from camb_chat import CAMBChat

def camb_message(web_client: slack.WebClient, user_id: str, channel: str):
    camb_chat = CAMBChat(channel)

    # Get message payload 
    message_waiting = camb_chat.get_message_waiting()
    response = web_client.chat_postMessage(**message_waiting)

    message = camb_chat.get_message_payload()
    response = web_client.chat_postMessage(**message)
    print (response)


@slack.RTMClient.run_on(event="message")
def message(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if text and text.lower() == "camb":
        return camb_message(web_client, user_id, channel_id)

if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    camb_token = 'xoxb-828755631473-830450926915-t4JN4xEl1ydhtIf7gWSrnPHN'
    rtm_client = slack.RTMClient(token=camb_token, ssl=ssl_context)
    rtm_client.start()


