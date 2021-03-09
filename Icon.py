import numpy as np
from PIL import Image


def color_to_char(pixel_color, c: str) -> list:
    new_arr = []

    for line in pixel_color:
        row = []
        for i in line:
            if i == 0:
                row.append(' ')
            else:
                row.append(c)
        new_arr.append(row)

    return new_arr


class Icon:
    def __init__(self, path: str, n: int, symbol='#') -> None:
        # stores the path to the icon
        self.path = path

        # loading and resizing the icon
        self.img = Image.open(r'{}'.format(self.path))
        new_size = int(self.img.size[0]/n), int(self.img.size[1]/n)
        self.img = self.img.resize(new_size)

        # symbol to fill the image on screen. standard: #
        self.symbol = symbol

        # initializes the array
        self.arr = color_to_char(np.array(self.img), self.symbol)

    def __repr__(self):
        string = ''

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if j == len(self.arr[0]) - 1:
                    string += '{}\n'.format(self.arr[i][j])
                else:
                    string += '{}'.format(self.arr[i][j])

        return string
