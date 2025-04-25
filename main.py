import os
import random

from PIL import Image, ImageEnhance

#extensions searched for
extensions = ('jpg', 'png', 'heic')


#if on windows switch './in' to '\in'!
files = os.listdir('./in')

def rotate_img(img, orientation):
    '''
    img - <PIL.Image>: the image object to be rotated
    orientation - <int>: 0 for straight, 1 for tilted, 2 for extreme
    '''
    if orientation == 'S':
        deg = random.randint(-30,30)
       
    elif orientation == 'M': #31 60
        deg = random.choice([random.randint(31,60), random.randint(-60,-31)])
    elif orientation == 'L':
        deg = random.choice([random.randint(61,150), random.randint(-150,-61)])
    
    return [orientation, img.rotate(deg, expand=True)]



# Simulate reduced brightness and contrast with the same brightness factor
def reduce_bright(img):
    enhancer = ImageEnhance.Brightness(img)
    brightness_factor = random.randint(3, 8) * 0.1
    
    img = enhancer.enhance(brightness_factor)

    contraster = ImageEnhance.Contrast(img)
    
    img = contraster.enhance(brightness_factor) 
    
    
    return [brightness_factor, img]




#image input name format: <unit>-<subchapter>-<writing type>.<file extension>
#writing type is either t for typed, m for messy, n for neat
#example: 7-8-t.png

#image output name format:
#./out/<unit>/<subchapter>-<writing type>-r<deg rotated>-b<percent brightness>.<file extension>


#if on windows again switch!
for f in files:
    path = './in/' + f

    tokens = f.split('-')

    target_path = f'./out/{f[0]}'

    extension = path.split('.')[-1]

    if extension in extensions:
        try:
            img = Image.open(path)

            os.makedirs(target_path, exist_ok=True)

            rot_images = [
                rotate_img(img, 'S'),
                rotate_img(img, 'M'),
                rotate_img(img, 'L')
            ]

            for r_i in rot_images:
                r_i[1].save(f'{target_path}/{tokens[1]}-{r_i[0]}N.{tokens[-1]}')

                b_i = reduce_bright(img)

                b_i[1].save(f'{target_path}/{tokens[1]}-{r_i[0]}P.{tokens[-1]}')
                


            
        except Exception as e:
            print(e)

