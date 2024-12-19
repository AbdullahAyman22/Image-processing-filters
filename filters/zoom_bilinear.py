import numpy as np


def zoom_bilinear(grayimg,size):
  enimage=grayimg
  for s in range(0,size-1):
    #multiplying clolumns (*2)-1:
    imgarr=np.zeros((enimage.shape[0],(enimage.shape[1]*2)-1),dtype=int)
    #row of enimage:
    f=0
    #column of enimage
    j=0
    #flag:
    m=1
    for i in range(0,imgarr.shape[0]):
      for k in range(0,imgarr.shape[1]):
        imgarr[i][k]=enimage[f][j]
        if m%2==0:
          if j<enimage.shape[1]-1:
            imgarr[i][k]=(int(enimage[f][j])+int(enimage[f][j+1]))/2
          j+=1
        m+=1
      #start from column 0 after finishing the row:
      j=0
      #reset the flag:
      m=1
      #increase the row of enimage(f) with the row of imgarr(i):
      f+=1

    imgarr2=np.zeros(((imgarr.shape[0]*2)-1,imgarr.shape[1]),dtype=int)

    j=0
    f=0
    m=1
    for i in range(0,imgarr2.shape[1]):
      for k in range(0,imgarr2.shape[0]):
        imgarr2[k][i]=imgarr[j][f]
        if m%2==0:
          if j<imgarr.shape[0]-1:
            imgarr2[k][i]=(imgarr[j][f]+imgarr[j+1][f])/2
          j+=1
        m+=1
      j=0
      m=1
      f+=1
    enimage=imgarr2

  return enimage


# imgarr2[0:255,0:511]=imgarr[0:255,0:511]
# imgarr2[256:511,0:511]=imgarr[0:255,0:511]




