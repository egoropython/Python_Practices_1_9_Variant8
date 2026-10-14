class ConsoleNotifier:
    def send(self, message): print("[УВЕДОМЛЕНИЕ]", message)
class ListNotifier:
    def __init__(self): self.messages=[]
    def send(self, message): self.messages.append(message)
