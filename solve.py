def check(s):
    st = []
    k = len(s)

    for i in range(k):
        if s[i] == '(':
            st.append(s[i])
        elif s[i] == ')' and st:
            st.pop()
        else:
            return False

    if st:
        return False
    else:
        return True

n = int(input())
for i in range(n):
    lst = list(input())
    if check(lst):
        print("YES")
    elif check(lst) == False:
        print("NO")