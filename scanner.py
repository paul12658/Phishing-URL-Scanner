# import necessary libraries
import re
import urllib.parse
import requests
import os
from dotenv import load_dotenv
# used for loading environment variables from a .env file

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
# used to get the Google API key from the environment variables

#
def is_ip_address(url):
    return re.match(r"https?://\d+\.\d+\.\d+\.\d+", url) is not None
# checks if the URL uses an IP address instead of a domain name

def has_suspicious_tld(url):
    suspicious_tlds = ['.zip', '.xyz', '.top', '.gq', '.tk', '.ml', '.cf']
    return any(url.endswith(tld) for tld in suspicious_tlds)
# checks if the URL has a suspicious top-level domain (TLD)

def has_suspicious_chars(url):
    return bool(re.search(r"[|\\{}[\]^~`]", url))
# checks if the URL contains suspicious characters that are often used in phishing URLs
# such as pipe, backslash, curly braces, square brackets, caret, tilde, or backtick

def is_long_url(url):
    return len(url) > 75
# checks if the URL is unusually long, which can be a sign of phishing attempts

def check_safe_browsing_api(url):
    safe_browsing_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + API_KEY
    body = {
        "client": {
            "clientId": "phishing-url-scanner",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(safe_browsing_url, json=body)
    result = response.json()
    return "matches" in result
# checks the URL against Google Safe Browsing API to see if it is flagged as malicious

def scan_url(url):
    heuristics = {
        "Uses IP address instead of domain": is_ip_address(url),
        "Suspicious TLD": has_suspicious_tld(url),
        "Contains suspicious characters": has_suspicious_chars(url),
        "Unusually long URL": is_long_url(url),
    }
    flagged_by_google = check_safe_browsing_api(url)
    return heuristics, flagged_by_google
# scans the URL for various heuristics and checks against Google Safe Browsing API
# returns a dictionary of heuristics and a boolean indicating if the URL is flagged by Google
if __name__ == "__main__":
    user_url = input("Enter a URL to scan: ")
    heuristics, flagged = scan_url(user_url)
    print("\nResults:")
    for k, v in heuristics.items():
        print(f"{k}: {'⚠️' if v else '✅'}")
    print(f"Google Safe Browsing: {'🚫 Threat Detected' if flagged else '✅ Clean'}")
    # prints the results of the scan to the console
    # user can input a URL to scan directly from the command line

