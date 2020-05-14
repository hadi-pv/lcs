import time

def lcslength(s1,s2):
    str1=list(" "+s1)
    str2=list(" "+s2)
    len1=len(str1)
    len2=len(str2)
    check=[str1,str2]
    test = [[0] * (len1) for i in range(len2)]

    for j in range(1,len2):
        for i in range(1,len1):
            if str1[i]==str2[j]:
                test[j][i]=1+max(test[j-1][i],test[j][i-1])
            else:
                test[j][i]=max(test[j-1][i],test[j][i-1])

    return(test)

def lcs(s1,s2,llen):
    str1=list(s1)
    str2=list(s2)
    len1=len(str1)
    len2=len(str2)
    Len=-1
    str=""
    index=[]
    while(len1>0 and len2>0):
        if str1[len1-1]==str2[len2-1]:
            index.insert(Len,str1[len1-1])
            len1-=1
            len2-=1
            Len-=1
        elif(llen[len2-1][len1]>llen[len2][len1-1]):
            len2-=1
        else:
            len1-=1

    return(str.join(index),len(index))


start_time=time.perf_counter()

s1=input("enter the first input strings :")
s2=input("enter the second input strings :")
llen=lcslength(s1,s2)
lstring,llength=lcs(s1,s2,llen)
print("LCS of input sequence is",lstring,"of length",llength)

end_time=time.perf_counter()
print("time required",(end_time-start_time))
