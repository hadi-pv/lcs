from time import *
from threading import *


class stringComparison:

    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
        self.test = [[0] * (len(self.s1)+1) for i in range(len(self.s2)+1)]
        self.c=Condition()

    def ltest(self):
        self.c.acquire()
        str1=list(" "+self.s1)
        str2=list(" "+self.s2)
        len1=len(str1)
        len2=len(str2)

        for j in range(1,len2):
            for i in range(1,len1):
                if str1[i]==str2[j]:
                    self.test[j][i]=1+max(self.test[j-1][i],self.test[j][i-1])
                else:
                    self.test[j][i]=max(self.test[j-1][i],self.test[j][i-1])

        self.c.notify()
        self.c.release()

class stringComparison2:

    def __init__(self,test):
        self.test=test


    def lcs(self):
        self.test.c.acquire()
        self.test.c.wait(timeout=0)
        llen=self.test.test
        str1=list(self.test.s1)
        str2=list(self.test.s2)
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

        print("LCS of input sequence is",str.join(index),"with length",len(index))
        self.test.c.release()


s1=input("enter the first input strings :")
s2=input("enter the second input strings :")
start_time=perf_counter()
obj1=stringComparison(s1,s2)
obj2=stringComparison2(obj1)
t1=Thread(target=obj1.ltest)
t1.start()
t2=Thread(target=obj2.lcs)
t2.start()
sleep(0.05)
end_time=perf_counter()
print("time required to run the code :",(end_time-start_time)-(0.05))
