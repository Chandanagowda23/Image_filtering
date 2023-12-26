import cv2
import numpy as np

#____________________________________________________________________#
# ### Convolution: 
image = cv2.imread('Noisy_image.png', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9

padded_image = np.zeros([215,206])
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image

matrix_dummy = np.zeros([215,206])

for i in range(1, matrix_dummy.shape[0]-1):
    for j in range(1, matrix_dummy.shape[1]-1):
        row, column = 1, 1
        a = padded_image[i-1][j-1] * kernel[row+1][column+1] 
        b = padded_image[i-1][j] * kernel[row+1][column]
        c = padded_image[i-1][j+1] * kernel[row+1][column-1] 
        d = padded_image[i][j-1] *  kernel[row][column-1]
        e = padded_image[i][j] *  kernel[row][column] 
        f = padded_image[i][j+1] *  kernel[row][column+1]
        g = padded_image[i+1][j-1] *  kernel[row+1][column-1]
        h = padded_image[i+1][j] *  kernel[row+1][column]
        n = padded_image[i+1][j+1] *  kernel[row+1][column+1]
        lst = sum(list([a,b,c,d,e,f,g,h,n]))
        matrix_dummy[i][j] = lst
        
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image
image_convol = matrix_dummy[1:matrix_dummy.shape[0]-1, 1:matrix_dummy.shape[1]-1]
cv2.imwrite('convolved_image.png', image_convol)


# ### Averaging Filter: 

image = cv2.imread('Noisy_image.png', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9

padded_image = np.zeros([215,206])
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image

matrix_dummy = np.zeros([215,206])

for i in range(1, matrix_dummy.shape[0]-1):
    for j in range(1, matrix_dummy.shape[1]-1):
        row, column = 1, 1
        a = padded_image[i-1][j-1] * kernel[row-1][column-1]
        b = padded_image[i-1][j] * kernel[row-1][column]
        c = padded_image[i-1][j+1] * kernel[row-1][column+1]
        d = padded_image[i][j-1] *  kernel[row][column-1]
        e = padded_image[i][j] *  kernel[row][column] 
        f = padded_image[i][j+1] *  kernel[row][column+1]
        g = padded_image[i+1][j-1] *  kernel[row+1][column-1]
        h = padded_image[i+1][j] *  kernel[row+1][column]
        n = padded_image[i+1][j+1] *  kernel[row+1][column+1]
        lst = sum(list([a,b,c,d,e,f,g,h,n]))
        matrix_dummy[i][j] = lst
        
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image
image_convol = matrix_dummy[1:matrix_dummy.shape[0]-1, 1:matrix_dummy.shape[1]-1]
cv2.imwrite('average_image.png', image_convol)


# ### Gaussian Filter: 

image = cv2.imread('Noisy_image.png', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])/16

padded_image = np.zeros([215,206])
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image

matrix_dummy = np.zeros([215,206])

for i in range(1, matrix_dummy.shape[0]-1):
    for j in range(1, matrix_dummy.shape[1]-1):
        row, column = 1, 1
        a = padded_image[i-1][j-1] * kernel[row-1][column-1]
        b = padded_image[i-1][j] * kernel[row-1][column]
        c = padded_image[i-1][j+1] * kernel[row-1][column+1]
        d = padded_image[i][j-1] *  kernel[row][column-1]
        e = padded_image[i][j] *  kernel[row][column] 
        f = padded_image[i][j+1] *  kernel[row][column+1]
        g = padded_image[i+1][j-1] *  kernel[row+1][column-1]
        h = padded_image[i+1][j] *  kernel[row+1][column]
        n = padded_image[i+1][j+1] *  kernel[row+1][column+1]
        lst = sum(list([a,b,c,d,e,f,g,h,n]))
        matrix_dummy[i][j] = lst
        
padded_image[1:padded_image.shape[0]-1, 1:padded_image.shape[1]-1] = image
image_convol = matrix_dummy[1:matrix_dummy.shape[0]-1, 1:matrix_dummy.shape[1]-1]
cv2.imwrite('gaussian_image.png', image_convol)


# ### Median Filter: 
image = cv2.imread('Noisy_image.png', cv2.IMREAD_GRAYSCALE)

padded_image = np.zeros([217,208])
padded_image[2:padded_image.shape[0]-2, 2:padded_image.shape[1]-2] = image

matrix_dummy = np.zeros([217,208])

for i in range(2, matrix_dummy.shape[0]-2):
    for j in range(2, matrix_dummy.shape[1]-2):
        a1 = padded_image[i-2][j-2]
        a2 = padded_image[i-2][j-1] 
        a3 = padded_image[i-2][j] 
        a4 = padded_image[i-2][j+1] 
        a5 = padded_image[i-2][j+2] 
        a6 = padded_image[i-1][j-2] 
        a7 = padded_image[i-1][j-1] 
        a8 = padded_image[i-1][j]
        a9 = padded_image[i-1][j+1]
        a10 = padded_image[i-1][j+2]
        a11 = padded_image[i][j-2]
        a12 = padded_image[i][j-1]
        a13 = padded_image[i][j]
        a14 = padded_image[i][j+1]
        a15 = padded_image[i][j+2]
        a16 = padded_image[i+1][j-2]
        a17 = padded_image[i+1][j-1]
        a18 = padded_image[i+1][j]
        a19 = padded_image[i+1][j+1]
        a20 = padded_image[i+1][j+2]
        a21 = padded_image[i+2][j-2]
        a22 = padded_image[i+2][j-1]
        a23 = padded_image[i+2][j]
        a24 = padded_image[i+2][j+1]
        a25 = padded_image[i+2][j+2]

        lst = list([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25])
        strd_lst = sorted(lst)
        matrix_dummy[i][j] = strd_lst[12]
        
image_convol = matrix_dummy[2:matrix_dummy.shape[0]-2, 2:matrix_dummy.shape[1]-2]
cv2.imwrite('median_image.png', image_convol)

# ###  Contrast and Brightness Adjustment: 

image = cv2.imread('Uexposed.png')
new_image = np.zeros(image.shape)

fact_contrast = 5
fact_brightness = 100

for i in range(image.shape[0]): 
    for j in range(image.shape[1]): 
        for k in range(image.shape[2]):
            new_image[i,j,k] = np.clip(fact_contrast*image[i,j,k] + fact_brightness, 0 ,255)
            
cv2.imwrite('adjusted_image.png', new_image)
