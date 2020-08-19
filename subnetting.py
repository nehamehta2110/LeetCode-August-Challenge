def check_region_subnet(m,i,j):
    flag = False
    if int(m[0]) >=int(i[0]) and int(m[0])<=int(j[0]):
        if  int(m[0])<int(j[0]):
            if int(m[1]) >=int(i[1]):
                flag=True
        elif int(m[0])==int(j[0]):
            if int(m[1])<int(j[1]):
                flag=True
            elif int(m[1])==int(j[1]):
                if int(m[2])<int(j[2]):
                    flag=True
                elif int(m[2])==int(j[2]):
                    if int(m[3])<int(j[3]):
                        flag=True
    return flag


def main():
    num = list(map(int,input().split()))
    num_reg = num[0]
    num_test = num[1]
    f = False
    s=[]
    u=[]
    for q in range(num_reg):
        # s[q]=list(map(str,input().split()))
        s.append(input())
    for r in range(num_test):
        u.append(input())
    for k in range(num_test):
        f=False
        t = u[k].split('.')
        for v in range(len(s)):
            f=False
            inp=s[v].split(" ")
            i = inp[0].split('/')[0].split('.')
            j = inp[1].split('/')[0].split('.')
            if check_region_subnet(t, i, j):
                f=True
                print(inp[2])


        if f==False:
            print("None")


if __name__ == '__main__':
    main()




