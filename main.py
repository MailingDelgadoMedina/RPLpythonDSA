#  FOR LOOPS

# Sequence- ordering of expresions in your program
# Selection - making choices like if/else
# Iteration - loops
# All programing language have the 3 main control flow and with those you can write any algorithm.
#Tip: an "Off by one number is when a loop displays the itiration starting in 0 instead of 1"

#Example 1
for i in range(10):
  print(i + 1, "Hello World")

#Example 2
"""
for i in range(3):
    num =  eval(input('Enter a number: '))
    print('The square of your number is ', num + num)
print('The loop is done!')
"""

#Example 3 - the num before the coma states from the position the iteration will start (end=' ' keeps everything on the same line)
for i in range(5,0, -1):
  print(i, end=' ')
print('Blast off!!!')
#Example 4
for i in range(4):
  print('*'*(i+1))
  

  