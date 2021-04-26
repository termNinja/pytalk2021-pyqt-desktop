class SlackConversation:
    def __init__(self, id: str, name: str, is_channel: bool):
        self.id = id
        self.name = name
        self.is_channel = is_channel

    def __repr__(self):
        return f"<id={self.id} name={self.name} is_channel={self.is_channel}>"