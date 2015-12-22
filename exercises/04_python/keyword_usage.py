
def keyword_usage(text,lst):
    arr=list()
    textsplit=text.split(" ")
    for i in lst:
        if (i in textsplit):
            arr.append(True)
        else:
            arr.append(False)
    arr=tuple(arr)
    return arr
res = keyword_usage('Dive  Into  Python',  ['Python',  'python', 'scala'])
print (res)
