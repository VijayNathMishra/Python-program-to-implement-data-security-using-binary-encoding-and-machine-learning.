#Write a Python program to implement data security using binary encoding and machine learning.
from sklearn.tree import DecisionTreeClassifier

# Function to convert text into binary
def text_to_binary(text):
    binary_data = ' '.join(format(ord(char), '08b') for char in text)
    return binary_data

# User input
message = input("Enter a message: ")

# Convert message to binary
binary_message = text_to_binary(message)

print("\nOriginal Message:", message)
print("Binary Encoded Message:", binary_message)

# Sample dataset for security classification
# 0 = Safe, 1 = Threat
X = [
    [10, 0],   # Safe
    [20, 0],   # Safe
    [30, 1],   # Threat
    [40, 1],   # Threat
    [15, 0],   # Safe
    [35, 1]    # Threat
]

y = [0, 0, 1, 1, 0, 1]

# Train Machine Learning Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Use binary length and special flag as features
binary_length = len(binary_message)

# Example feature:
# 0 = normal message
# 1 = suspicious message
flag = int(input("\nEnter security flag (0=Safe, 1=Suspicious): "))

prediction = model.predict([[binary_length, flag]])

print("\nSecurity Analysis Result:")
if prediction[0] == 0:
    print("Message Classified as SAFE")
else:
    print("Message Classified as THREAT")



    import numpy as np
import pandas as pd
import time
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# =====================================================================
# 1. BINARY ENCRYPTION LAYER (XOR Encryption)
# =====================================================================
def xor_encrypt_decrypt(data: str, key: str) -> str:
    """
    Encrypts or decrypts data using a binary XOR operation.
    Applying XOR twice with the same key returns the original plaintext.
    """
    result = []
    key_length = len(key)
    for i, char in enumerate(data):
        # Perform XOR between the binary representation of the char and key char
        xor_char = chr(ord(char) ^ ord(key[i % key_length]))
        result.append(xor_char)
    return "".join(result)


# =====================================================================
# 2. MACHINE LEARNING LAYER (Anomalous Decryption/Brute-Force Detector)
# =====================================================================
def generate_mock_traffic_data():
    """
    Generates synthetic data representing decryption attempts.
    Features: [attempt_frequency (Hz), failed_attempts_in_row, avg_time_diff (ms)]
    Labels: 0 = Normal User, 1 = Brute-Force Attack
    """
    data = []
    
    # Generate Normal User Traffic (Low frequency, few failures)
    for _ in range(100):
        frequency = random.uniform(0.1, 1.5)
        failures = random.randint(0, 2)
        time_diff = random.uniform(500, 2000)
        data.append([frequency, failures, time_diff, 0])
        
    # Generate Brute-Force Traffic (High frequency, many failures, rapid succession)
    for _ in range(100):
        frequency = random.uniform(10.0, 50.0)
        failures = random.randint(5, 20)
        time_diff = random.uniform(10, 80)
        data.append([frequency, failures, time_diff, 1])
        
    df = pd.DataFrame(data, columns=['frequency', 'failures', 'time_diff', 'is_attack'])
    return df

def train_ids_model():
    """Trains a Random Forest to detect malicious decryption behaviors."""
    df = generate_mock_traffic_data()
    X = df[['frequency', 'failures', 'time_diff']]
    y = df['is_attack']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    return model


# =====================================================================
# 3. SIMULATION RUNNER
# =====================================================================
if __name__ == "__main__":
    print("--- Step 1: Initializing Binary Encryption ---")
    secret_message = "Confidential: Launch codes are 42-X-99"
    secret_key = "SuperSecretKey"
    
    # Encrypting
    encrypted_message = xor_encrypt_decrypt(secret_message, secret_key)
    print(f"Original:  {secret_message}")
    print(f"Encrypted (Raw Binary/Chars): {repr(encrypted_message)}")
    
    # Decrypting with correct key
    decrypted_message = xor_encrypt_decrypt(encrypted_message, secret_key)
    print(f"Decrypted: {decrypted_message}\n")

    print("--- Step 2: Training ML Intrusion Detection System ---")
    ids_model = train_ids_model()
    print("IDS Model trained successfully dynamically monitoring traffic...\n")

    print("--- Step 3: Simulating Traffic & ML Detection ---")
    
    # Scenario A: Legitimate User trying to decrypt
    # Low frequency (0.5 requests/sec), 0 previous failures, 1200ms delay
    normal_traffic_pattern = np.array([[0.5, 0, 1200.0]])
    normal_pred = ids_model.predict(normal_traffic_pattern)[0]
    
    print(f"Simulation A (Legitimate User Decryption Attempt):")
    if normal_pred == 1:
        print("ALERT: Access Denied. Malicious activity detected by ML.")
    else:
        print(f"Access Granted. Decrypted Data: {xor_encrypt_decrypt(encrypted_message, secret_key)}")
        
    print("-" * 40)

    # Scenario B: Hacker attempting a Brute-Force Attack
    # High frequency (35 requests/sec), 12 previous failures, 15ms delay
    attack_traffic_pattern = np.array([[35.0, 12, 15.0]])
    attack_pred = ids_model.predict(attack_traffic_pattern)[0]
    
    print(f"Simulation B (Brute-Force Script Decryption Attempt):")
    if attack_pred == 1:
        print("🚨 ALERT: Threat Detected! Machine Learning blocked this decryption request. System locked.")
    else:
        # This shouldn't execute if ML is working correctly
        print(f"Access Granted. Decrypted Data: {xor_encrypt_decrypt(encrypted_message, 'WrongKey')}")
        print("Warning: Decryption succeeded with wrong key! Potential vulenerability detected.")
        
