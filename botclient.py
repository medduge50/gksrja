import http.server
import socketserver
import requests

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 5959), handler) as httpd:
  ip = requests.get('https://ipinfo.io/ip').text
  print(ip)
  print('포트 5959으로 사이트가 생성되었습니다.')
  httpd.serve_forever()
