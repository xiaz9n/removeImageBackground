from PIL import Image

# Open an image file
with Image.open('figure.png') as img:
    # Convert the image to RGBA format
    img = img.convert("RGBA")
    
    # Get data of the image
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[0] in list(range(200, 256)):
            new_data.append((item[0], item[1], item[2], 0))
        else:
            new_data.append(item)
            
    # Update image data
    img.putdata(new_data)
    
    # Save the new image
    img.save('figure_rmbg.png', 'PNG')
