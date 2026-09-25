import random, requests, os
from PIL import Image, ImageDraw, ImageFont

# FB Secrets
PAGE_ID = os.environ.get("FB_PAGE_ID")
TOKEN = os.environ.get("FB_TOKEN")

# Math Quiz banayo
a = random.randint(10, 99)
b = random.randint(10, 99)
op = random.choice(["+", "-", "x"])
if op == "+": ans = a + b
elif op == "-": ans = a - b
else: ans = a * b

# Image banayo
img = Image.new('RGB', (1080, 1080), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
# Simple text - bina font ke bhi chalega
draw.text((150, 400), f"{a} {op} {b} = ?", fill=(0,0,0), font=ImageFont.load_default())
draw.text((150, 600), f"Comment your answer!", fill=(255,0,0), font=ImageFont.load_default())
img.save("quiz.jpg")

# FB par post karo
url = f"https://graph.facebook.com/{PAGE_ID}/photos"
files = {'source': open('quiz.jpg', 'rb')}
data = {'message': f"Math Quiz Time! {a} {op} {b} = ? #mathquiz #puzzle", 'access_token': TOKEN}
r = requests.post(url, files=files, data=data)
print(r.text)
print(f"Quiz: {a}{op}{b}={ans}")
