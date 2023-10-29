N = int(input())

cnt = 0

r_cnt, l_cnt = (int(s) for s in input().split())

right = []
left = []

right = input().split()
left = input().split()

for i in right:
    if i in left: cnt += 1

print(N-cnt)