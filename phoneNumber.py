#########################################
# A Simple Phone Number Location Program#
#########################################
# Besides this file "phonenumber.py"
# Create a New File call it "testphone.py" for example and in that file setup a variable
# call it "number" and assign the variable a phone number with country code
# Import Phone Numbers Module

import phonenumbers as pn
from testphone import number

# Import Geocoder
from phonenumbers import geocoder

us_number = pn.parse(number, "US")
print("The number you provided is from:",
      geocoder.description_for_number(us_number, "EN"))
