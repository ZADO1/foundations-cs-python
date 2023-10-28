#Question 1
print("a. 10*(90+2)-5 = 915") # Solved by hand
print("b. 10*90+2-5 = 897")
print("c. 10*90+(2-5) = 897")
print("d. 10.0*(90+2)-5 = 915")
print("e. 120/(20+40)-(6-2)/4 = 1")
print("f. 5.0/2 = 2.5")
print("g. 5/2 = 2.5")
print("h. 5.0/2.0 = 2.5")
print("i. 5/2.0 = 2.5")
print("j. 678%3*(8-(9/4)) = 0")


#------------ Quest 2--------
id_add_0 = "0"
id_input = input("id :")
id_input = id_input.strip()
id_input = id_add_0 + id_input
name_input = str.upper(input("name :"))
name_input = name_input.strip()
date_of_birth = input("Date of Birth (DD/MM/YYY):")
date_of_birth = date_of_birth.replace("-", "/")
date_of_birth = date_of_birth.strip()
address = str.lower(input("Addres :"))
address = address.strip()
print(f"Your profile - id: [{id_input}], name: [{name_input}], DOB: [{date_of_birth}], Address:[{address}]")
# -----------------------------------------------------------------------
# Question 3
ask_number = input("choose a number :")
print(f"{ask_number} has {len(ask_number)} digitss")

#Question 4---------------------------------------------------------------

number_grade = eval(input("What is your number_grade :"))
letter_grade = ""
if number_grade >= 97:
    letter_grade = "A+"
elif 93 <= number_grade < 97:
    letter_grade = "A"
elif 90 <= number_grade < 93:
    letter_grade = "A-"
elif 87 <= number_grade < 90:
    letter_grade = "B+"
elif 83 <= number_grade < 87:
    letter_grade = "B"
elif  80 <= number_grade < 83:
    letter_grade = "B-"
elif 77 <= number_grade < 80:
    letter_grade = "C+"
elif 73 <= number_grade < 77:
    letter_grade = "C"
elif 70 <= number_grade < 73:
    letter_grade = "C-"
elif 67 <= number_grade < 70:
    letter_grade = "D+"
elif 63 <= number_grade < 67:
    letter_grade = "D"
elif 60 <= number_grade < 63:
    letter_grade = "D-"
else :
    letter_grade = "F"
print(f"{number_grade} is equivalent to a {letter_grade}.")
#-------