import numpy as np

def histogram_equalization(grayimg):
  #put zeros to the boundries:
  imgarr=np.zeros((grayimg.shape[0]+2,grayimg.shape[1]+2),dtype=int)
  imgarr[1:imgarr.shape[0]-1,1:imgarr.shape[1]-1]=grayimg[0:grayimg.shape[0],0:grayimg.shape[1]]

  #array of size 256 to store pixles from 0 to 255:
  arr=np.zeros((256),dtype=int)

  # array to store how many gray pixel of this number
  arr2=np.zeros((256),dtype=int)

  #filling the array with values from 0 to 255
  for x in range(256):
    arr[x]=x


  i=0
  #for eaxh gray pixel in iterate on the whole image to find its frequency and put it in the same gray level place in arr2:
  for x in arr:
    for r in range(imgarr.shape[0]):
      for c in range(imgarr.shape[1]):
        if(imgarr[r][c]==arr[i]):
          arr2[i]+=1
    i+=1


  total=0
  #finding total:
  for x in arr2:
    total+=x
  
  #dividing each value by total
  dev_on_sum=np.zeros((256),dtype=float)
  for x in range(256):
    dev_on_sum[x]=arr2[x]/total
    #print(dev_on_sum[x])
  

  adding_before=np.zeros((256),dtype=float)

  for x in range(256):
    if(x==0):
      adding_before[x]=dev_on_sum[x]
    else:
      adding_before[x]=dev_on_sum[x]+adding_before[x-1]
    #print(dev_on_sum[x])


  sum_multiply_max_gray=np.zeros((256),dtype=int)

  for x in range(256):
    sum_multiply_max_gray[x]=round(255*adding_before[x])
  
  i=0
  for x in arr:
    for r in range(imgarr.shape[0]):
      for c in range(imgarr.shape[1]):
        if(imgarr[r][c]==arr[i]):
          imgarr[r][c]=sum_multiply_max_gray[i]
    i+=1



  #print(total)
  return imgarr

  