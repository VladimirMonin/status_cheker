import urllib.request

request = urllib.request.urlopen("https://noukash.com/intensive").read().decode('utf-8')
print(request)
