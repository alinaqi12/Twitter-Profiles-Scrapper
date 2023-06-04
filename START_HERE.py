from save1 import enter_user
from sear import Usernames
import os
import sys
from clear_tables import clearTables

#--------------------------------------------------------------------------------#

user=sys.argv[1]
depth=int(sys.argv[2])

#if Extend==1:
#    clearTables(Extend)
#else:

clearTables()

########--------------------------------------------------------------------------------#

enter_user(user,depth)
print("Search is done")
usernames1,descriptions=Usernames()
usernames1=list(set(usernames1))
#descriptions=set(descriptions)
print(usernames1)

##print(usernames1)
print("Extracted intial information")
try:
    os.remove('../../new.txt')
except:
    try:
        os.remove('new.txt')
    except:
        a=1

##--------------------------------------------------------------------------------#

##print("code is here 9")
##Usernames1=Shortlist(Usernames1)

##Twitter mein usernames ka issue aarha hai.. tou osint k baad real id again scrap hogi. aur phir uska Full name search kia jae ga.
##uske baad jo usernames aaeinge unka comparison hoga.. tou jo users naye hounge unko feedback mein list mein store kr k again clustering hogi.



##Profile_pic(Usernames1)                                                                         
##Description_Analysis(legit)                                                                    
##Tweet_Analysis()                                                                
print("SUCCESS")                                                                                
                                                                                                
                                                                                                
                                                                                                
