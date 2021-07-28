import phonenumbers
from phonenumbers import geocoder
phone = '+5516988708462'

phone_number = phonenumbers.parse(phone)
print(geocoder.description_for_number(phone_number,'pt'))


