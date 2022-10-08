try {
class ExampleProtocol(protocol.Protocol):
def dataReceived(self, data):

def confirmAuth(self, headers):
try:
token = cPickle.loads(base64.b64decode(headers['AuthToken']))
if not check_hmac(token['signature'], token['data'], getSecretKey()):
raise AuthFail
self.secure_data = token['data']
except:
raise AuthFail
}
