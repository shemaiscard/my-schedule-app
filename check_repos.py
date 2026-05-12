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
        url = f"https://api.github.com/repos/shemaiscard/{repo}/contents"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            contents = json.loads(response.read().decode())
            filenames = [item['name'] for item in contents]
            
            is_webapp = any(f.endswith('.html') or f == 'package.json' or f.endswith('.js') for f in filenames)
            has_manifest = any('manifest.json' in f or 'manifest.webmanifest' in f for f in filenames)
            
            # Additional check for public folder if package.json exists (React/Next)
            if 'public' in filenames:
                pub_url = f"https://api.github.com/repos/shemaiscard/{repo}/contents/public"
                pub_req = urllib.request.Request(pub_url, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    with urllib.request.urlopen(pub_req, context=ctx) as pub_resp:
                        pub_contents = json.loads(pub_resp.read().decode())
                        pub_filenames = [item['name'] for item in pub_contents]
                        if any('manifest.json' in f or 'manifest.webmanifest' in f for f in pub_filenames):
                            has_manifest = True
                except:
                    pass

            if is_webapp and not has_manifest:
                results.append(f"{repo} (Web App, No Manifest)")
            elif is_webapp and has_manifest:
                results.append(f"{repo} (Web App, HAS Manifest)")
            else:
                results.append(f"{repo} (Not a traditional Web App)")
    except Exception as e:
        results.append(f"{repo} (Error: {e})")

print("\n".join(results))
