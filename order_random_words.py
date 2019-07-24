def your_order(string):
    word = ''
    ordered = []
    for n in string:
        if n != ' ':
            word += n
        else:
            for a in word:
                if int(a) >= 1 and int(a) <= 9:
                    ordered.insert(a, word)

def main():
    test = []
    test.append(your_order("is2 Thi1s T4est 3a"))
    test.append(your_order("Ri1ce r6ound served4 ofte3n 5in bowl7s. i2s"))
    test.append(your_order("throu7gh. fo6llow t2he and5 1Kick stra4ight ba3ll"))
    test.append(your_order("bea2uty bo9y. t7he of3 stu6nned vi5ew th4e young8 1The"))
    test.append(your_order("of3 u7s. f6aced Fo1ur wor5k stea4dy ho2urs"))
    test.append(your_order("1The f6rom t7he was3 sho2w ve8ry a4 f5lop st9art."))
    test.append(your_order("s6how W1e o3f ta2lked in7 th4e the8 c9ircus. sl5ide"))
    test.append(your_order("a9ir. 3of A1 wi2sp i6n bl8ue clo4ud the7 h5ung"))
    print(test)

main()