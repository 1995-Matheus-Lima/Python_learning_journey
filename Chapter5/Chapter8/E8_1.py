# ----- Part 1 done!
# def chop(L):
#     L.remove(L[0])
#     L.remove(L[-1])
#     print(L)
# mylist = ['1','2','3','4']
# t = chop(mylist)
# print(mylist)
# print(t)

# ----- Part 2 done!
def middle(L):
    l = L[1:-1]
    return l
mylist = ['1','2','3','4']
print(middle(mylist))