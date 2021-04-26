from typing import List

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from example01_slack_msg.SlackConversation import SlackConversation


class SlackController:
    def __init__(self, token):
        self.client: WebClient = None
        try:
            self.client = WebClient(token)
            self.status = self.client.api_test()
            self.conversations: List[SlackConversation] = self.list_channels()
        except SlackApiError as e:
            self.status = e.response.data

    def list_channels(self):
        response = self.client.conversations_list()
        print(response.data)
        channels = response.data['channels']
        listed_channels = []
        for channel in channels:
            print(channel)
            listed_channels.append(SlackConversation(channel['id'], channel['name'], channel['is_channel']))
        return listed_channels

    def send_msg_to_channel(self, msg, channel_id):
        try:
            result = self.client.chat_postMessage(channel=channel_id, text=msg)
            print(result)

        except SlackApiError as e:
            print(f"Error posting message: {e}")