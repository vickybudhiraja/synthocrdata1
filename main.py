#### IMPORTANT ##########################################
# This code is compatible to Google colab sheets        #
# You need to mod it to include it into your own code   #
# If you need help, send me a comment                   #
#########################################################

## FIRST STEP: make sure to install this lib
# !pip install trdg

from trdg.generators import GeneratorFromStrings

from IPython.display import display, Image
from PIL import Image as PILImage
from io import BytesIO

from matplotlib.pyplot import imshow
import numpy as np

generator = GeneratorFromStrings(
    #strings = ['नमस्ते', 'उत्तर प्रदेश', 'पी एम', 'देंगे', 'आज', 'बड़ी', 'खुशखबरी', 'जन्मदिन पर ', 'संग्राम', ' वायरल', 'वीडियो'],
    strings = ['Papers', 'I ', 'Try', 'and', 'code', 'with', 'you'],
    count = 256,
    #fonts = ["/content/fonts/Gargi.ttf"],
    fonts = ["/content/fonts/Bizarro.ttf"],
    language="hi",
    size = 100,
    background_type = 3,
    image_dir = '/content/images',
    text_color = '#000000,#888888',
    #distorsion_type=3
)

for img, lbl in generator:
    display(img)

