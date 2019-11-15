# Norma
#  unidump.py:
#
#  Skeleton code for H7-2: finish it
#
#  Prompt user to enter int N, then print out Unicode
#   characters from 32 through N-1, 32 per line, with
#   no intervening spaces.
#
#  At beginning of each line, print char number N of first char per line
#   in format: 'NNNN: '
#
#

N = int(input("Enter integer N: "))

for n in range(32,32+ N-1):
    if n % 32 == 0:  # start next line, then add linenum prefix
        if n < 100:
            print()
            print('00',n, ':', end='')
        elif n <1000:
            print()
            print('0',n, ':', end='')
        else:
            print()
            print(n, ':', end='')

    print(str(chr(n)), '', end='')

