def encode(msg, key):
    original = []
    cipher_list = []
    encoded = []
    for i in msg:
        original += [ord(i)]
    for i in original:
        cipher = i + key
        cipher_list.append(cipher)
    for i in cipher_list:
        encoded += [chr(i)]

    new_list = ''.join(encoded)
    return new_list


def encode_better(msg, key):
    encoded_str = ''
    for i in range(len(msg)):
        msg_ord = (ord(msg[i])) - 65
        key_ord = (ord(key[i % len(key)])) - 65
        total = (msg_ord + key_ord) % 58
        new_ord = total + 65
        encoded_chr = (chr(new_ord))
        encoded_str = encoded_str + encoded_chr
        return encoded_str
