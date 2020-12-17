from PIL import Image 

def revalLBSImage(imgage_or_imagePath, nbits=1):
    
    def getLBS(byte,n=1):
        byte = byte & 255>>8-n
        byte = byte << 8 - n
        return byte
  
    if isinstance(imgage_or_imagePath, str):
        img = Image.open(imgage_or_imagePath)
    else :
        img = imgage_or_imagePath
        
    width,heigh = img.size
    if img.mode == 'RGB' :
        for row in range(heigh):
            for col in range(width):
                (r,g,b) = img.getpixel((col,row))
                r = getLBS(r,nbits)
                g = getLBS(g,nbits)
                b = getLBS(b,nbits)
                img.putpixel((col,row),(r,g,b))
    else :
        for row in range(heigh):
            for col in range(width):
                l = img.getpixel((col,row))
                img.putpixel((col,row), getLBS(l,nbits))
    return img
