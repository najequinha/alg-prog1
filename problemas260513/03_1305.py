def verificar(seq: list, k: int) -> int:
    cont = 0
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if j < i:
                continue
            if seq[i] + seq[j] == k:
                cont += 1
                
    return cont

def main():
    seq = list(map(int, input().split()))
    k = int(input())
    res = verificar(seq, k)
    print(res)
    
main()
    


