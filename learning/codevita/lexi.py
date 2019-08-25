def dictionary(P):
    dictord = {}
    lst = [a for a in range(1,27)]
    P = list(P)
    for s,i in zip(P,lst):
        dictord[s] = i   
    return dictord

def sort_string(dictord, S):
    S = list(S)
    for i in range(0,len(S)):
        for j in range(i+1,len(S)):
            if dictord[S[i]] > dictord[S[j]]:
                temp = S[i]
                S[i] = S[j]
                S[j] = temp
    return ''.join(S)

def main():
    try:
        flag = 1
        while flag:
            T = int(input('enter no of test cases:'))
            P = []
            S = []
            if T<0 or T>1000:
                    print('enter an integer')
                    main()
            for i in range(0,T):
                P.append(input('enter dictionary order: ').lower())
                S.append(input('enter string: ').lower())
    #            P = 'abcdefghijklmnopqrstuvwxzy'
                if len(P[i]) != 26:
                    print('length should be 26')
                    main()
                elif len(S[i])<0 or len(S[i]) > 100:
                    print('length should be 1 to 100')
                    main()
                else:
                    flag = 0
    except:
        print('enter a number please')
        main()
    
    for i in range(0,T):
        dictord = dictionary(P[i])
        sortstr = sort_string(dictord, S[i])
        print(sortstr)
        
        
if __name__ == "__main__":
    main()
            
        

