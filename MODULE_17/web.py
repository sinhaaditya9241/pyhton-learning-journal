import requests

url = "http://localhost:8000/media/images/20250531_1703_Rooftop_AI_Connection_simple_compose_01jwk1t5q2fyqa2wfk5vxdgm2s.png"

user = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


respone = requests.get(url = url, headers= user)

pic = respone.content

f = open("20250531_1703_Rooftop_AI_Connection_simple_compose_01jwk1t5q2fyqa2wfk5vxdgm2s.png", "wb")

f.write(pic)

