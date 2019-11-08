import requests

r = requests.get("https://ufh.ac.za")
print(r.status_code)
print(r.ok)
