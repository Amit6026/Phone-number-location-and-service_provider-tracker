import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number = "paste your phone number with country code"

country_number= phonenumbers.parse(number,"Ch")
print(geocoder.description_for_number(country_number,"en"))

service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

