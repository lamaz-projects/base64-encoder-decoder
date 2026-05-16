import base64
import sys

def encode_text(plain_text):
    # Convert string to bytes, encode it, and convert back to string
    text_bytes = plain_text.encode('utf-8')
    encoded_bytes = base64.b64encode(text_bytes)
    return encoded_bytes.decode('utf-8')

def decode_text(encoded_text):
    try:
        # Convert string to bytes, decode it, and convert back to string
        encoded_bytes = encoded_text.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def main():
    print("=========================================")
    print("         BASE64 ENCODER / DECODER        ")
    print("=========================================")
    
    print("1. Encode plain text into Base64")
    print("2. Decode Base64 back into plain text")
    choice = input("\nSelect an option (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print("[-] Error: Invalid selection.")
        return

    user_input = input("Enter the text string: ").strip()

    # Handle edge case: empty input gracefully
    if not user_input:
        print("[-] Error: Input cannot be empty.")
        return

    if choice == '1':
        result = encode_text(user_input)
        print(f"\n[+] Encoded Base64 String:\n{result}")
    else:
        result = decode_text(user_input)
        if result is not None:
            print(f"\n[+] Decrypted/Decoded Plain Text:\n{result}")
        else:
            print("\n[-] Error: Invalid Base64 string provided.")
            
    print("=========================================")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Program terminated by user.")
        sys.exit()