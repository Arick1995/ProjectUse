import numpy
from PIL import Image

a = numpy.array([[22,754,0,0,1,0],[0,0,22,754,0,1],[294,676,0,0,1,0],[0,0,294,676,0,1],[550,754,0,0,1,0],[0,0,550,754,0,1]])
b= numpy.array([41,44,85,20,125,57])
c = numpy.linalg.solve(a,b)

print(c)

pic1=Image.open("C:/Users/tkustaff/Desktop/Affine_DB/Back.jpg")
pic2=Image.open("C:/Users/tkustaff/Desktop/Affine_DB/lemonS.jpg")
A,h = pic2.size

wMax,hMax= pic1.size
w,h = pic2.size

apic1 = numpy.array(pic1)
apic2 = numpy.array(pic2)

for i in range(hMax):
    for j in range(wMax):
        src = numpy.array([[j,i,0,0,1,0],[0,0,j,i,0,1]])
        ans = numpy.round(numpy.matmul(src,c),0)
        if ans[1] >= h or ans[0] >= w :
            continue
        if ans[1] < 0 or ans[0] < 0:
            continue
        r,g,b=apic2[int(ans[1]),int(ans[0])]
        if r >=200 and g >= 200 and b>=200:
            continue
        apic1[i,j] = apic2[int(ans[1]),int(ans[0])]
        
sImg = Image.fromarray(apic1,mode="RGB")
sImg.save("C:/Users/tkustaff/Desktop/Affine_DB/t2.jpg")
