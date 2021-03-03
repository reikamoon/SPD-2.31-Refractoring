# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def older_than_18_year_old(age):
    if age > LEGAL_DRINKING_AGE:
        return True
        print("Allowed to enter.")
    else: 
        return False
        print("Enterance of minors is denited.")
    
    
person = Person(17.9)

        
