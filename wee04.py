

# Finds the shortest word 
def shortest_word(words: list[str]) -> str:
  #returns None if list is invalid
  result = None 
  if words:
    #starts the loop on the first word and assumes its the shortest
    result = words[0] 
    #loops through every word on the list
    for word in words:
      # if the current word in the loop is shorter it replaces result
      if len(word) < len(result):
        result = word
  #returns the shortest word or None 
  return result
#calls the function shortest_word
print(shortest_word)

# Finds the longest word 
def longest_word(words: list[str]) -> str:
  #returns None if list is invalid
  result = None 
  if words:
    #starts the loop on the first word and assumes its the longest
    result = words[0] 
    #loops through every word on the list
    for word in words:
      # if the current word in the loop is longer it replaces result
      if len(word) > len(result):
        result = word
  #returns the longest word or None 
  return result
#calls the function longest_word
print(longest_word)

# Finds odd words
def odd_words(words: list[str]) -> list[str]:
  #returns None if list is invalid
  result = None
  #checks that there is an input
  if words:
    #creates an empty list named result to store words with an odd number of characters
    result = []
    #makes a loop to go through every word on the list
    for word in words: 
      #checks if the word is odd by taking the remainder and dividing it by 2, if it's not zero its odd
      if len(word) % 2 != 0:
        #adds the word to the empty list if it is odd
        result.append(word)
  #returns the result list of odd words
  return result
#calls the function odd_words
print(odd_words)

# Finds average words
def average_words(words: list[str]) -> list[str]:
  #returns None if list is invalid
  result = None
  #verifies that there's an input
  if words and len(words) > 0:
    #a placeholder for the total number of chracters
    total = 0
    #a placeholder for how many words are in the list
    count = 0
    # A loop to go trhough the words and calculate total length and count
    for word in words:
      #adds the length of the current word to total
      total += len(word)
      #increases word count by 1
      count += 1
    # This calculates the average length
    average = total // count
    # this creates an empty list were words whose length is +- 1 from the average length will be put
    result = []
    for word in words:
      length = len(word)
      if length == average -1 and length == average + 1:
        result.append(word)
  return result 
#calls the function average_words 
print(average_words)

# Finds an intersection
def intersect(foo: list[str], bar: list[str]) -> bool:
  # start with an ssumption that there is no match so that it can change if there is one
  result = False
  # checks if both lists are valid
  if foo and bar: 
    #checks if the word is in the first list
    for word in foo:
      #checks if the word is also in the 2nd list
      if word in bar:
        # finds a match and statemnt switches to True
        result = True 
  # returns True if 1 match is found but False otherwise
  return result
#calls the function intersect
print(intersect)



#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
