import numpy as np
from numpy import linalg
from skimage import io

def solve(src_points, dst_points):
    x = np.array([
            [src_points[0][0], src_points[0][1], 0, 0, 1, 0],
            [0, 0, src_points[0][0], src_points[0][1], 0, 1],
            [src_points[1][0], src_points[1][1], 0, 0, 1, 0],
            [0, 0, src_points[1][0], src_points[1][1], 0, 1],
            [src_points[2][0], src_points[2][1], 0, 0, 1, 0],
            [0, 0, src_points[2][0], src_points[2][1], 0, 1],
        ])
    y = [
        [dst_points[0][0]],
        [dst_points[0][1]],
        [dst_points[1][0]],
        [dst_points[1][1]],
        [dst_points[2][0]],
        [dst_points[2][1]],
    ]
    transform = linalg.solve(x, y)
    return {'a': transform[:4].reshape(2,2), 'b': transform[4:]}

def linearTransform(x, y, transform):
    [[res_x], [res_y]] = np.rint(np.dot(transform['a'], [[x],[y]]) + transform['b']).astype(int)
    return [res_x, res_y]

workdir = 'C:/Users/tkustaff/Desktop/第15組_practice3/'

glass_img = io.imread(workdir + 'eyeglass.jpg')
huzi_img = io.imread(workdir + 'mustache.jpg')
face_img = io.imread(workdir + 'face.jpg')

glass_transform = solve([[0, 0], [glass_img.shape[1], 0], [glass_img.shape[1], glass_img.shape[0]]], [[200, 130], [375, 130], [375, 185]])
huzi_transform = solve([[0, 0], [huzi_img.shape[1], 0], [huzi_img.shape[1], huzi_img.shape[0]]], [[200, 200], [370, 200], [370, 240]])

''' glass '''
for x in np.arange(0, glass_img.shape[1]):
    for y in np.arange(0, glass_img.shape[0]):
        if (glass_img[y][x][0] == glass_img[y][x][1] == glass_img[y][x][2] == 255):
            continue
        [dst_x, dst_y] = linearTransform(x, y, glass_transform)
        face_img[dst_y][dst_x] = glass_img[y][x]

''' huzi '''
for x in np.arange(0, huzi_img.shape[1]):
    for y in np.arange(0, huzi_img.shape[0]):
        if (huzi_img[y][x][0] == huzi_img[y][x][1] == huzi_img[y][x][2] == 255):
            continue
        [dst_x, dst_y] = linearTransform(x, y, huzi_transform)
        face_img[dst_y][dst_x] = huzi_img[y][x]
        

face_img = face_img.astype(np.uint8)
io.imsave(workdir + 'result.jpg', face_img)


'''



for i in range(h):
    for j in range(w):
        src = numpy.array([[j,i,0,0,1,0],[0,0,j,i,0,1]])
        ans = numpy.round(numpy.matmul(src,c),0)
        if ans[1] >= hMax or ans[0] >= wMax :
            continue
        if a[1] < 0 or ans[0]<0:
            continue
        r,g,b=apic2[i,j]
        if r >=200 and g >= 200 and b>=200:
            continue
        apic1[int(ans[1]),int(ans[0])] = apic2[i,j]
        
sImg = Image.fromarray(apic1,mode="RGB")
sImg.save("C:/Users/tkustaff/Desktop/Affine_DB/t2.jpg")
'''
