#question 1
###########
def Question1(s, i):
  print(s[::-1] * i)


Question1("daiz", 4)


#################################################################
#question2
###########
def question2(s):
  uppercase_chars = ""
  lowercase_chars = ""

  for char in s:
    if char.isupper():
      uppercase_chars += char
    else:
      lowercase_chars += char

  rearranged_string = uppercase_chars + lowercase_chars
  print(rearranged_string)


question2("ZiaD")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


###############################################################
#question 3
###########
def question3(s1, s2):
  sorted(s1)
  sorted(s2)
  return sorted(s1) == sorted(s2)


result = question3("ziad", "daxxxiz")
print(result)

############################################################
# question4
#############
print("--------------")


def min(l):
  highest_number = l[0]
  for number in l:
    if number > highest_number:
      highest_number = number
  print("the highest number is :  ", highest_number, "at index:",
        l.index(highest_number))


min([1, 2, 3, 4, 5, 5, 6, 677, 7])

# question4 part 2


def min(l):
  lowestNumber = l[0]
  for number in l:
    if number < lowestNumber:
      lowestNumber = number
  print("the highest number is :  ", lowestNumber, "at index:",
        l.index(lowestNumber))


min([1, 2, 3, 4, 5, 5, 6, 677, 7])
#####################################################
print("----------------------------------")


#question 5
############
def Question5(n):
  if n == 0:
    return 0
  return n % 10 + Question5(n // 10)


print(Question5(137))

##############################################################


#question 6
############
def question6(s):
  if len(s) <= 1:
    return s
  if s[0] == s[1]:
    return question6(s[1:])

  else:
    return s[0] + question6(s[1:])


print(question6("ziaaaddp"))
###########################################################
