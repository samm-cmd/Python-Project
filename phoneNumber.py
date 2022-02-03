#########################################
# A Simple Phone Number Location Program #
#########################################
# Besides this file "phonenumber.py"
# Create a New File call it "testphone.py" for example and in that file setup a variable
# call it "number" and assign the variable a phone number with country code
# Import Phone Numbers Module
import phonenumbers as pn
# Import the number from the testphone file
from testphone import number
# Import Geocoder
from phonenumbers import geocoder
# Import Service Provider "Carrier"
from phonenumbers import carrier

us_number = pn.parse(number, "CH")  # -> "CH": Stands for Country History
print("The number you provided is from:",
      geocoder.description_for_number(us_number, "en"))  # -> "EN": Means English

service_number = pn.parse(number, "RO")
print("The Carrier is:", carrier.name_for_number(service_number, "en"))
