
import requests;

class SyntesisCrypto:

  @staticmethod
  def getSignature(text) -> str:
    link = 'https://hiring.api.synthesia.io/crypto/sign?message=' + text;
    response = requests.get(link, headers={
      'Authorization': '2a28f61683dd4bf970a084a407520c40'
    });
    if (response.status_code == 200):
      return response.content;
    else:
      raise Exception('Request to get signature failed with code: ' + str(response.status_code));

  @staticmethod
  def verifySignature(text, signature) -> bool:
    response = requests.get('https://hiring.api.synthesia.io/crypto/sign?message=' + text + '&signature=' + signature, {
      'Authorization': '2a28f61683dd4bf970a084a407520c40'
    });
    return response.status_code == 200
