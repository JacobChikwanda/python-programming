# Facebook Login Simulation Program

## Problem Statement
You are required to write a Python program that simulates the login functionality of Facebook. The user will be prompted to enter their email and password, and the program will validate the input against hardcoded credentials. The program should implement control structures to handle the following scenarios:
1. **Login Success** - If the email and password match the stored values, display a success message.
2. **Invalid Credentials** - If the email or password is incorrect, display an error message.
3. **User Not Found** - If the entered email doesn't match the stored email, display a user not found message.

The program should also include a menu screen where users can either attempt to log in or exit the program. The menu should persist and allow the user to keep trying to log in until they choose to exit by pressing a designated key.

### **Hardcoded Credentials**
- **Email**: `user@example.com`
- **Password**: `password123`

### **Concepts Covered**
- Loops (to persist the menu screen and handle multiple login attempts).
- Control Structures (to manage the login scenarios like success, invalid credentials, or user not found).

### **Requirements**
- The email and password should be hardcoded as variables within the program.
- The program should use a loop to display the menu until the user decides to exit.
- After each login attempt, the user should be returned to the menu screen.

---

## **Sample Output**

```python
Welcome to the Facebook Login System
1. Login
2. Exit
Choose an option: 1

Enter your email: user@example.com
Enter your password: password123
Login successful! Welcome to your account.

---------------------

Welcome to the Facebook Login System
1. Login
2. Exit
Choose an option: 1

Enter your email: user@example.com
Enter your password: wrongpassword
Invalid credentials, please try again.

---------------------

Welcome to the Facebook Login System
1. Login
2. Exit
Choose an option: 1

Enter your email: unknown@example.com
Enter your password: password123
User not found.

---------------------

Welcome to the Facebook Login System
1. Login
2. Exit
Choose an option: 2
Exiting the system. Goodbye!
