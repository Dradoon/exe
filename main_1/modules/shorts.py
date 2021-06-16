path_abrivs="./imports/abrivs.txt"

def listcom(lis,mi,ma):
    j=""
    for i in range(mi,ma):
        j=j+lis[i]+" "
    return j    

def abrivs(a):
    a=a.split()
    f=open(path_abrivs,"r+")       
    while True:
        j=f.readline()
        if j!="":
            j=j.split()
            for i in range(0,len(a)):
                if j[0]==a[i]:
                    q=listcom(j,1,len(j))
                    a[i]=q
                else: pass
                    

        else:
            return(listcom(a,0,len(a)))
            break

