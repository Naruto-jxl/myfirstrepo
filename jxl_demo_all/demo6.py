# astr = "sSDsdSSDDFssssdfweqEWSWW"
# alist = filter(lambda x:x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],astr)
# print(list(alist))
import sys
def counts(arg):
    return sys.getrefcount(arg)
alist = [1,11,1]
print('alist',id(alist),counts(alist))
bli = alist
print('bli',id(bli),counts(alist))
cli = [1,11,1]

print('cli',id(cli),counts([1,11,1]))
print('[1,11,1]',id([1,11,1]))
# a = 123
# print('a',id(a))
# b = 123
# print('b',id(b))











