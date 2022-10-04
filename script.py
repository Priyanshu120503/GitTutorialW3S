n = int(input("Enter number of rows: "))
print('\n'.join(['*'*i + '  '*(2*(n-i)) + '* '*i for i in range(1, n+1)]))

print()

print('\n'.join(['  '*(n-i) + '* '*i for i in range(1,n+1)]))

f = []
i = 2
num = n
while n!=1:
  if n%i==0:
    f.append(i)
    n //= i
  else: i+=1
print(f'Prime Factors of {num} are: {f}') 
