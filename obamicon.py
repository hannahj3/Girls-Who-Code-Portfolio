from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)


my_image = Image.open(sebastian.jpeg)
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.
#print(len(image_list))=375000
recolored = []
print(image_list)

for pixel in image_list:
    intensity = pixel[0] + pixel[1] + pixel[2]
    if pixel[0] + pixel[1] + pixel[2] <= 182:
        recolored.append(darkBlue)
    elif 182 < intensity and intensity <= 364:
        recolored.append(red)
    elif 364 < intensity and intensity <= 546:
        recolored.append(lightBlue)
    elif intensity > 546:
        recolored.append(yellow)

print(recolored)


new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recoloredmichelle.jpg", "jpeg")
