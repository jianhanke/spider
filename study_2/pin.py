import tesserocr
from PIL import Image

image=Image.open('code3.jpg')
result=tesserocr.image_to_text(image)
print(result)
print(len(result))
image=image.convert('L')
image.show()
threshold=130
table=[]
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)
image=image.point(table,'1')
image.show()
result2=tesserocr.image_to_text(image)
print(result2)
print(len(result2))