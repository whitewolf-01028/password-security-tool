# 🔐 Password Security Tool (Python)

A simple **Python-based Password Security Tool** that helps users evaluate password safety.

This tool can:

* Check password strength
* Check if a password has appeared in known data breaches
* Generate strong random passwords
* Save scan reports automatically

---

# 📌 Features

## 1️⃣ Password Strength Checker

Analyzes the password based on:

* Minimum length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Results:

* Weak
* Medium
* Strong

---

## 2️⃣ Password Breach Checker

Checks whether the password has appeared in known **data breaches** using the **Have I Been Pwned API**.

Security method used:

* Password converted to **SHA1 hash**
* Only the **first 5 characters of the hash** are sent to the API
* This follows the **k-Anonymity model**, so the full password is never exposed.

---

## 3️⃣ Strong Password Generator

Generates secure random passwords containing:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Default length: **12 characters**

Example generated password:

```
A9f#T7@kL2!p
```

---

## 4️⃣ Report Generator

Every action performed in the tool is automatically saved in:

```
/reports/scan_report.txt
```

Example report:

```
===== Password Scanner Report =====
Password Checked: example123
Strength: Medium
Date: 2026-03-09
-----------------------------------
```

---

# 📸 Screenshot

Below is a demo of the Password Security Tool running in the terminal.

![Password Security Tool Demo](screenshot/demo.png)

---

# 📂 Project Structure

```
password-security-tool/
│
├── password_tool.py
├── README.md
│
├── reports/
│   └── scan_report.txt
│
└── screenshots/
    └── demo.png
```

---

# ⚙️ Requirements

Install dependencies before running:

```bash
pip install requests
```

Recommended Python version:

```
Python 3.8+
```

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/password-security-tool.git
```

Navigate to the project folder:

```bash
cd password-security-tool
```

Run the script:

```bash
python password_tool.py
```

---

# 🖥️ Tool Menu

```
-------------------------------------------------
        PASSWORD SECURITY TOOL
-------------------------------------------------
1. Check Password Strength
2. Check Password Breach
3. Generate Strong Password
4. Exit
-------------------------------------------------
```

---

# 🔐 Security Concepts Used

* Password strength validation
* Regular expressions
* SHA-1 hashing
* k-Anonymity security model
* API integration
* Secure password generation

---

# 🚀 Future Improvements

Possible upgrades:

* GUI version using Tkinter
* Export reports as PDF
* Password entropy calculation
* Batch password scanning
* Web-based dashboard

---

# 📚 Learning Purpose

This project is useful for beginners learning:

* Python scripting
* Cybersecurity basics
* API integration
* Password security practices

---

# ⚠️ Disclaimer

This tool is intended **for educational purposes only**.
Do not use it to test or collect passwords from others.

---

# 👨‍💻 Author

Cybersecurity Practice Project.

If you like this project, consider ⭐ starring the repository.
