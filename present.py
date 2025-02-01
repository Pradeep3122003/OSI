import base64

def encode_message(message):
    print("[Layer 5-6] Encoding message...")
    return base64.b64encode(message.encode()).decode()

def decode_message(encoded_message):
    print("[Layer 5-6] Decoding message...")
    return base64.b64decode(encoded_message.encode()).decode()

if __name__ == "__main__":
    msg = "Hello, OSI Model!"
    encoded = encode_message(msg)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decode_message(encoded)}")
