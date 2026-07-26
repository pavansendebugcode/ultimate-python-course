# Match case statement 
# match case lets Python compare a value against multiple patterns and run the first matching block, like a switch statement.




a = int(input("Enter your age ; " ))

match a:

    case 18:
        print("wow! aap bade ho gaye")

    case 25:
        print("you are elisable for loksabha member")

    case 30:
        print("you are elizable for rajsabha member")

    case 35:
        print("you are eligable for become a prident ")

    case _:
        print("you are good person thats a very good age ", a)


