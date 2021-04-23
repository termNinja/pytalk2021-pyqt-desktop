from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackMsgDispatcher:
    def __init__(self, token):
        self.client = WebClient(token)

    def list_channels(self):
        return ['A', 'B', 'C']

    def send_msg_to_channel(self, msg, channel_id):
        try:
            # Call the chat.postMessage method using the WebClient
            result = self.client.chat_postMessage(channel=channel_id, text=msg)

            print(result)

        except SlackApiError as e:
            print(f"Error posting message: {e}")