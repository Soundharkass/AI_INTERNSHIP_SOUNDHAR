import requests
from PIL import Image
import matplotlib.pyplot as plt

image_url = "https://picsum.photos/300"

response = requests.get(image_url)

if response.status_code == 200:
    with open("sample_image.jpg", "wb") as file:
        file.write(response.content)

    img = Image.open("sample_image.jpg")

    plt.imshow(img)
    plt.axis("off")
    plt.show()