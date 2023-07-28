import sys
import os
import random

from PIL import Image

def randomize_a_pixel(img):
    
    # get a random number between 0 and 255
    c = lambda: random.randint(0,255)
    
    x = random.randint(0, img.size[0])
    y = random.randint(0, img.size[1])
    
    img.putpixel((x,y), (c(), c(), c()))
    

def remove_exif_and_randomize_hash(image_path):
    img = Image.open(image_path)
    
    # extend a tiny bit of the image to randomize the hash
    image_dimensions = img.size
    img.resize(image_dimensions[0] + int(image_dimensions[0]/100), image_dimensions[1] + int(image_dimensions[1]/100))
    
    # change 5 pixels of the image to add some noise
    [randomize_a_pixel(img) for i in range(5)]
    
    # save the image and remove exif data
    img.save(image_path, exif=b'')

def main():
    
    path = None
    
    try:
        path = sys.argv[1]
    except:
        print("Please enter a path directing to a folder of images")
        sys.exit()
        
    images = os.listdir(path)
    
    for image in images:
        image_path = os.path.join(path, image)
        
        remove_exif_and_randomize_hash(image_path)
    

if __name__ == "__main__":
    main()