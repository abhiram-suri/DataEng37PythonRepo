input_rating = input("What is the film rating\n")

if input_rating.upper() == "U":
    print("Anyone can watch this")
elif input_rating.upper() == "PG":
    print("Anyone can watch this with Parental Guidance")
elif input_rating.upper() == "12" or input_rating.upper() == "12A":
    print("Anyone over the age of 12 can watch this, if 12A then it may contain content unsuitable for some")
elif input_rating.upper() == "15":
    print("Anyone over the age of 15 can watch this")
elif input_rating.upper() == "18":
    print("You need to be at least 18 and have a ticket")
else: print("you have entered a wrong certificate rating")
print("This will always run")

