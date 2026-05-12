import subprocess
import json

repos = ["Ze-Pdf", "Portfolio", "yin-ai", "Ze-Matrix-", "survey", "amakarita", "ZE-BASE-Number-Base-Converter", "UNO", "CIPHER-SHIELD-SUITE"]

results = []
for repo in repos:
    try:
        cmd = ["gh", "api", f"repos/shemaiscard/{repo}/contents"]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        contents = json.loads(output)
        filenames = [item['name'] for item in contents]
        has_manifest = any('manifest.json' in f or 'manifest.webmanifest' in f for f in filenames)
        
        if not has_manifest:
            # Check public folder for modern apps
            if 'public' in filenames:
                pub_cmd = ["gh", "api", f"repos/shemaiscard/{repo}/contents/public"]
                pub_output = subprocess.check_output(pub_cmd, stderr=subprocess.STDOUT)
                pub_contents = json.loads(pub_output)
                if any('manifest.json' in f or 'manifest.webmanifest' in f for f in [i['name'] for i in pub_contents]):
                    has_manifest = True
            
        results.append(f"{repo}: {'HAS Manifest' if has_manifest else 'No Manifest'}")
    except Exception as e:
        results.append(f"{repo}: Error")

print("\n".join(results))
