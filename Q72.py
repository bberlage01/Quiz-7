#Bethany Berlage
def hash_spam(x,y):
    index=0
    total=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=1
            total+=1
        else:
            index+=1
    if total>=4:
        print("this tweet will be considered as a spam")


hash_spam("H#el#l#o th#er#e","#")
hash_spam("Hel#lo there","#")
