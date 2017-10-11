from Crypto.Cipher import AES
import base64

def decript(data):
    MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(str(data)))
    id = raw_decrypted.rstrip("\0")
    return id
