#   Michael Cooper
#   August 2019
#   hexspeak a file

import re

def main():
    try:
        toHex = open(".//toHex.txt", "r+")
        lines = toHex.read().splitlines()
    except:
        print("File 'toHex.txt' does not exist.")
        exit(-1)
    finally:
        toHex.close()

    hexify(lines)

def hexify(lines):
    for line in lines:
        line = re.sub(r"(O|o)", "0", line)
        line = re.sub(r"(I|L|i|l)", "1", line)
        line = re.sub(r"(S|s)", "5", line)
        line = re.sub(r"(G)", "6", line)
        line = re.sub(r"(g)", "9", line)
        line = re.sub(r"(ate)", "8", line, re.IGNORECASE)
        line = re.sub(r"(T|t)", "7", line)
        print(line)
    # if name contains forbidden letters i.e. only has ABCDEF
    # replace O -> zero, I | L -> one, S -> 5, T -> 7, G -> 6, g -> 9, ate -> 8 | a7e

if __name__ == "__main__":
    main()