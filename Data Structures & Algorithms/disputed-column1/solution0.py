
def main():
    n, m = map(int, input().split())
    strings = []

    for _ in range(n):
        strings.append(input().strip())

    print(strings)
    count=0
    for col in range(0,n):
        dis=set()
        for row in range(0,m):
            if strings[row][col]!="*":
                dis.add(strings[row][col])
        if len(dis)>1:
            count+=1
    print(count)
        

if __name__ == "__main__":
    main()
