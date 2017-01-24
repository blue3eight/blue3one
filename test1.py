from PIL import Image 

def revalLBSImage(imagePath,nbits=1):
  
    def getLBS(byte,n=1):
        byte = byte & 255>>8-n
        byte = byte << 8 - n
        return byte
    
    img = Image.open(imagePath)
    width,heigh = img.size
    for row in range(heigh):
        for col in range(width):
            (r,g,b) = img.getpixel((col,row))
            r = getLBS(r,nbits)
            g = getLBS(g,nbits)
            b = getLBS(b,nbits)
            img.putpixel((col,row),(r,g,b))
    return img
#imshow(np.resize(np.array(fg),(100,100)))
