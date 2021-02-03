# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:48:46 2020

@author: Mir Safi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:44:00 2020

@author: Mir Safi
"""

# Function to convert a normal String into Binary String:

def conver_to_binary(message):
    res = "".join(f"{ord(i):08b}" for i in message)
    return res

# Encode the image

# Ecode the image with text and save it as victim_image
def encode(image, victim_image, text):
    from PIL import Image
    i=0
    
    # Convert the String to binary String
    data = conver_to_binary(text)
    
    # Use Length of data as a key for the decoding purpose
    length = len(data)
    # Open the image
    with Image.open(image) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    if(i < length):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i+=1
                img.putpixel((x,y), tuple(pixel))
        img.save(victim_image, "PNG")
    return length

# Decoding 

def decode(image, length):
    from PIL import Image
    i=0
    extracted_bin = []
    with Image.open(image) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    if(i < length):
                        extracted_bin.append(pixel[n]&1)
                        i+=1
                        
                        
    #print(extracted_bin)
    
    str1 = ''.join(str(e) for e in extracted_bin)
    
    
    split = ','.join([str1[i:i+8] for i in range(0, len(str1), 8)])
    #print(split)

    ascii_string = "".join([chr(int(binary, 2)) for binary in split.split(",")])
    #ascii_string  
   
    return ascii_string

string = "Stegno Example"
l = encode("unb.jpeg","victim.png",string)

stegno_text = decode("victim.png",l)
print(stegno_text)