import os
from PIL import Image, ImageDraw, ImageFont

# Set the font file path and the output directory
font_file = 'MaruBuri-Regular.otf'
output_dir = 'output/'

# Load the font with a specific size
font_size = 48
font = ImageFont.truetype(font_file, font_size)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the range of Korean Hangul Syllables
start_unicode = 0xAC00
end_unicode = 0xD7A3

# Set the image size and background color
image_size = (64, 64)
bg_color = (255, 255, 255)

# Iterate through the Hangul Syllables and generate images
for codepoint in range(start_unicode, end_unicode + 1):
    char = chr(codepoint)

    # Create a new image with a white background
    image = Image.new('RGB', image_size, bg_color)
    draw = ImageDraw.Draw(image)

    # Get the size of the character
    w, h = draw.textsize(char, font)

    # Calculate the position to center the character
    x = (image_size[0] - w) // 2
    y = (image_size[1] - h) // 2

    # Draw the character on the image
    draw.text((x, y), char, font=font, fill=(0, 0, 0))

    # Save the image with a suitable file name
    file_name = f"{output_dir}/{char}.png"
    image.save(file_name)

print("Character images generated successfully.")
