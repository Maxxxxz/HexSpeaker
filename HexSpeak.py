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

    # compile regexes
    res = []
    res.append(re.compile("[hjkmnpqruvwxyz]"))
    res.append(re.compile(r"(O|o)",))
    res.append(re.compile(r"(I|L|i|l)"))
    res.append(re.compile(r"(S|s)"))
    res.append(re.compile(r"(G)"))
    res.append(re.compile(r"(g)"))
    res.append(re.compile(r"(ate)"))
    res.append(re.compile(r"(T|t)"))

    newlines = []

    for line in lines:
        # remove line from list if it contains illegal characters that can not be converted
        match = res[0].search(line, re.IGNORECASE)
        if not match:
            line = res[1].sub("0", line)
            line = res[2].sub("1", line)
            line = res[3].sub("5", line)
            line = res[4].sub("6", line)
            line = res[5].sub("9", line)
            line = res[6].sub("8", line, re.IGNORECASE)
            line = res[7].sub("7", line)
            newlines.append(line)

        with open(".//outHex.txt", "w+") as f:
            all = '\n'.join(newlines)
            f.write(all)
    # if name contains forbidden letters i.e. only has ABCDEF
    # replace O -> zero, I | L -> one, S -> 5, T -> 7, G -> 6, g -> 9, ate -> 8 | a7e

if __name__ == "__main__":
    main()