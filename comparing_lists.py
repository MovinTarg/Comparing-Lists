i = [1,2,5,6,2]
j = [1,2,5,6,2]

k = [1,2,5,6,5]
l = [1,2,5,6,5,3]

m = [1,2,5,6,5,16]
n = [1,2,5,6,5]

o = ['celery','carrots','bread','milk']
p = ['celery','carrots','bread','cream']


def compareLists (varListA, varListB):
    a = set(varListA)
    b = set(varListB)
    # print a^b
    if a^b == set([]):
        print "The lists are the same."
    else:
        print "The lists are not the same."    
compareLists(o, p)