import webbrowser
import os
import http.server
import socketserver
import subprocess

def run_uvicorn():
    uvicorn_command = "uvicorn main:app --reload --port 8000"
    subprocess.Popen(uvicorn_command, shell=True, cwd=os.path.join("server"))

def open_html():
    html_path = os.path.abspath("index.html")

    os.chdir(os.path.dirname(html_path))
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("127.0.0.1", 0), Handler)

    server_port = httpd.server_address[1]

    webbrowser.open(f"http://127.0.0.1:{server_port}/", new=2)

    print(f"Server is running at http://127.0.0.1:{server_port}/")

    httpd.serve_forever()

if __name__ == "__main__":
    run_uvicorn()
    open_html()
