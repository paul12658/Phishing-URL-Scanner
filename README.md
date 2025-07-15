#  Phishing URL Scanner

A simple but powerful web tool that helps detect suspicious or malicious URLs using both quick heuristics and Google Safe Browsing threat intelligence.

---

## Features

- Detects suspicious patterns in URLs:
  - IP addresses instead of domain names
  - Suspicious or rare domain endings (e.g., `.zip`, `.xyz`, `.tk`)
  - Weird characters often used in scam URLs
  - Unusually long URLs

- Integrates with **Google Safe Browsing API** to flag:
  - Malware
  - Phishing
  - Unwanted software links

- Built with Python and Flask – no JavaScript required

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/paul12658/phishing-url-scanner.git
cd phishing-url-scanner
# Windows
python -m venv venv
source venv/Scripts/activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#Go to Google Cloud Console

Enable the Safe Browsing API

Generate an API key

Create a .env file in the root of the project and add:


# Run Project
python app.py

# Contributions
Pull requests are welcome! If you have ideas to improve heuristics or UI, feel free to open an issue or contribute directly.



