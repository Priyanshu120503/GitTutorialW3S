n = int(input(("Enter number of rows: "))
print('\n'.join(['*'*i + '  '*(2*(n-i)) + '* '*i for i in range(1, n+1)]))
