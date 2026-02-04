def solution(phone_book):
    L = len(phone_book)
    phone_book.sort(key=len)
    for i in range(L):
        for j in range(i+1,L):
            prefix = False
            for k,char in enumerate(phone_book[i]):
                if phone_book[i][k]!=phone_book[j][k]:
                    prefix = False
                    break
                elif phone_book[i][k]==phone_book[j][k]:
                    prefix = True
            if prefix:
                return False
                   
    return True


def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
                   
    return True