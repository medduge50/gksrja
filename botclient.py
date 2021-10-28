import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 5959), handler) as httpd:
  print('포트 5959으로 사이트가 생성되었습니다.')
  httpd.serve_forever()
