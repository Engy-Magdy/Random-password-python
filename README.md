# 🔑 Random-Password-Generator

A customizable Python command-line application that generates secure random passwords based on specific user requirements for letters, numbers, and symbols.

## 🚀 Features
- **Precise Customization:** Allows the user to define the exact number of characters, letters, numerical digits, and special symbols they want in their password.
- **Mathematical Logic Validation:** Features a strict condition ensuring that the sum of all individual character types perfectly matches the total password length before execution.
- **Shuffled Output:** Uses Python's `random.shuffle` to ensure the generated characters are thoroughly mixed for better security.

## 🛠️ Built With
- **Python 3**
- Core Libraries: `random`, `string`

## 📋 How It Works
1. The program prompts the user for the total password length.
2. The user inputs the desired amount of letters, numbers, and symbols.
3. The system validates the input:
   - If the sum matches the total length, it generates and shuffles the password.
   - If there is a mismatch, it displays a clear validation error message.

## 💻 How to Run
Simply run the script using Python:
```bash
python password_generator.py
