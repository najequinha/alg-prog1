n = int(input())
sum_in = 0
sum_out= 0

for i in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        sum_in += 1
    else:
        sum_out +=1

print(f"{sum_in} in\n{sum_out} out")
