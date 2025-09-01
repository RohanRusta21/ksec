ksec

A CLI tool to encrypt secrets for Kubernetes YAML files, compatible with Helm and standard manifests.

Installation

Install ksec using pip:

pip install ksec

Prerequisites





Python 3.8 or higher



pip for installing Python packages

Usage

Generate an Encryption Key

ksec generate-key

Output: A base64-encoded key (e.g., AgrB1X...==).

Warning: Store this key securely (e.g., in a password manager or KMS). Do not commit it to version control.

Encrypt a Secret

Encrypt a secret value for use in Kubernetes or Helm YAML files:

ksec encrypt --value "my-super-secret" --key "AgrB1X...==" --output-format yaml-snippet

Output:

encryptedSecret: gAAAAABm...

Options:





--value: The secret to encrypt (prompts if not provided).



--key: The base64-encoded key (prompts if not provided).



--output-format: plain (default), base64, or yaml-snippet.

Example: Kubernetes Secret

Add the encrypted secret to a Kubernetes Secret:

apiVersion: v1
kind: Secret
metadata:
  name: my-secret
data:
  api-key: gAAAAABm...

Example: Helm values.yaml

Add to values.yaml:

myApp:
  apiKey: gAAAAABm...

Deploy with Helm:

helm install my-release ./charts

Decryption

Your application must decrypt the secret using the same key. Example in Python:

from cryptography.fernet import Fernet

key = "AgrB1X...=="  # Securely injected
encrypted_secret = "gAAAAABm..."
fernet = Fernet(key)
decrypted = fernet.decrypt(encrypted_secret.encode()).decode()
print(decrypted)  # Outputs: my-super-secret

Security Notes





Key Management: Use a secure method (e.g., AWS KMS, environment variables) to store and access the encryption key.



Symmetric Encryption: ksec uses Fernet (AES-128 with HMAC). For production, consider integrating with a Kubernetes controller or KMS for better security.

Support

File issues on GitHub or reach out on X with #ksec.

License

MIT
