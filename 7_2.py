#7-2
def binary_search(n_list, target, s ,e):
    m = (s +e) //2

    if s > e:
        return  False

    if target == n_list[m]:
        return True

    elif target > n_list[m]:
         return binary_search(n_list, target,m+1, e) #return 안하니깐 이상한 답이 나옴
    else:
         return binary_search(n_list, target,s, m-1)

N = int(input())
N_list =  list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list =  list(map(int, input().split()))

e = len(N_list) - 1
m = e // 2

for i in M_list:
	if True == binary_search(N_list, i, 0, e):
		print("yes")
	elif False == binary_search(N_list, i, 0, e):
		print("no")
