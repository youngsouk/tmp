n2ch = "".join([
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789+/",
])
ch2n = dict(zip(n2ch, range(len(n2ch))))
#print (ch2n)

def separate(seq, size):
    return (seq[i:i+size] for i in range(0, len(seq), size))

def decode(base64):
    print (base64)
    ns = []
    for ch in base64:
        if ch == "=": break
        ns.append(ch2n[ch])

    data = ""
    rem = len(ns) % 4 # padding 없을 시 추가
    if rem > 0: 
        ns += [0] * (4 - rem)
    print ("Base64 값", ns)

    t = ""
    for i in ns:
        t += bin(i) + " "
    print ("2진수 값", t)

    t = ""
    t2 = ""
    for i in range(0, len(ns), 4):
        b3 = (ns[i] << 18) | (ns[i + 1] << 12) | (ns[i + 2] << 6) | ns[i + 3]
        data += chr(b3 >> 16) + chr((b3 >> 8) & 0xff) + chr(b3 & 0xff)
        t += str((b3 >> 16) & 0xff) + " " + str((b3 >> 8) & 0xff) + " " + str(b3 & 0xff) + " "
        t2 += hex((b3 >> 16) & 0xff) + " " + hex((b3 >> 8) & 0xff) + " " + hex(b3 & 0xff) + " "
        pass
    print ("10진수 값", t)
    print ("16진수 값", t2)
    return data


def main():
    print (decode("cmFpbnlEaU1pR28="))


if __name__ == '__main__':
    main()