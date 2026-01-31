# 🔐 Password Generator (Python)

This project is a **simple password generator written in Python**. It allows you to generate a random password and optionally save it along with a username, description, and creation date/time into a text file.

---

## ✨ Features

* Generate random passwords using:

  * Uppercase and lowercase English letters
  * Numbers
  * Symbols
* User-defined password length
* Save generated passwords to `password.txt`
* Store creation date and time
* Menu-based Command Line Interface (CLI)

---

## 🛠️ Requirements

* Python 3.8 or higher
* No external libraries required (uses only Python standard libraries)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/BLACK-C-ORVUS/Password-Generator.git
```

2. Navigate to the project directory:

```bash
cd password-generator
```

3. Run the program:

```bash
python password_generator.py
```

---

## 📌 Usage

After running the program, you will see the following menu:

```
1) Create a Password
2) Exit
```

### Steps:

1. Choose **Create a Password**
2. Enter the desired password length
3. A random password will be generated and displayed
4. Choose whether to save the password
5. If yes, enter:

   * Username
   * Comment / description
6. The password will be saved in `password.txt`

---

## 📂 Project Structure

```
password-generator/
│
├── password_generator.py
├── password.txt
└── README.md
```

---

## ⚠️ Security Notes

* This project is for **educational purposes only**
* Passwords are stored in **plain text**
* For real-world use, consider:

  * Hashing or encrypting stored passwords
  * Using a secure password manager

---

## 🧠 Future Improvements

* Encrypt the saved password file
* Option to select character types
* Allow or prevent duplicate characters
* Add a graphical user interface (GUI)

---

## 👤 Author

* BLACK-C-ORVUS
* 🌐 GitHub: https://github.com/BLACK-C-ORVUS

---

## 📜 License

This project is released under the **MIT License**.

---

⭐ If you find this project useful, please consider giving it a star!
