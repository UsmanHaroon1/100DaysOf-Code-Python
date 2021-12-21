alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

res = []
def encrypt(text, shift):
    res.clear()
    for l in text:
        if(l==' '):
            res.append(' ')
            continue;
        nidx = alphabet.index(l) + shift
        if (nidx >= 26):
           nidx = nidx - 26
        res.append(alphabet[nidx])
    return res
def decrypt(text,shift):
    res.clear()
    for l in text:
        if (l == ' '):
            res.append(' ')
            continue;
        nidx = alphabet.index(l) - shift
        if (nidx < 0):
           nidx = nidx + 26
        res.append(alphabet[nidx])
    return res

def caesar(start_text,shift,direction):
    res.clear()
    shift=shift%len(alphabet)
    if(direction=="decode"):
        shift*=-1
    for l in start_text:
        if (l not in alphabet):
            res.append(l)
            continue;
        nidx = alphabet.index(l) + shift
        res.append(alphabet[nidx])
    return res

import art

print(art.logo)

direction=""
while(direction != "exit"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to Exit:\n").lower()

    if (direction != "encode" and direction != "decode"):
        if(direction != "exit"):
            print("Wrong choice!!,Please choice again")
        continue;
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"The {direction}d text is:{''.join(caesar(text, shift,direction))}")

print("Exit!!")

