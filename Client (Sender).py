import socket
import ssl
import json

def send_secure_object(data_object, host='127.0.0.1', port=8443):
    # 1. Create a standard TCP Socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Configure SSL/TLS Context for a client
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # Since we are using a self-signed testing certificate, we disable strict CA chain validation.
    # IN PRODUCTION: Keep this enabled and load a verified CA certificate.
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Wrap the socket into a secure TLS configuration
    secure_socket = context.wrap_socket(raw_socket, server_hostname=host)

    try:
        # Connect over the secure network tunnel
        secure_socket.connect((host, port))
        print(f"[+] Secured network tunnel open to {host}:{port}")

        # 3. Serialize the Python data object into a JSON string byte-stream
        serialized_payload = json.dumps(data_object).encode('utf-8')

        # Transmit the data across the encrypted line
        print("[*] Transmitting encrypted data object...")
        secure_socket.sendall(serialized_payload)

        # Receive validation back from the receiving endpoint
        server_reply = secure_socket.recv(4096).decode('utf-8')
        print(f"[Server Response]: {server_reply}")

    except Exception as e:
        print(f"[!] Network Connection Failure: {e}")
    finally:
        secure_socket.close()
        print("[*] Secure socket closed.")

if __name__ == "__main__":
    # Define a complex structured object to send
    transaction_object = {
        "user_id": 99214,
        "action": "TRANSFER",
        "amount": 2500.50,
        "currency": "USD",
        "verified": True,
        "meta_tags": ["mobile_app", "external_api", "auth_level_2"]
    }
    
    send_secure_object(transaction_object)
