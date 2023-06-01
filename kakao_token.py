import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "15a0cf231d5a48f1ecc8b1a93cb1b34e",
    "redirect_url" : "https://example.com/oauth",
    "code" : "X4n4jyNpeODG0V09n71CYusplbJXJm7BOPBZRqN5HCLijlYhbX_ZjlPtm8ELsjKNSB7cJgoqJQ8AAAGIdhvVvw"}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)
