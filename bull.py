def translate(lista ,i):
    listb = []
    num = 0
    if i < 30:
        for j in range (len(lista)):
            if j == 0:
                num += 1
            elif lista[j] != lista[j-1]:
                listb.append(num)
                num = 1
                listb.append(lista[j-1])
            else:
                num += 1
        listb.append(num)        
        listb.append(lista[j])   
        return translate(listb,i+1)
    else:
        return lista

if __name__ == "__main__":
    
    a = [1]
    answer = ""
    b = translate(a,0)
    for i in range(len(b)):
        answer += str(b[i])
    print len(translate(a,0))
