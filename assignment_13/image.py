import requests
import re
import ast

user = input("Enter the image name: ")
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = f"https://www.google.com/search?sca_esv=ba28415142d5cdfa&sxsrf=AE3TifNhctPsq7qNXGTPWOzn1g17pHMVZA:1752662820424&q={user}&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeioyp3OhN11EY0n5qfq-zENyQuF3_WaPI4Qgb6AZzy-etFjo9fqZ_m1LmwOk0Tw7NlugVBqJ2aYQkP3knYTQiMAm7VMYCShUYFAjfab01LRPu7T6r7JLyXh4g10wM4MIuhgmcw9MWBeBQodDsJvoIkm6a8gjQ8MCeXyHrPcd-p2hF-AVnA&sa=X&ved=2ahUKEwjr98nmmcGOAxVOa2wGHV_OHKwQtKgLKAF6BAgUEAE&biw=1920&bih=993&dpr=1"
response = requests.get(url=url, headers=user_agent).text

pattern = r'\["https://.*?\.jpg",\s*[0-9]+,\s*[0-9]+\]'
images = re.findall(pattern, response)

print(f"Total images: {len(images)}")
if not images:
    print("No images found.")
else:
    no_of_images = int(input("Enter the number of images to print: "))
    for i, img in enumerate(images):
        if i >= no_of_images:
            break
        try:
            image_url = ast.literal_eval(img)[0]
            print(image_url)
            try:
                image_data = requests.get(image_url, headers=user_agent).content
                with open(f"image_{i+1}.jpg", "wb") as f:
                    f.write(image_data)
                print(f"Downloaded image_{i+1}.jpg")
            except Exception as e:
                print(f"Error downloading image: {e}")
        except Exception as e:
            print(f"Error parsing image data: {e}")