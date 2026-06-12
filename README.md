# Python Program to Implement Data Security Using Binary Encoding and Machine Learning

A comprehensive data security solution that combines binary encoding techniques with machine learning-based threat detection to protect sensitive information.

## 📋 Overview

This project implements a multi-layered data security approach:
1. **Binary Encoding** - Convert data to secure binary representations
2. **Machine Learning Classification** - Detect anomalous/access patterns
3. **Encryption Layer** - Add cryptographic protection
4. **Threat Detection** - ML model identifies suspicious activities

## 🚀 Features

- ✅ Binary encoding/decoding for data transformation
- ✅ Machine Learning model for anomaly detection (Random Forest)
- ✅ AES encryption integration for additional security
- ✅ Real-time threat classification
- ✅ Data integrity verification using hashing
- ✅ Complete API for security operations

## 📦 Requirements

```bash
pip install numpy pandas scikit-learn cryptography hashlib
```

## 📁 Project Structure

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd data-security-ml
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the program:**
```bash
python data_security.py
```

## 🎯 Usage

### Basic Example

```python
from data_security import DataSecurity

# Initialize security system
security = DataSecurity()

# Encode data using binary encoding
original_data = "Sensitive Information"
encoded_data = security.binary_encode(original_data)
print(f"Encoded: {encoded_data}")

# Encrypt data
encrypted = security.encrypt_data(encoded_data)
print(f"Encrypted: {encrypted}")

# Detect threats using ML
threat_level = security.detect_threat("user_access_pattern")
print(f"Threat Level: {threat_level}")

# Decode and decrypt
decoded = security.binary_decode(encoded_data)
print(f"Decoded: {decoded}")
```

### Machine Learning Threat Detection

```python
from ml_model import ThreatDetector

# Initialize ML model
detector = ThreatDetector()

# Train model (if not already trained)
detector.train_model()

# Predict threat level
threat_score = detector.predict_threat({
    'access_frequency': 150,
    'failed_attempts': 5,
    'time_of_day': 3,
    'data_volume': 1024
})
print(f"Threat Score: {threat_score}")
```

## 🧪 Testing

```bash
python test_security.py
```

**Expected output:**
## 🔐 Security Features

### 1. Binary Encoding
- Converts text to binary representation
- Reversible encoding/decoding
- Adds obfuscation layer

### 2. AES Encryption
- 256-bit key strength
- CBC mode with padding
- Secure key generation

### 3. Hash Verification
- SHA-256 hashing
- Data integrity checks
- Tamper detection

### 4. ML Threat Detection
- Real-time anomaly classification
- Pattern-based detection
- Adaptive learning capability

## 🛡️ Security Best Practices

1. **Key Management:** Store encryption keys securely
2. **Model Updates:** Regularly update ML model with new patterns
3. **Access Logs:** Monitor and log all security operations
4. **Backup:** Keep encrypted backups of important data
5. **Testing:** Regular security auditing and testing

---

**Built with Python 3.7+**  
**Last Updated: June 2026**
