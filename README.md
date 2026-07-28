# 🔐 Password Generator (Python)

A secure and flexible password generator written in Python.
Supports customizable password rules, encrypted local storage, and clipboard integration.

---

## 🚀 Features

* Generate one or multiple passwords
* Customizable length and quantity
* Support for:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Guarantees **at least one character of each selected type**
* Optional removal of confusing/specific symbols (banlist)
* Clipboard support (copy last generated password)
* **Encrypted password storage** using `Fernet` symmetric encryption
* Persistent encryption key (auto-generated on first run)
* JSON-based storage with add/load/delete operations

---

## 🧠 How It Works

The generator follows a secure and predictable algorithm:

1. Select active character sets based on user input
2. Remove banned characters from every selected set (if enabled)
3. Ensure at least **one character from each selected type**
4. Generate remaining characters randomly
5. Shuffle the final password using a cryptographically secure shuffle
6. Return the result

Generated passwords are then encrypted with a locally stored key before being saved to disk.

This guarantees:

* randomness 🔀
* compliance with password requirements 🔒
* passwords are never stored in plaintext 🗝️

---

## ⚙️ Installation

1. Clone the repository:

```
git clone <your-repo-url>
cd password-generator
```

2. Install dependencies:

```
pip install pyperclip cryptography
```

---

## ▶️ Usage

Run the script:

```
python main.py
```

Follow the prompts in the terminal:

* Set password length
* Choose character types
* Select number of passwords
* Optionally enable banlist filtering
* Optionally enable clipboard saving

On the first run, an encryption key file (`key`) will be generated automatically and reused on subsequent runs.

---

## 📋 Example Output

```
Your password(s): ['A9$dK2!xPq']
```

---

## ⚠️ Notes

* If multiple passwords are generated, **only the last one is copied to clipboard**
* Clipboard data may be accessible by other applications — use with caution
* If no character types are selected, the program will raise an error
* If all characters of a selected type are removed by the banlist, the program will raise an error instead of silently generating a weaker password
* If the generated password length is shorter than the number of required character types, the length is automatically increased with a warning
* The encryption key file must be kept private — anyone with access to it can decrypt all stored passwords
* Losing the key file makes all previously stored encrypted passwords permanently unreadable

---

## 🛡️ Security Considerations

* Uses Python's `secrets` module for cryptographically secure randomness (including shuffling)
* Avoids predictable patterns
* Supports filtering of ambiguous/banned characters
* Passwords are encrypted at rest using `Fernet` (AES-based symmetric encryption with built-in integrity checks)
* Encryption key is generated once and stored separately from the encrypted password file

---

## 📁 Project Structure

```
password-generator/
│
├── main.py         # Orchestrates the whole flow
├── generator.py    # Alphabet building + password generation logic
├── validate.py      # Input validation and constraint checks
├── ui.py            # Console input/output, clipboard, key file I/O
├── crypto.py        # Encryption/decryption (Fernet)
├── Storage.py        # JSON-based storage for encrypted passwords
├── key                # Auto-generated encryption key (keep private!)
├── password.json      # Encrypted password storage
└── README.md
```

---

## 💡 Future Improvements

* CLI arguments support (`--length`, `--digits`, etc.) 
* Passphrase generator (e.g. `apple-dog-sun`)
* Labeled password entries (e.g. save password under a name like "gmail")
* Search/filter saved passwords by label
* Command to rotate/reset the encryption key

---

## 👨‍💻 Author

Created as a learning project to improve Python skills, secure random generation, and basic applied cryptography.

---

## 📜 License

This project is open-source and free to use.
