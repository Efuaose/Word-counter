user_sent = input("Input words: ")

#strip removes the extra white spaces
user_sent = user_sent.strip(' ')

#split divides the words into their own personal spaces
list_of_words = user_sent.split(' ')

#len counts the number of words tat have been sparated
number_words =len(list_of_words)

print(number_words)


#.replace is used to replace letterss with thhe letter put in the racket 