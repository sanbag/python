def compression (strr):
    out = ''
    dict={}
    for i in strr:
        dict[i] =dict.get(i,0)+1

    for key,val in dict.items():
        out+= str(val)+key

    print(out)
compression('santoshaa')

def five_time_occurence(strr):
    out = ''

    dict={}
    for i in strr:
        dict[i] =dict.get(i,0)+1

    for key,val in dict.items():
        while val>0:
            out += str(min(val,5))+key
            val -= 5
    print(out)

five_time_occurence('aaaaaaaaaaaaaabbbbbbbbb')


def maintain_order(strr):
    out = ''
    count =1

    for i in range(len(strr)-1):
        if strr[i]==strr[i+1]:
            count+=1
        else:
            out+= str(count)+strr[i]

    out+=str(count)+strr[i]
    print(out)

maintain_order('abaaa')

