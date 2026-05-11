# Password Manager

A secure, lightweight password management tool built with Python that uses military-grade encryption to store and retrieve your passwords safely.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Security Considerations](#security-considerations)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## ✨ Features

- **Secure Encryption**: Uses Fernet (symmetric encryption) from the `cryptography` library for password protection
- **Easy-to-Use Interface**: Simple command-line menu-driven interface
- **Password Storage**: Stores passwords locally in a CSV file
- **Password Retrieval**: Quickly retrieve stored passwords by website name
- **Lightweight**: Minimal dependencies and fast performance
- **Cross-Platform**: Runs on Windows, macOS, and Linux

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** (Python 3.12+ recommended)
- **pip** (Python package manager)
- **Virtual Environment** support (usually included with Python)
- **Git** (optional, for cloning the repository)

### System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 100 MB
- **Disk Space**: Minimum 50 MB (including Python and dependencies)

---

## 💻 Installation

### Step 1: Clone or Download the Project

**Option A: Using Git**
```bash
git clone <repository-url>
cd Password_Manager
```

**Option B: Manual Download**
1. Download the project files
2. Extract the ZIP file
3. Navigate to the `Password_Manager` directory

### Step 2: Create a Virtual Environment

Creating a virtual environment is **highly recommended** to avoid conflicts with other Python projects.

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Upgrade pip

Ensure you have the latest version of pip:

**On Windows:**
```powershell
python -m pip install --upgrade pip
```

**On macOS/Linux:**
```bash
python3 -m pip install --upgrade pip
```

### Step 4: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

**Or manually install the required package:**

```bash
pip install cryptography
```

---

## 🚀 Setup Instructions

### Automatic Setup (Recommended)

If a `setup.py` or `requirements.txt` file exists, run:

```bash
pip install -r requirements.txt
```

### Manual Setup

1. **Verify Python Installation**
   ```bash
   python --version
   ```
   Expected output: `Python 3.8.x` or higher

2. **Verify Virtual Environment Activation**
   
   Your terminal should show `(venv)` at the beginning of the line:
   ```
   (venv) C:\Users\YourName\Password_Manager>
   ```

3. **Install Cryptography Package**
   ```bash
   pip install cryptography
   ```

4. **Verify Installation**
   ```bash
   python -c "import cryptography; print('Cryptography installed successfully')"
   ```

---

## 🎯 How to Run

### Running the Application

**Step 1: Navigate to the Project Directory**
```bash
cd /path/to/Password_Manager
```

**Step 2: Activate Virtual Environment (if not already activated)**

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**Step 3: Run the Program**
```bash
python main.py
```

### Expected Output

When you run the program, you should see:

```
1. Add Password
2. Get Password
3. Exit
Enter your choice:
```

---

## 📖 Usage Guide

### Option 1: Add a New Password

1. Run the program: `python main.py`
2. Enter `1` and press Enter
3. Follow the prompts:
   ```
   Website: github.com
   Username: myusername
   Password: mypassword123
   ```
4. The password will be encrypted and saved to `passwords.csv`

### Option 2: Retrieve a Stored Password

1. Run the program: `python main.py`
2. Enter `2` and press Enter
3. Enter the website name:
   ```
   Enter website: github.com
   ```
4. The program will display:
   ```
   Website: github.com
   Username: myusername
   Password: mypassword123
   ```

### Option 3: Exit the Program

1. Enter `3` and press Enter
2. The program will terminate

### Example Session

```
1. Add Password
2. Get Password
3. Exit
Enter your choice: 1

Website: twitter.com
Username: john_doe
Password: secure_pass_123

1. Add Password
2. Get Password
3. Exit
Enter your choice: 2

Enter website: twitter.com

Website: twitter.com
Username: john_doe
Password: secure_pass_123

1. Add Password
2. Get Password
3. Exit
Enter your choice: 3

(Program exits)
```

---

## 📁 File Structure

```
Password_Manager/
├── main.py                 # Main application file
├── passwords.csv          # Encrypted password storage (auto-created)
├── requirements.txt       # Python package dependencies
├── README.md             # This file
├── .gitignore            # Git ignore file (recommended)
└── venv/                 # Virtual environment (auto-created)
    ├── Scripts/          # Executables (Windows)
    ├── bin/              # Executables (macOS/Linux)
    └── Lib/              # Packages
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `main.py` | Core application logic and menu system |
| `passwords.csv` | Encrypted password database (created automatically) |
| `requirements.txt` | Lists all Python dependencies |
| `venv/` | Isolated Python environment for the project |

---

## 🔐 Technical Details

### Encryption Algorithm

The application uses **Fernet (symmetric encryption)** from the `cryptography` library:

- **Type**: Symmetric encryption
- **Algorithm**: AES 128-bit (via Fernet)
- **Key Size**: 128 bits
- **Mode**: CBC (Cipher Block Chaining)

### Data Storage

- **Format**: CSV (Comma-Separated Values)
- **Structure**: `website, username, encrypted_password`
- **Location**: `passwords.csv` (same directory as `main.py`)

### Key Generation

A new encryption key is generated each time the program runs:
- Keys are generated using `Fernet.generate_key()`
- Keys are stored in memory during runtime
- **Important**: Keys are NOT persisted; regenerating them will make old passwords unrecoverable

### Dependencies

```
cryptography>=42.0.0
```

---

## ❌ Troubleshooting

### Issue 1: `ModuleNotFoundError: No module named 'cryptography'`

**Solution:**
```bash
# Ensure virtual environment is activated
pip install cryptography
```

### Issue 2: `FileNotFoundError: [Errno 2] No such file or directory: 'passwords.csv'`

**Solution:**
The program creates `passwords.csv` automatically on first run. If this error persists:
```bash
# Create an empty passwords.csv file
echo "" > passwords.csv
```

### Issue 3: `IndexError: list index out of range`

**Solution:**
Make sure `passwords.csv` has the correct format with 3 columns. Delete and recreate:
```bash
rm passwords.csv
# Run the program to auto-create a new file
python main.py
```

### Issue 4: Python Command Not Found

**Solution:**
- On Windows, use `python` or `python.exe`
- On macOS/Linux, use `python3`
- Ensure Python is installed and added to PATH

### Issue 5: Virtual Environment Won't Activate

**Solution (Windows):**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 6: Permission Denied When Running

**Solution (macOS/Linux):**
```bash
chmod +x main.py
python3 main.py
```

### Issue 7: Passwords Not Saving

**Ensure the directory has write permissions:**
```bash
# Linux/macOS
chmod 755 /path/to/Password_Manager

# Windows - Run command prompt as Administrator
icacls "C:\path\to\Password_Manager" /grant:r %username%:F
```

---

## 🔒 Security Considerations

### Important Notes

⚠️ **Critical Security Information:**

1. **Key Management**: Currently, a new encryption key is generated each time the program runs. This means:
   - Passwords added in one session are encrypted with one key
   - Passwords cannot be retrieved in subsequent sessions
   - **This should be fixed in a production version**

2. **Recommendations for Production Use**:
   - Store the encryption key securely (e.g., environment variables or a secure key management service)
   - Use master password protection
   - Add password strength validation
   - Implement logging and audit trails
   - Never store passwords in plain text

3. **Backup Sensitive Data**:
   - Regularly backup your `passwords.csv` file
   - Keep the encryption key in a secure location
   - Store backups in encrypted storage

4. **File Permissions**:
   - Restrict access to `passwords.csv`: `chmod 600 passwords.csv` (Linux/macOS)
   - Never commit `passwords.csv` to version control
   - Use `.gitignore` to exclude sensitive files

5. **CSV Format**:
   The encrypted passwords in CSV format are not human-readable, but keep the file private.

---

## 🚀 Future Improvements

Potential enhancements for future versions:

- [ ] **Persistent Encryption Key**: Store key securely (encrypted environment variable)
- [ ] **Master Password**: Add master password protection
- [ ] **Password Strength Meter**: Validate password complexity
- [ ] **Update/Delete Passwords**: Edit or remove existing entries
- [ ] **Search Functionality**: Advanced search and filtering
- [ ] **GUI Interface**: Graphical user interface using Tkinter or PyQt
- [ ] **Database Support**: Migrate from CSV to SQLite or PostgreSQL
- [ ] **Cloud Sync**: Optional cloud backup and synchronization
- [ ] **Two-Factor Authentication**: Enhanced security features
- [ ] **Password Generator**: Auto-generate strong passwords
- [ ] **Export/Import**: Backup and restore functionality
- [ ] **Multi-User Support**: Multiple user accounts

---

## 📝 License

This project is open-source and available under the **MIT License**.

You are free to:
- Use the software for any purpose
- Modify and distribute the software
- Include it in proprietary applications

**Conditions:**
- Include the original license and copyright notice

---

## 📧 Support & Contributing

### Questions or Issues?

If you encounter any issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Technical Details](#technical-details)
3. Verify all prerequisites are installed

### Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

---

## ⚠️ Disclaimer

This is a **educational project** designed to demonstrate encryption concepts and password management principles. While it uses industry-standard encryption, it is **not recommended for storing highly sensitive credentials** in production environments.

For production use, consider dedicated password managers like:
- 1Password
- Bitwarden
- LastPass
- KeePass

---

## 🔄 Version History

- **v1.0** (May 2026): Initial release
  - Basic add/retrieve password functionality
  - CSV-based storage
  - Fernet encryption

---

**Last Updated**: May 9, 2026

---

## 📚 Additional Resources

### Learning Resources
- [Cryptography.io Documentation](https://cryptography.io/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [CSV Module Documentation](https://docs.python.org/3/library/csv.html)

### Security Resources
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Fernet Specification](https://github.com/fernet/spec)

---

## 🎓 Learning Outcomes

By using this project, you'll learn:
- ✅ How to use Python's `cryptography` library
- ✅ Symmetric encryption concepts
- ✅ File I/O operations with CSV
- ✅ Virtual environment management
- ✅ Basic command-line application development
- ✅ Password security best practices

---

**Enjoy your secure password management! 🔐**
