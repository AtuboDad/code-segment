from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

class SM4:
    def __init__(self, key):
        self.key = key
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, plaintext):
        padded_text = pad(plaintext.encode(), AES.block_size)
        return self.cipher.encrypt(padded_text)

    def decrypt(self, ciphertext):
        decrypted_bytes = self.cipher.decrypt(ciphertext)
        return unpad(decrypted_bytes, AES.block_size).decode()

# 示例使用
if __name__ == '__main__':
    key = os.urandom(16)  # 生成16字节密钥
    sm4 = SM4(key)

    plaintext = "Hello, SM4 Encryption!"
    ciphertext = sm4.encrypt(plaintext)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = sm4.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")