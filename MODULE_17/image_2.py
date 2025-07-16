import requests
import re

# user input for image name
user = input("Enter the image name: ")

# user agent to avoid blocking by the Server
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# Constructing the URL for Google search
url = f"https://www.google.com/search?sca_esv=ba28415142d5cdfa&sca=xsrf=AE3tIFwhCtSg7qNkGTPW2n1g17pPHVf2:1576268280242&q={user}&udm=2"

# Making the request to Google search
response = requests.get(url, headers=user_agent)

# Decode bytes content to string
html_content = response.content.decode('utf-8')

# Extracting the image URL from the response using regex
pattern = r"https://.*?\.(jpg|jpeg|png)"
images = re.findall(pattern, html_content)

for image in images:
    print(image)
