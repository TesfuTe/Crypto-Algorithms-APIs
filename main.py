import uvicorn
from fastapi import FastAPI
from caesar_cipher import CaesarCipher


app = FastAPI()


@app.post("/caesar/encrypt")
def caesar_encrypt(text: str):
    cipher = CaesarCipher(text)
    return {"encrypted_text": cipher.encrypt()}


@app.post("/caesar/decrypt")
def caesar_decrypt(text: str):
    cipher = CaesarCipher(text)
    return {"decrypted_text": cipher.decrypt()}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
