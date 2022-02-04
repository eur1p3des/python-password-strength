import string

# Ask for the password:
password = input("Please enter your password: ")


# DESCRIPTION: Function that returns the number of points obtained depending the use of CAPITAL and lowercase letters.
def upper_lower_points(password):
    points = 0
    # DESCRIPTION: Function that returns the number of capital letters in the password.
    def count_uppercase(password):
        count = 0
        for i in password:
            if i.isupper():
                count += 1
        return count
    # DESCRIPTION: Function that returns the number of lowercase letters in the password.
    def count_lowercase(password):
        count = 0
        for i in password:
            if i.islower():
                count += 1
        return count

    lowercase = count_lowercase(password)
    uppercase = count_uppercase(password)


    if (lowercase >= 1 and uppercase >= 1):
        points += 1
        max = False
        if (lowercase >=2 or uppercase >= 2) or (lowercase >=2 and uppercase >= 2):
            points += 1
    else:
        points -= 1

    return points

# DESCRIPTION: Function that returns the number of points obtained based on the number of integers used.
def number_points(password):
    points = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n_digits = 0
    for i in password:
        if i in digits:
            n_digits += 1

    if n_digits >= 1:
        points += 1
        if n_digits >= 2:
            points += 1
    else:
        points -= 1

    return points

# DESCRIPTION: Function that returns the number of points obtained depending on the number of special
# characters used in the password.
def special(password):
    n_special = 0
    points = 0
    special = ""

    for i in password:
        if (i.isalpha() == False and i.isdigit() == False):
            n_special += 1
            special += i

    if n_special >= 1:
        points += 1
        if n_special >= 2:
            points += 1
    else:
        points -= 1
    return points



# DESCRIPTION: Function that calculates the strenghth points of the input password.
def calculate_strength(password):
    points = 0
    max = False
    # Password size
    p_size = int(len(password))

    ################################
    #       Points per length      #
    ################################
    if p_size < 8:
        points -= 1
        max = False
    if p_size >= 8 and p_size <= 16:
        points += 1
        max = False
    else:
        points += 2
        max = True

    ################################
    #   Check for capital letter   #
    ################################
    point = upper_lower_points(password)
    if point != 2:
        max = False
    else:
        max = True
    points += point

    ###############################
    #  Search for numbers         #
    ###############################
    point = number_points(password)
    if point != 2:
        max = False
    else:
        max = True
    points += point


    #################################
    # Search for special characters #
    #################################
    point = special(password)
    if point != 2:
        max = False
    else:
        max = False
    points += point

    #################################
    # Check for repeated characters #
    #################################
    points2 = points
    for i in range(p_size-1):
        if password[i] == password[i+1]:
            points2 -= 1
            max = False

    if points2 == points:
        points+=1
        max = True

    if max == True:
        points += 1

    # In case that the points in the end are lower than 0, e.g -1, points equals to 0
    if points <= 0:
        points = 0

    # Finally we return the score
    return points


################################
#           MAIN               #
################################
final_score = calculate_strength(password)

if final_score >= 0 and final_score < 5:
    print("Your password is not strong, please choose another one.")
if final_score >= 5 and final_score < 8:
    print("Your password is okay, but could be better, we recommend you to change it.")
if final_score >= 8:
    print("Your password is strong, nice job.")
