num = input('Enter a number (decimal or integer): ')
# type your code here

#Sanitise the input
  #take away spaces before and after with the value tool: .strip
  #remove the dot with tool: replace
  #strip the 0s on the left with tool: .lstrip
num_modified = num.strip().replace(".", "").lstrip("0")

#Count length
  #tool: len()
sf = len(num_modified)



# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
