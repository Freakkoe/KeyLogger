# 🔑 Keylogger - Keyboard Event Logger

A simple keylogger written in Python that records keystrokes and saves them in a log file. This tool can be used for monitoring your own keystrokes for debugging or educational purposes.

## ⚠️ Legal Disclaimer

**This software is intended for legal and authorized use only.**  
Using this tool without explicit permission from the system owner may be illegal and violate privacy laws. **The developer assumes no liability for misuse of this software.**

## 🔍 Features
- Logs keystrokes, including special keys (Enter, Backspace, Shift, etc.)
- Saves keystrokes to a log file (`key_log.txt`)
- Logs errors in a separate file (`keylogger_errors.log`)
- Automatically stops when the `Esc` key is pressed

## 📋 Requirements

- Python 3.6+
- `pynput` library (for keyboard monitoring)

## 🚀 Installation

1. **Clone or download the repository**   
```bash   
git clone https://github.com/Freakkoe/keylogger.git   
cd keylogger   
```

2. **Install required dependencies**   
```bash   
pip install pynput   
```

## 💻 Usage

Run the keylogger with:
```bash
python keylogger.py
```

Keystrokes are stored in `key_log.txt`, and any errors are logged in `keylogger_errors.log`.

To stop the keylogger, press Escape (Esc).

## 📝 Log Files

- `key_log.txt` → Stores all recorded keystrokes
- `keylogger_errors.log` → Stores error messages in case of issues

## 🛡️ Security Considerations

- Only use this software with explicit permission from the system owner
- Do not use it on systems where you do not have administrative rights
- Ensure compliance with local privacy and cybersecurity laws

## 📄 License

BSD 3-Clause License

Copyright (c) 2025 Freakkoe All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## 👤 Author

Freakkoe