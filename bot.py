print(f"DEBUG PAGE_ID: {PAGE_ID}")
print(f"DEBUG TOKEN START: {TOKEN[:25]}")
import os, requests, random
from PIL import Image, ImageDraw, ImageFont

PAGE_ID = os.environ.get("FB_PAGE_ID")
TOKEN = os.environ.get("FB_TOKEN")

# Quiz banao
a,b = random.randint(10,99), random.randint(10,99)
quiz = f"{a}+{b}={a+b}"

# Image banao
img = Image.new('RGB', (1080,1080), color='white')
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("arial.ttf", 80)
except:
    font = ImageFont.load_default()
d.text((250,450), quiz, fill='black', font=font)
img.save("quiz.jpg")

# POST - Page par hi jayega
url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
with open("quiz.jpg","rb") as f:
    r = requests.post(url, data={"caption": quiz, "access_token": TOKEN}, files={"source": f})
print(r.text)
print(f"Quiz: {quiz}")
