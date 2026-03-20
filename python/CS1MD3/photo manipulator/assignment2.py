from PIL import Image
from typing import List


def mirror(raw: List[List[List[int]]])-> None:

    for row in raw:
        for dat in range (len(raw[0])//2):
            row[dat],row[-(dat+1)] = row[-(dat+1)],row[dat]
        
    """
    Assume raw is image data. Modifies raw by reversing all the rows
    of the data.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> mirror(raw)
    >>> raw
    [[[255, 255, 255], [0, 0, 0], [233, 100, 115]],
     [[255, 255, 255], [1, 9, 0], [199, 201, 116]]]
    """
    return


def grey(raw: List[List[List[int]]])-> None:

    def average(L):
        total = 0
        for i in L:
            total += i
        avg = total//3
        return[avg,avg,avg]

    for row in raw:
        for i in range (len(raw[0])):
            row[i] = average(row[i])
    
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> grey(raw)
    >>> raw
    [[[149, 149, 149], [0, 0, 0], [255, 255, 255]],
     [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
    """
    return


def invert(raw: List[List[List[int]]])->None:

    def inv (L):
        largest = 0
        smallest = 255
        for val in L:
            if val > largest:
                largest = val
            if val < smallest:
                smallest = val
        for i in range(len(L)):
            if L[i] == largest:
                L[i] = smallest
            elif L[i] == smallest:
                L[i] = largest
        return L
                

    for row in raw:
        for value in row:
            value = inv(value)
    
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """
    return

def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    if len(raw1[0][0]) == 0:
        return raw2
    if len(raw2[0][0]) == 0:
        return raw1

    len1 = len(raw1)
    len2 = len(raw2)

    wid1 = len(raw1[0])
    wid2 = len(raw2[0])

    maxH = max(len1,len2)
    maxW = max(wid1,wid2)

    new_list = []

    def undefined(i,j, h,w):
        return i >= h or j >= w
        
    for i in range(maxH):
        row = []
        for j in range(maxW):
            if undefined(i,j,len1,wid1) and undefined(i,j,len2,wid2):
                row.append([0,0,0])
            elif undefined(i,j,len2,wid2):
                row.append(raw1[i][j])
            elif undefined(i,j,len1,wid1):
                row.append(raw2[i][j])
            elif i % 2 == 0:
                row.append(raw1[i][j])
            else:
                row.append(raw2[i][j])
            
        new_list.append(row)
    return new_list


    """
    Merges raw1 and raw2 into new raw image data and returns it.
    It merges them using the following rule/procedure.
    1) The new raw image data has height equal to the max height of raw1 and raw2
    2) The new raw image data has width equal to the max width of raw1 and raw2
    3) The pixel data at cell (i,j) in the new raw image data will be (in this order):
       3.1) a black pixel [0, 0, 0], if there is no pixel data in raw1 or raw2
       at cell (i,j)
       3.2) raw1[i][j] if there is no pixel data at raw2[i][j]
       3.3) raw2[i][j] if there is no pixel data at raw1[i][j]
       3.4) raw1[i][j] if i is even
       3.5) raw2[i][j] if i is odd
    """

def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:
    if len(raw[0][0]) == 0:
        return raw

    def average(L):
        avg = []
        count = len(L)
        for i in range(3):
            total = 0
            for subL in L:
                total += subL[i]
            avg.append(total//count)
        return avg

    leng = len(raw)
    widt = len(raw[0])

    compressed = []
    for i in range(leng):
        if i%2 == 0:
            row = []
            for j in range(widt):
                if j%2 == 0:
                    L = [raw[i][j]]
                    if i+1 < leng:
                        L.append(raw[i+1][j])
                    if j+1 < widt:
                        L.append(raw[i][j+1])
                    if len(L) == 3:
                        L.append(raw[i+1][j+1])
                    avg = average(L)
                    row.append(avg)
            compressed.append(row)
    return compressed
                    
    """
    Compresses raw by going through the pixels and combining a pixel with
    the ones directly to the right, below and diagonally to the lower right.
    For each RGB values it takes the average of these four pixels using integer
    division. If is is a pixel on the "edge" of the image, it only takes the
    relevant pixels to average across. See the second doctest for an example of
    this.

    >>> rawb = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
    >>> raw1 = compress(raw)
    >>> raw1
    [[[108, 77, 57], [153, 115, 26]],
     [[63, 79, 87], [191, 51, 33]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
    >>> raw2 = compress(raw)
    >>> raw2
    [[[108, 77, 57], [255, 177, 50]],
     [[117, 166, 80], [0, 1, 1]]]
    """
    return


"""
**********************************************************

Do not worry about the code below. However, if you wish,
you can us it to read in images, modify the data, and save
new images.

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)
