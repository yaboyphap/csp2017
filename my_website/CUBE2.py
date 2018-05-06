
import matplotlib.pyplot as plt
import os.path           

directory = os.path.dirname(os.path.abspath(__file__))  

filename = os.path.join(directory, 'RBO.jpg')
img = plt.imread(filename)
height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c]) > 600 :
            img[r][c] = [192, 255, 197]
        if sum(img[r][c]) > 180 and sum(img[r][c]) < 240:
            img[r][c] = [204, 51, 153]
        if sum(img[r][c]) > 480 and sum(img[r][c]) < 599:
            img[r][c] = [51, 153, 255]
        if sum(img[r][c]) > 290 and sum(img[r][c]) < 350:
           img[r][c] = [255, 255, 0]
        if sum(img[r][c]) < 10:
            img[r][c] = [0,0,0]
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')
fig.show()
