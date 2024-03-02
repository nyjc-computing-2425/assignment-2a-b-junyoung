num = input('Enter a number (decimal or integer): ')
# type your code here

num_modified = num.strip().replace(".", "").lstrip("0")
sf = len(num_modified)

# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
