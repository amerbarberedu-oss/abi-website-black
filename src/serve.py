#!/usr/bin/env python3
"""Local dev server that mimics Vercel's cleanUrls:true behavior.
/about → serves about.html
/es/contact → serves es/contact.html
/manhattan → serves index.html (campus JS handles the rest)
/ → serves index.html
"""
import http.server, os, socketserver

PORT = 8080
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# Special route aliases (Vercel rewrites in vercel.json)
ALIASES = {
    '/manhattan': '/index.html',
    '/es/manhattan': '/es/index.html',
    '/500-hours-master-barber-program-landing-page': '/landing-funnels/500-hours-master-barber-program-landing-page/index.html',
    '/500-hours-master-barber-program-landing-page/spanish': '/landing-funnels/500-hours-master-barber-program-landing-page/spanish/index.html',
    '/master-barber-program-bronx': '/landing-funnels/master-barber-program-bronx/index.html',
    '/master-barber-program-bronx/spanish': '/landing-funnels/master-barber-program-bronx/spanish/index.html',
}

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]
        # Check aliases first
        if path in ALIASES:
            self.path = ALIASES[path]
            return super().do_GET()
        # Already has .html or ends with / or has file extension → serve normally
        if path.endswith('.html') or path.endswith('/') or '.' in path.split('/')[-1]:
            return super().do_GET()
        # Try path + .html
        html_path = path + '.html'
        full = os.path.join(ROOT, html_path.lstrip('/'))
        if os.path.isfile(full):
            self.path = html_path
            return super().do_GET()
        # Try path/index.html
        idx_path = path.rstrip('/') + '/index.html'
        full_idx = os.path.join(ROOT, idx_path.lstrip('/'))
        if os.path.isfile(full_idx):
            self.path = idx_path
            return super().do_GET()
        # Fallback
        return super().do_GET()

with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Serving at http://localhost:{PORT} (clean URLs + Vercel aliases enabled)")
    httpd.serve_forever()
