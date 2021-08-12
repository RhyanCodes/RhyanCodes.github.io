print("Part A")
print(' ')
myList = ['duck', 'pork', 'mango', 'boba tea', 'chicken', 'beef', 'noodle', 'sushi']
print(myList)

myList2 = myList[1:]
print(myList2)

myList2.append('milk tea')
print(myList2)

del myList2[2]
print(myList2)

myList3 = myList2
print(myList3)

print(' ')
print('Part B')
print(' ')
print('1. count(sub,[start,[end]]) will count the number of instances the substring or sub appears in the string. The start and end represent the index position to begin and end at.')
str = 'How now brown cow?'
sub = 'o'
print('The string is: ', str, 'and the sub is: ', sub)
print('str.count(sub,0,20): ', str.count(sub,0,20))
print(' ')

print('2. endswith(suffix,[start,[end]]) will return True if a string ends with the specified suffix and False if it does not. Start and end indicate where to begin and end.)')
car = 'driving'
suffix = 'ing'
print('The string is: ', car, 'and the suffix is: ',  suffix)
print('car.endswith(suffix,0,10): ',car.endswith(suffix,0,10))
print(' ')

print('3. index(sub,[start,[end]]) will return the index position of the substring or sub. Start and end indicate where to begin and end.')
dinner = 'Tonight we will eat beef with rice and beans.'
sub1 = 'beef'
print('The string is: ', dinner, 'and the sub is: ', sub1)
print('dinner.index(sub1, 0, 40): ',dinner.index(sub1, 0, 40))
print(' ')

print('4. find(sub,[start,[end]]) will return the index position of the first instance of the substring or sub. Start and end indicate where to begin and end.')
beach = 'The beach boardwalk is the tourist attraction of Manhattan Beach.'
sub2 = 'beach'
print('The string is: ', beach, 'and the sub is: ', sub2)
print('beach.index(sub2, 0, 50): ', beach.index(sub2, 0, 50))
print(' ')

print('5. isalnum() will return True if the string has (a-z) or (0-9) characters and False if it does not.')
txt = 'CUNY2022'
print('The string is: ', txt)
print('.isalnum() will return: ',txt.isalnum())
print(' ')

print('6. isalpha() will return True if the string has (a-z) characters only and False otherwise.')
txt1 = 'Coding'
print('The string is: ', txt1)
print('.isalpha() will return: ',txt1.isalpha())
print(' ')

print('7. isdigit() will return True if the characters are all (0-9) and False if otherwise.')
digit = '999999'
print('The string is: ', digit)
print('.isdigit() will return: ', digit.isdigit())
print(' ')

print('8. islower() will return True if the characters are all lowercase and False if otherwise.')
txt2 = 'software'
print('The string is: ', txt2)
print('.islower() will return: ', txt2.islower())
print(' ')

print('9. isspace() will return True if the characters are all blank space and False if otherwise.')
txt3 = '     ' 
print('The string is: ', txt3)
print('.isspace() will return: ', txt3.isspace())
print(' ')

print('10. istitle() will return True if ONLY the first letter for each word in a string is uppercase and False if otherwise.')
txt4 = 'Yankees Win The World Series' 
print('The string is: ', txt4)
print('.istitle() will return: ', txt4.istitle())
print(' ')

print('11. isupper() will return True if all the characters in a string are uppercase and False if otherwise.')
txt5 = 'ALLCAPS' 
print('The string is: ', txt5)
print('.isupper() will return: ', txt5.isupper())
print(' ')

print('12. join() will take all the items in an iterable object and join them into a string. Add an empty string at the start of .join() to use that to separate the objects with a space.')
list = ['The', 'Army', 'and', 'the', 'Navy']
print('The iterable is: ', list)
print(' " ".join(list) will return: ',' '.join(list))
print(' ')

print('13. lower() will make all the characters in a string lowercase.')
txt6 = 'ALLCAPS AND MOON'
print('The string is: ', txt6)
print('txt6.lower() will return: ',txt6.lower())
print(' ')

print('14. replace(old,new,[count]) will search for an old string and replace it with a new one. The count represents the number of instances of the old text you want to replace.')
txt7 = 'I prefer to code in Java.' 
print('The string is: ', txt7)
print('txt7.replace("Java", "Python", 1) will return: ',txt7.replace('Java', 'Python', 1))
print(' ')

print('15. split([sep,[maxsplit]]) will split a string into a list. The sep is the separator Python will use to split the string and maxsplit is the number of splits.')
txt8 = 'I need a vacation in Jamaica.' 
print('The string is: ', txt8)
print('txt8.split(' ') will return: ',txt8.split(' '))
print(' ')

print('16. splitlines([keepends]) will split a string by each new line. keepends takes True or False and if True is used it will show things like \n')
txt9 = 'Foggy Sunday morning\nCoffee and sweater needed.' 
print('The string is: ', txt9)
print('txt9.splitlines() will return: ',txt9.splitlines())
print(' ')

print('17. startswith(prefix,[start,[end]]) will return True if the string starts with the specifiec prefix and False if otherwise. Start and end show where to begin and end the search.')
txt10 = 'Attention! Report now.'
prefix = 'Attention'
print('The string is: ', txt10,'The prefix is: ', prefix)
print('startswith(prefix,0,20) will return: ',txt10.startswith(prefix,0,20))
print(' ')

print('18. strip([chars])will delete the empty space at the beginning and end of a string. Chars allows you to specify what characters to remove.')
txt11 = '         central park        ' 
print('The string is: ', txt11)
print('txt11.strip() will return:',txt11.strip())
print(' ')

print('19. upper() will turn all the characters in a string uppercase.')
txt12 = 'python is an object oriented programming language.'
print('The string is: ', txt12)
print('txt12.upper() will return: ', txt12.upper())
print(' ')

print('Part C')
print(' ')
print('For the final project, I will be teaming up with Ismael Baker. \nWe will work on the Python web Scraper/Postgresql project.\nI will work on the Python and Ismael will help integrate the database.')



