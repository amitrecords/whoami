def Preprocessing_msg(data):
    names=['Amit','Charlie','Debbie','Jim','Triveni']
    unames=['amit','charlie','dsk','jim','triveni']
    ctr=0
    labels=[]
    messages=[]
    noise=0
    for line in data:
        seg= line.strip().lower().replace('<','').split('>')
        #print(seg)
        if len(seg) < 2:
            #print(seg)
            noise +=1
        elif len(seg) > 2:
            #print(seg)
            noise += 1
        else:
            for name in unames:
                if name in seg[0]:
                    labels.append(names[unames.index(name)])
                    messages.append(seg[1])
                    ctr+=1
    return messages, labels

#hlogs = open('logs.log',"r")
#data = hlogs.readlines()
#X,y = Preprocessing_msg(data)
#print(y)