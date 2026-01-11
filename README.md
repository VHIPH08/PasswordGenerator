# Password Generator

Password generator written in Python.

## Description
This project generates random passwords with different difficulty levels.
It is designed for learning purposes and demonstrates working with strings,
random generation and basic class design.

The generator can create multiple passwords at once and save them to a file.

## Features
- Three difficulty levels:
  - easy
  - middle
  - hard
- Custom number of generated passwords
- Uses secure random generation (`secrets`)
- Avoids ambiguous characters in hard mode
- Saves generated passwords to a text file

## Difficulty levels
- **easy**
  - Length: 4–7
  - Letters and digits
- **middle**
  - Length: 8–11
  - Printable characters
- **hard**
  - Length: 12–29
  - Letters, digits and special symbols
  - Excludes ambiguous characters (0, O, l, I, etc.)

## Project structure
password_generator/
├── password_generator.py
└── README.md

## Usage
```python
from password_generator import PasswordGenerator

generator = PasswordGenerator("hard", 5)
passwords = generator.password_gen()
generator.password_saver(passwords)
