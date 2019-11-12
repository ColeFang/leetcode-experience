import random
def get_matrix():
    m=int(input("How many points do you want?"))
    mat=[]
    for i in range(m):
        temp=[]
        for j in range(m):
            tempint=random.randint(0,1)
            temp.append(tempint)
        mat.append(temp)
    return mat
def get_root():
    m=int(input("Which points do you want to be the root? please enter the number"))
    return m
def get_base(mat):
    root=get_root()
    base=[]
    for i in range(len(mat)):
        if i==root:
            base.append(i)
        elif mat[i][root]==1 or mat[root][i]==1:
            base.append(i)
    return base
def new_matrix(mat,base):
    m=len(base)
    newmat=[]
    for i in range(m):
        temp=[]
        for j in range(m):
            temp.append(mat[base[i]][base[j]])
        newmat.append(temp)
    return newmat
def compute(mat,base):
    atemp=[]
    htemp=[]
    newmat=new_matrix(mat,base)
    for i in range(len(base)):
        atemp.append(1)
        htemp.append(1)
    temp=0
    m=len(base)
    while atemp[0]-temp>0.1 or atemp[0]-temp<-0.1:
        newa=[]
        newh=[]
        for i in range(m):
            a=0
            h=0
            for j in range(m):
                if newmat[j][i]==1:
                    a+=htemp[j]
                if newmat[i][j]==1:
                    h+=atemp[j]
            newa.append(a)
            newh.append(h)
        aa=[]
        hh=[]
        for each in newa:
            each=each/sum(newa)
            aa.append(each)
        for each in newh:
            each=each/sum(newh)
            hh.append(each)
        temp=atemp[0]
        atemp=aa
        htemp=hh

    print("the list of authority is")
    print(atemp)
    print("the list of hub is")
    print(htemp)
    return atemp


if __name__=='__main__':
    matrix=get_matrix()
    for i in matrix:
        print(i)
    base=get_base(matrix)
    print("the base point is")
    print(base)
    a=compute(matrix,base)
