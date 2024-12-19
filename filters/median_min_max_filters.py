import numpy as np





def median_min_max_filters(grayimg, num, iterations):
    for x in range(iterations):
        
        #add zeros in the boundries:
        imgarr=np.zeros((grayimg.shape[0]+2,grayimg.shape[1]+2),dtype=int)
        imgarr2=np.zeros((grayimg.shape[0]+2,grayimg.shape[1]+2),dtype=int)
        #put the image inside the new array with zero boundries:
        imgarr[1:imgarr.shape[0]-1,1:imgarr.shape[1]-1]=grayimg[0:grayimg.shape[0],0:grayimg.shape[1]]
        imgarr2[1:imgarr2.shape[0]-1,1:imgarr2.shape[1]-1]=grayimg[0:grayimg.shape[0],0:grayimg.shape[1]]
        #add 1d 9 array to carry median:
        arr9=np.zeros([9],dtype=int)
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
                    arr9[i]=imgarr[r][c]
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
        #sorting the 1d 9 columns array then put the median in the middle of the 3*3 pixels in the original image:
            if num==4 or num==0 or num==8:
                rr=8
                ii=0
                
                for x in range(8):
                    for y in range(rr):
                        if arr9[ii]>arr9[ii+1]:
                            temp=arr9[ii]
                            arr9[ii]=arr9[ii+1]
                            arr9[ii+1]=temp
                        ii+=1
                    ii=0
                    rr-=1

                    
                   
                #arr9.sort()
                imgarr2[f][s]=arr9[num]
            elif num==1:
                av=np.average(arr9)#arr9[0]
                imgarr2[f][s]=av
            else:
                gaussian=np.zeros([9],dtype=int)
                gaussian[0]=1
                gaussian[1]=2
                gaussian[2]=1
                gaussian[3]=2
                gaussian[4]=4
                gaussian[5]=2
                gaussian[6]=1
                gaussian[7]=2
                gaussian[8]=1
                gaussian=np.reshape(gaussian,(3,3)) 
                 
                arr9_ed=np.reshape(arr9,(3,3))
                multip=(np.multiply(gaussian,arr9_ed))
                filter=np.sum(multip)/16
                                
                imgarr2[f][s]=int(filter)
              

        imgarr2=np.delete(imgarr2,0,0)
        imgarr2=np.delete(imgarr2,imgarr2.shape[0]-1,0)
        imgarr2=np.delete(imgarr2,0,1)
        imgarr2=np.delete(imgarr2,imgarr2.shape[1]-1,1)
        # Update the grayimg for the next iteration:
        grayimg = imgarr2  
    return imgarr2