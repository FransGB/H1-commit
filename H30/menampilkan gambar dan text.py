from PIL import Image
import matplotlib.pyplot as plt


image_path = 'H30/istriku.jpg'

image = Image.open(image_path)


plt.imshow(image)
plt.axis('off') 

plt.figtext(0.5, 0.1, "Ini Istri Saya", ha='center', fontsize=12)

plt.show()