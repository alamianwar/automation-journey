print("🔒 System Locked - Password Required")
correct_password = "1234"
attempts = 3

while attempts > 0 :
    password = input("Enter password: ")

    if password == correct_password:
        print("✅ Access granted, Welcome!")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong password, Attempts left: {attempts}")

if attempts == 0:
    print("⛔ Too many wrong attempts. Access locked.")