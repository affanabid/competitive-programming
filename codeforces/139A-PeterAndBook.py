def sol(pages, days):
    while pages > 0:
        for i in range(7):
            pages = pages - days[i]
            if pages <= 0:
                return i + 1
            
        

def main():
    p = int(input())
    d = list(map(int, input().split()))
    print(sol(p, d))



main()
