#   Michael Cooper
#   August 2019
#   hexspeak a file


def main():
    try:
        toHex = open(".//toHex.txt", "r+")
        lines = toHex.read().splitlines()
    except:
        print("File 'toHex.txt' does not exist.")
        exit(-1)
    finally:
        toHex.close()

    for line in lines:
       print(line)

    hexify(lines)

def hexify():
    pass
    # if name contains forbidden letters i.e. only has ABCDEF
    # replace O -> zero, I | L -> one, S -> 5, T -> 7, G -> 6, g -> 9, ate -> 8 | a7e



if __name__ == "__main__":
    main()