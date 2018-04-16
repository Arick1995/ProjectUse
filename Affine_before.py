import numpy
from PIL import Image

a = numpy.array([[41,44,0,0,1,0],[0,0,41,44,0,1],[85,20,0,0,1,0],[0,0,85,20,0,1],[125,57,0,0,1,0],[0,0,125,57,0,1]])
b= numpy.array([22,754,294,676,550,754])
c = numpy.linalg.solve(a,b)

print(c)

pic1=Image.open("C:/Users/tkustaff/Desktop/Affine_DB/Back.jpg")
pic2=Image.open("C:/Users/tkustaff/Desktop/Affine_DB/lemonS.jpg")
A,h = pic2.size

wMax,hMax= pic1.size
w,h = pic2.size

apic1 = numpy.array(pic1)
apic2 = numpy.array(pic2)

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
