def tickets(people):
    cash = 0
    able = True
    for given in people:
        if    given == 25:
            cash += 25
        elif  cash >= given - 25 and given >= 25:
            cash += given
            cash -= given - 25
        else:
          able = False
          return "NO"
    if able: return  "YES"

def main():
    tickets([25, 26, 50])
    tickets([25, 100])
    tickets([100, 24])
    tickets([25, 50.5, 75, 100])


main()
