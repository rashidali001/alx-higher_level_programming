#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    sum = 0

    if arg == 0:
        print('{}'.format(sum))
        exit()

    i = 1
    
    while i <= arg:
        sum = sum + int(sys.argv[i])
        i += 1

    print('{}'.format(sum))
