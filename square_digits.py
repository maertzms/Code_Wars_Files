def square_digits(num):
  sqr_num = ''
  for n in str(num):
    sqr_num += str(int(n) ** 2)
  return int(sqr_num)

def main():
  print(square_digits(9119))
  print(square_digits('2112'))

main()