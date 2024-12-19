import numpy as np

def convolution(grayimg,arr):
  #add zeros in the boundries:
  imgarr=np.zeros((grayimg.shape[0]+2,grayimg.shape[1]+2),dtype=int)
  imgarr2=np.zeros((grayimg.shape[0]+2,grayimg.shape[1]+2),dtype=int)
  #put the image inside the new array with zero boundries:
  imgarr[1:imgarr.shape[0]-1,1:imgarr.shape[1]-1]=grayimg[0:grayimg.shape[0],0:grayimg.shape[1]]
  imgarr2[1:imgarr2.shape[0]-1,1:imgarr2.shape[1]-1]=grayimg[0:grayimg.shape[0],0:grayimg.shape[1]]
  #add 1d 9 array to carry median:
  arr9=np.zeros([9],dtype=int)
  arr2=np.zeros([9],dtype=int)

  
  temp=arr[0][0]
  arr[0][0]=arr[0][2]
  arr[0][2]=temp

  temp=arr[1][0]
  arr[1][0]=arr[1][2]
  arr[1][2]=temp

  temp=arr[2][0]
  arr[2][0]=arr[2][2]
  arr[2][2]=temp



  temp=arr[0][0]
  arr[0][0]=arr[2][0]
  arr[2][0]=temp

  temp=arr[0][1]
  arr[0][1]=arr[2][1]
  arr[2][1]=temp

  temp=arr[0][2]
  arr[0][2]=arr[2][2]
  arr[2][2]=temp


  ii12=0
  for r in range(3):
    for c in range(3):
      arr2[ii12]=arr[r][c]
      ii12+=1
      


  i=0
  col_s=0
  col_e=3
  row_s=0
  row_e=3
  while row_e<=(imgarr.shape[0]):
    #iterating over the rows and columns of image with 3*3 mask:
    for r in range(row_s,row_e):
      for c in range(col_s,col_e):
        #putting 3*3 pixles into the 1d 9 columns array we made:
        arr9[i]=imgarr[r][c]*arr2[i]
        #saving the middle place of the 3*3 pixles in the image:
        if i==4:
          f=r
          s=c
        i+=1
    #iterating on every column until we reach the last one:
    if col_e<(imgarr.shape[1]):
      col_s+=1
      col_e+=1

    #if we reached the last column we go to next row and reset columns to zero-3 again:
    else:
      col_s=0
      col_e=3
      row_s+=1
      row_e+=1
    i=0
    #adding all values
    
    total=arr9[0]+arr9[1]+arr9[2]+arr9[3]+arr9[4]+arr9[5]+arr9[6]+arr9[7]+arr9[8]
    
    #equal add
    imgarr2[f][s]=total
  #deletethe zeros boundries:
  imgarr2=np.delete(imgarr2,0,0)
  imgarr2=np.delete(imgarr2,imgarr2.shape[0]-1,0)
  imgarr2=np.delete(imgarr2,0,1)
  imgarr2=np.delete(imgarr2,imgarr2.shape[1]-1,1)
  return imgarr2