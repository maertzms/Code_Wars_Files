def persistence(n):
    # your code
    runs = 0
    if len(n) == 1:
        return runs
    else:
        runs += 1
        mult(n, runs)
        
        
def mult(num, runs):
    