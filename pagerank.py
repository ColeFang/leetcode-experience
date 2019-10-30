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
def preprocess(mat):
    for j in range(len(mat)):
        number=0
        for i in range(len(mat)):
            number+=mat[i][j]
        for i in range(len(mat)):
            if number==0:
                continue
            else:
                mat[i][j]/=number
def rank(mat):
    l=len(mat)
    start_list = []
    for i in range(l):
        start_list.append(1/l)
    while(True):
        new_list=[]
        for i in range(l):
            new=0
            for j in range(l):
                new+=start_list[i]*mat[i][j]
            new_list.append(new)
        if new_list[0]-start_list[0]<=0.1 or min(new_list)<=0.1:
            start_list = new_list
            break
        start_list=new_list
    return start_list
def print_matrix(mat):
    for i in range(len(mat)):
        print(mat[i])

if __name__=='__main__':
    matrix=get_matrix()
    preprocess(matrix)
    print_matrix(matrix)
    last_list=rank(matrix)
    print(last_list)
