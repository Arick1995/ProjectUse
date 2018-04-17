import numpy as np
import os
from skimage import io
from numpy import linalg

'''Solve transform function'''
def solve(src_points, dst_points):
    '''Prepare x'''
    x = np.array([
        [src_points[0][0], src_points[0][1], 0, 0, 1, 0],
        [0, 0, src_points[0][0], src_points[0][1], 0, 1],
        [src_points[1][0], src_points[1][1], 0, 0, 1, 0],
        [0, 0, src_points[1][0], src_points[1][1], 0, 1],
        [src_points[2][0], src_points[2][1], 0, 0, 1, 0],
        [0, 0, src_points[2][0], src_points[2][1], 0, 1],
    ])
    '''Prepare y'''
    y = np.array([
        [dst_points[0][0]],
        [dst_points[0][1]],
        [dst_points[1][0]],
        [dst_points[1][1]],
        [dst_points[2][0]],
        [dst_points[2][1]],
    ])
    '''Solve using numpy linalg'''
    res = linalg.solve(x, y)
    '''return a is (2,2) matrix, and b is (2,1) matrix'''
    return {'a': np.array(res[:4]).reshape(2,2), 'b': res[4:]}

'''Transform using y = ax+b'''
def linearTransform(x, y, transform): 
    [[res_x], [res_y]] = np.rint(np.dot(transform['a'], [[x], [y]]) + transform['b']).astype(int)
    return [res_x, res_y]

'''Transform using x = -1a(y-b)'''
def linearTransformInv(x, y, transform):
    ainv = linalg.inv(transform['a'])
    [[res_x], [res_y]] = np.rint(np.dot(ainv, ([[x], [y]] - transform['b']))).astype(int)
    return [res_x, res_y]

'''Process downsampling'''
def downsampling(src_img, dst_img, transform, range):
    '''Process image in source range'''
    for x in np.arange(range[0][0], range[1][0]):
        for y in np.arange(range[0][1], range[1][1]):
            '''Calculate point to destenation image'''
            [dst_x, dst_y] = linearTransform(x, y, transform)
            '''Copy image pixel'''
            dst_img[dst_y][dst_x] = src_img[y][x]
    return dst_img.astype(int)

'''Process upsampling'''
def upsampling(src_img, dst_img, transform, range):
    '''Calculate range in destenation image'''
    dst_range = [linearTransform(range[0][0], range[0][1], transform), linearTransform(range[1][0], range[1][1], transform)]
    '''Process image in destenation range'''
    for dst_x in np.arange(dst_range[0][0], dst_range[1][0]):
        for dst_y in np.arange(dst_range[0][1], dst_range[1][1]):
            '''Calculate point in source image'''
            [x, y] = linearTransformInv(dst_x, dst_y, transform)
            '''Copy image pixel'''
            dst_img[dst_y][dst_x] = src_img[y][x]
    return dst_img.astype(int)

'''Get current location and generate file path'''
dir = os.path.dirname(__file__)
src_path = os.path.join(dir, 'head.jpg')
dst_path = os.path.join(dir, 'result.jpg')

'''Generate 3 Transform function for 3 areas'''
transform1 = solve([[0, 0], [1000, 0], [1000, 500]], [[0, 0], [1000, 0], [1000, 200]])
transform2 = solve([[0, 500], [1000, 500], [1000, 900]], [[0, 200], [1000, 200], [1000, 1000]])
transform3 = solve([[0, 900], [1000, 900], [1000, 1348]], [[0, 1000], [1000, 1000], [1000, 1348]])

'''Load source image and generate black destenation image'''
src_img = io.imread(src_path)
dst_img = np.zeros(src_img.shape)

'''Process 3 areas'''
dst_img = downsampling(src_img, dst_img, transform1, np.array([[0, 0], [1000, 500]]))
dst_img = upsampling(src_img, dst_img, transform2, (np.array([[0, 500], [1000, 900]])))
dst_img = downsampling(src_img, dst_img, transform3, np.array([[0, 900], [1000, 1348]]))

'''Save image'''
io.imsave(dst_path, dst_img.astype(np.uint8))
