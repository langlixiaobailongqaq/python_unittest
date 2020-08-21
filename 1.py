def count(str1):
    length=len(str1)
    a=0
    for i in range(length):
        if str1[i] == "%":
            a+=1
    print("%%出现的次数为 %d 次" % a)
count("@@%%%%!!&&&")