def reverseWords(s: str) -> str:
    list = s.split()
    list.reverse()
    o=" ".join(list)
    return o

if __name__ == "__main__":
    i = " the  sky is  blue "

    o = reverseWords(i)

    print ("|"+o+"|")
