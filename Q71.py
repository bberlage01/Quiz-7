#Bethany Berlage
def count_hashtag(x,y):
    index=0
    total=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=1
            total+=1
        else:
            index+=1
    return total

print(count_hashtag("H#ello th#er#e","#"))
