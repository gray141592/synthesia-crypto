from message import Message

class Controllers:
  @staticmethod
  def getMessageSignature(messageText) -> str:
    message = Message(messageText);
    if (message.was_customer_notified()):
      return message.signature;
    return 'Signature currently unavailable';