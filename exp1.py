from http.server import HTTPServer, BaseHTTPRequestHandler
content='''<html>
<h1>Configuration Deatails of laptop</h1>
<h2>Device Specifications</h2>
<pre>Device name	Bunny
Processor	AMD Ryzen 7 7435HS                              (3.10 GHz)
Installed RAM	16.0 GB (15.8 GB usable)
Device ID	77678CE8-B4C2-4B9C-BAFE-6E2F043457E4
Product ID	00342-42749-93580-AAOEM
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display
</pre>
<h2>Support</h2>
<p>Manufacturer ASUS</p>
<pre>
</html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
http=HTTPServer(server_address,Myserver)
http.serve_forever()