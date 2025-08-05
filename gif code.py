import imageio.v3 as io
filename=["img1.jpg","img2.jpg"]
image=[]
for fn in filename:
    image.append(io.imread(fn))
io.imwrite('me&dad.gif',image,duration=500,loop=0)

