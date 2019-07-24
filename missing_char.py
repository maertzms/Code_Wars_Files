def find_missing_letter(chars):
    missing_char = ''
    for n in chars:
        var = int(n)
        if int(n) != int(n) + 1:
            missing_char = char(int(n) + 1)
    return missing_char

def main():
    print("Hello World")
    data = ['a','b','c','d','f']
    find_missing_letter(data)
    data = ['O','Q','R','S']
    find_missing_letter(data)

main()