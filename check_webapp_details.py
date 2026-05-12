import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

repos = ["digital-wallet-sim", "Ze-video-downloader", "Flight-reservation-app"]

for repo in repos:
    try:
        url = f"https://api.github.com/repos/shemaiscard/{repo}/contents"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            contents = json.loads(response.read().decode())
            filenames = [item['name'] for item in contents]
            print(f"{repo}: {filenames}")
    except:
        pass
