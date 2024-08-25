from PIL import Image, ImageFilter

# i open the image here then we can use alot on it
img = Image.open('./pokemon/pikachu.jpg')

print(f"this is image mode: {img.mode}")
print(f"image size: {img.size}")

altered_img = img.filter(ImageFilter.SHARPEN)
altered_img2 = img.convert('L')
altered_img.save("./altered_images/sharp_pikachu.png", 'png')
altered_img2.save("./altered_images/gray_pikachu.png", 'png')

# we can use show() to display the image

img1 = img.filter(ImageFilter.BLUR)
# img1.show()


img2 = img.convert('L')
# crooked = img2.rotate(90)
crooked = img2.resize((300, 300))
# crooked.show()

img3 = img.crop((0, 0, 200, 200))
# img3.show()

# ON A BIG IMAGE TO PROCESS AND AVOID SQUEESING

new_img = Image.open('./pokemon/one-eye.jpg')
new_img.thumbnail((300, 300))
new_img.show()