import requests
ip = requests.api.get('https://api.ipify.org').text
print(ip)