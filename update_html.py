import os
import re

manifest_link = '    <link rel="manifest" href="manifest.json">\n    <meta name="theme-color" content="#0066ff">\n'
sw_script = """    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('sw.js').then(reg => {
                    console.log('Service Worker registered');
                }).catch(err => {
                    console.log('Service Worker registration failed', err);
                });
            });
        }
    </script>\n"""

for filename in os.listdir('/home/giscard/IdeaProjects/Portfolio'):
    if filename.endswith('.html') and filename != 'googlee977c67da3aaf487.html':
        filepath = os.path.join('/home/giscard/IdeaProjects/Portfolio', filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Add manifest link if not present
        if 'manifest.json' not in content:
            content = content.replace('</head>', manifest_link + '</head>')
        
        # Add SW script if not present
        if 'navigator.serviceWorker.register' not in content:
            content = content.replace('</body>', sw_script + '</body>')
        
        with open(filepath, 'w') as f:
            f.write(content)
