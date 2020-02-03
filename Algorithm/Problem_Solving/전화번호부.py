def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i,len(phone_book)):
            if str(phone_book[i]) == str(phone_book[j])[0:len(str(phone_book[i]))]:
                return False

    return True


print(solution([119, 97674223, 1195524421]))