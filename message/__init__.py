from syntesis_api import SyntesisCrypto;

class Message:

  def __init__(self, text) -> None:
      self.text = text;
      try:
        self.signature = SyntesisCrypto.getSignature(text);
        self.customer_notified = True;
      except Exception as e:
        self.customer_notified = False;

  def update_signature(self, signature) -> None:
    signature_verified = SyntesisCrypto.verifySignature(self.text, signature);
    if (signature_verified):
      self.signature = signature;
    else:
      raise Exception('Signature for message not valid');

  def notify_customer(self) -> None:
    self.customer_notified = True;

  def was_customer_notified(self) -> bool:
    return self.customer_notified == True;
