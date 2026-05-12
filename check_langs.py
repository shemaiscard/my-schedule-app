import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

repos = [
    "digital-wallet-sim", "Face-Analysis-pro", "Flight-reservation-app",
    "Grading-Mngmt-System", "grading-system-GUI", "my-village",
    "smart-room-iot", "SOCIAL-CONNECT", "Text-Autocomplete-System", 
    "Ze-video-downloader"
]

results = []

for repo in repos:
    try:
        url = f"https://api.github.com/repos/shemaiscard/{repo}/languages"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            langs = json.loads(response.read().decode())
            results.append(f"{repo}: {list(langs.keys())}")
    except Exception as e:
        pass

print("\n".join(results))
