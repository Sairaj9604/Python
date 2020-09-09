def peak(a,lb,ub):
    mid=(lb+ub)//2
    if((mid==0 and a[mid]>a[mid+1]) or (mid==(len(a)-1) and a[mid]>a[mid-1]) or (a[mid+1]<a[mid] and a[mid-1]<a[mid])):
        return a[mid]
    elif(a[mid-1]>a[mid]):
        return peak(a,lb,mid-1)
    elif(a[mid+1]>a[mid]):
        return peak(a,mid+1,ub)
    else:
        return a[0]
a=list(map(int,input("Enter a List:").split()))
if(len(a)==1):
    b=a[0]
else:
    b=peak(a,0,len(a)-1)
    print("Peak Element is:",b)
