import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from glob import glob

with open('char_list.txt', mode='rt', encoding='UTF8') as f:
    char_list = [char.replace('\n', '') for char in f.readlines()]
    print(char_list)
print(len(char_list))
co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
START_HAN_UNICODE = "AC00"
END_HAN_UNICODE = "D7A3"
fonts = glob("./font/*.ttf")
# print(fonts)
co = co.split(" ")

Hangul_list = [a+b+c+d
               for a in co
               for b in co
               for c in co
               for d in co]

Hangul_list = np.array(Hangul_list)

s = np.where(START_HAN_UNICODE == Hangul_list)[0][0]
e = np.where(END_HAN_UNICODE == Hangul_list)[0][0]

Hangul_list = Hangul_list[s:e+1]

for char in Hangul_list:
    unicodeChars = chr(int(char, 16))
    if unicodeChars not in char_list:
        continue
    img = Image.new('RGB', [28, 28])
    draw = ImageDraw.Draw(img)

    for ttf in fonts:
        font_name = os.path.basename(ttf).split('.')[0]
        font = ImageFont.truetype(font=ttf, size=100)

        x, y = font.getsize(unicodeChars)

        theImage = Image.new('RGB', (x + 3, y + 3), color='white')

        theDrawPad = ImageDraw.Draw(theImage)

        theDrawPad.text((0, 0), unicodeChars[0], font=font, fill='black')

        theImage.save('img/{}_{}.png'.format(unicodeChars, font_name))
