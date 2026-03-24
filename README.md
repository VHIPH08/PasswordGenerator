# 🔐 Password Generator

A flexible and secure password generator built with Python.
Supports custom length, multiple passwords, character selection, and clipboard integration.

---

## 🚀 Features

* Generate one or multiple passwords
* Custom password length
* Choose character types:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Punctuation
* Optional exclusion of ambiguous characters (e.g. `O`, `0`, `l`, `1`)
* Automatic clipboard copy (for single password)
* Save passwords to a file
* Input validation with defaults
* Secure randomness using `secrets`

---

## 🧠 How It Works

The program follows a clean architecture pipeline:

```text
Input → Validation → Alphabet Creation → Password Generation → Output
```

Each step is handled by a separate function for better readability and scalability.

---

## ⚙️ Installation

1. Make sure you have Python 3 installed
2. Install required dependency:

```bash
pip install pyperclip
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

You will be prompted to enter:

* Password length (default: 12)
* Number of passwords (default: 1)
* Character types (Y/N):

  * Uppercase
  * Lowercase
  * Numbers
  * Symbols
* Whether to exclude ambiguous characters

---

## 📋 Example

```text
How long u wanna ur password be?(Default is 12) → 10
How many passwords u want?(Default is 1) → 2
Upper letters? → Y
Lower letters? → Y
Numbers? → Y
Punctuation? → N
Ban ambiguous characters? → Y
```

Output:

```text
Your passwords: ['aF8kLm2QpZ', 'X9vRt4BnQa']
```

---

## 📌 Notes

* If only one password is generated:

  * It is automatically copied to clipboard
  * Clipboard is cleared after 60 seconds
* If no character types are selected:

  * Program raises an error (`Alphabet is empty`)

---

## ⚠️ Limitations

* Validation still uses `input()` inside logic (can be improved)
* No CLI arguments yet (interactive only)
* No password strength indicator

---

## 🛠️ Future Improvements

* Add CLI arguments (`--length`, `--upper`, etc.)
* Password strength checker
* GUI version
* Custom word-based passwords
* Unit tests

---

## 📁 File Output

Passwords can be saved to:

```text
file.txt
```

Each password is written on a new line.

---
