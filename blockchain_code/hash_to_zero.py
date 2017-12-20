from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
print(f'x is 5, what number will y be so that hash(x*y) ends up with 0 ?')

while True:
    print(f'Is y equal {y} ?')
    hash_result = sha256(f'{x*y}'.encode()).hexdigest()
    print(f'Hash of x*y = {x*y} is {hash_result}')

    if hash_result[-1] == "0":
        break
    else:
        y += 1
print(f'The solution is y = {y}')
