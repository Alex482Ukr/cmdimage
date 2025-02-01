from PIL import Image
from PIL import ImageEnhance
from math import ceil
from os import get_terminal_size

class Screen:
    symbols = r''' `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@'''

    def __init__(self, width=120, height=30):
        self.matrix = [[self.symbols[0] for i in range(width)] for _ in range(height)]
    
    @property
    def rows(self):
        return len(self.matrix)
    @property
    def cols(self):
        return len(self.matrix[0])

    @classmethod
    def scale(cls, num, sc1, sc2):
        return ceil(num / sc1 * (sc2-1 if sc2 != 0 else sc2))

    def show(self):
        for i in range(self.rows):
            print(*self.matrix[i], sep='', end='\n')
    
    def gradient(self):
        self.matrix = [[self.symbols[self.scale(i, self.cols, len(self.symbols))] for i in range(self.cols)] for _ in range(self.rows)]


    def import_image(self, path):
        with Image.open(path) as im:
            im = ImageEnhance.Contrast(im).enhance(1.3)
            im = im.convert('L')
            im = im.resize((self.cols, self.rows))
            bitmap = im.load()
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = self.symbols[self.scale(bitmap[j, i], 255, len(self.symbols))]
    

if __name__ == '__main__':
    size = get_terminal_size()
    scr = Screen(size.columns-1, size.lines-1)

    while True:
        scr.import_image(input("Path to image: ").strip('"'))
        scr.show()