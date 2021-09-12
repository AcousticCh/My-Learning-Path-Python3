#if someone lives tell 90
#take days weeks and months left and multiply them accordingly
#subtracting subject age from 90 then multiply
#for leapyear bs figure out percentage of leap yars then 
#how many days each year is missing and multiply perentage by daysd missing per year
#then subtract days from well days

userAge = ""
days = 365
weeks = 52
months = 12 
yearsToLive = 90

userAge = input("how old are you?\n")
userAge = int(userAge)
yearsToLive -= userAge
days *= yearsToLive
weeks *= yearsToLive
months *= yearsToLive
print(f"You have {days} days, {weeks} weeks and {months} months if you live to 90.")
