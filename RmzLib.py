import pyaes

class ramznegari():
    def __init__(self):
        self.key = "Saeid_javadi_uSpSaeid_Javadi_USP"
        self.key = self.key.encode('utf-8')


    def enccc(self,plaintext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        ciphertext = aes.encrypt(plaintext.encode("utf8"))
        # print(ciphertext)
        return ciphertext


    def deccc(self,ciphertext):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypted = aes.decrypt(ciphertext).decode('utf-8')
        return decrypted
