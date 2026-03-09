import hashlib
import requests
import re
import random
import string
import datetime
import os

REPORT_FILE = "reports/scan_report.txt"

os.makedirs("reports", exist_ok=True)

print("""
-------------------------------------------------
        PASSWORD SECURITY TOOL
-------------------------------------------------
1. Check Password Strength
2. Check Password Breach
3. Generate Strong Password
4. Exit
-------------------------------------------------
""")


def save_report(content):

    with open(REPORT_FILE, "a") as file:

        file.write("\n===== Password Scanner Report =====\n")
        file.write(content)
        file.write("\nDate: " + str(datetime.datetime.now()))
        file.write("\n-----------------------------------\n")


def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def check_breach(password):

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)

    hashes = response.text.splitlines()

    for h in hashes:

        hash_suffix, count = h.split(":")

        if hash_suffix == suffix:
            return count

    return 0


def generate_password(length=12):

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = "".join(random.choice(characters) for i in range(length))

    return password


while True:

    choice = input("\nSelect Option: ")

    if choice == "1":

        password = input("Enter password: ")

        strength = check_strength(password)

        print("Password Strength:", strength)

        save_report(f"Password Checked: {password}\nStrength: {strength}")

    elif choice == "2":

        password = input("Enter password: ")

        breach = check_breach(password)

        if breach:
            msg = f"Password found {breach} times in breaches"
            print("WARNING:", msg)
        else:
            msg = "Password not found in breaches"
            print(msg)

        save_report(f"Password Checked: {password}\nBreach Status: {msg}")

    elif choice == "3":

        password = generate_password()

        print("Generated Password:", password)

        save_report(f"Generated Password: {password}")

    elif choice == "4":

        print("Exiting Tool...")
        break

    else:

        print("Invalid option")