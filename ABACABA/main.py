# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

def main():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    prev="a"
    j=0
    
    for i in range(1,len(alphabet)):
        if (i==len(alphabet)):
            print("last:")
        print(prev)
        prev = prev+alphabet[i]+prev


if __name__ == "__main__":
    main()


'''
Time: O(2^m), Space: O(2^m), where m = len(alphabet).
'''
