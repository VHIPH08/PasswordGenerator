# 🔐 Password Generator (Python)

A secure and flexible password generator written in Python.
Supports customizable password rules, multiple outputs, and clipboard integration.

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
* Save passwords to a file

---

## 🧠 How It Works

The generator follows a secure and predictable algorithm:

1. Select active character sets based on user input
2. Ensure at least **one character from each selected type**
3. Generate remaining characters randomly
4. Shuffle the final password for better randomness
5. Return the result

This guarantees both:

* randomness 🔀
* compliance with password requirements 🔒

---

## ⚙️ Installation

1. Clone the repository:

```
git clone <your-repo-url>
cd password-generator
```

2. Install dependencies:

```
pip install pyperclip
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
* Optionally enable clipboard saving

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

---

## 🛡️ Security Considerations

* Uses Python's `secrets` module for cryptographically secure randomness
* Avoids predictable patterns
* Supports filtering of ambiguous characters

---

## 📁 Project Structure

```
password-generator/
│
├── main.py
├── passwords.txt
└── README.md
```

---

## 💡 Future Improvements

* CLI arguments support (`--length`, `--digits`, etc.) done
* Passphrase generator (e.g. `apple-dog-sun`)
* GUI interface
* Custom user-defined character sets

---

## 👨‍💻 Author

Created as a learning project to improve Python skills and understanding of secure random generation.

---

## 📜 License

This project is open-source and free to use.
