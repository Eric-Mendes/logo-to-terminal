import numpy as np
from PIL import Image


def print_arr(new_arr: list) -> None:
    for i in range(len(new_arr)):
        for j in range(len(new_arr[0])):
            if j == len(new_arr[0])-1:
                print(new_arr[i][j])
            else:
                print(new_arr[i][j], end='')


if __name__ == '__main__':

    # specify the path of the image you want to show
    path = input('Specify the path of the image you want to show: ')
    image = Image.open(r'{path}'.format(path=path))

    # resizing the image so it fits in the terminal
    max_size = int(input("Width: ")), int(input("Height: "))
    ratio = min(max_size[0]/image.size[0], max_size[1]/image.size[1])
    new_size = (int(image.size[0]*ratio), int(image.size[1]*ratio))
    image = image.resize(new_size)

    # turning the image into a 2d array
    # each number is the color of a pixel
    # white = 0
    # black = 255
    arr = np.array(image)

    # mapping the numbers to symbols
    # each black pixel will have the # symbol
    # white will have a whitespace
    new_arr = []
    for line in arr:
        row = []
        for i in line:
            if i == 0:
                row.append(' ')
            else:
                row.append('#')

        new_arr.append(row)

    print_arr(new_arr)
