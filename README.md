# RemoteKeylogger

This project demonstrates a basic **keylogger** implementation in Python. It captures keystrokes from the user's keyboard and sends the captured keys via email when a threshold of 250 characters is reached.

## 🔍 Purpose

The goal of this project is to showcase how a keylogger works by capturing keyboard input and sending the data via email. This type of tool can be used for educational purposes or in controlled environments for testing.

### ⚠️ Legal Disclaimer:
This project should not be used for malicious purposes. Unauthorized use of keyloggers is illegal and unethical. Always ensure you have explicit consent from the user before running such software. 

## 🛠️ Requirements

- **Python 3** or later
- **pynput** library to listen to keyboard events
- **smtplib** library for sending email
- A **Gmail** account to send emails (you need to enable "Less secure app access" for your Gmail account)

### Install the necessary dependencies:

You can install the required library using pip:

```bash
pip install pynput
```

## 🔧 Setup and Configuration

1. **Set up the Email Account**:
   - Replace the `from_email` and `to_email` variables with your own email addresses.
   - Replace the `password` variable with the password for the `from_email` account.
   
   **Important**: You might need to allow "less secure apps" in your Gmail settings to allow sending emails via SMTP.

2. **Running the Program**:
   - Run the Python script, and the program will begin capturing keystrokes.
   - Once the program captures at least 250 characters, it will send an email with the captured content to the specified recipient email address.
   
   The keylogger will continue to run in the background and capture keys until manually stopped.

## ▶️ Usage

### Example:

When a user types on their keyboard, the program will capture the keystrokes and send the data via email once the length of the captured text reaches 250 characters. Here's a breakdown of how the captured keys are handled:

- **Space** is replaced with `' '`.
- **Enter** is replaced with `\n` (newline).
- **Shift** is ignored.
- **Backspace** is recorded as `<` to indicate a character was deleted.

### Example Email Content:

```
Keycaptured
The user typed the following keys:
abc< defgh...
```

## 📑 Code Explanation

- **`keylog(key)`**: This function listens to the keys pressed by the user and processes them. It replaces specific keys like space, enter, and backspace with readable characters. Once 250 characters are captured, it triggers the email sending function.
  
- **`send_email(content)`**: This function sends an email with the captured keystrokes as content. It uses **SMTP** to connect to the Gmail server and send the email.

- **`Listener(on_press=keylog)`**: This listens for key presses and calls the `keylog` function for each key press.

## ⚠️ Notes

- **Security**: Be cautious when using this type of code. Always ensure proper authorization and consent before monitoring keyboard inputs.
- **Email Credentials**: Be aware that using your email password in scripts can be risky. Consider using an app-specific password if available or implementing additional security measures.

## 📄 License

This project is open-source and free to use. However, please be responsible with its use and ensure that you comply with local laws and regulations regarding privacy and surveillance.
