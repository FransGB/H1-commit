from PIL import Image
import matplotlib.pyplot as plt


image_path = 'H29/istriku.jpg'

image = Image.open(image_path)

# Menampilkan gambar
plt.imshow(image)
plt.axis('off') 
plt.show()