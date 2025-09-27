#Q18
person = {
    'name': 'Riya',
    'age': 22,
    'city': 'Delhi',
    'mobile': '9876543210',
    'pin_code': '110001'
}

city = input("Enter new city: ")
mobile = input("Enter new mobile number: ")

person['city'] = city
person['mobile'] = mobile

print("\nUpdated details:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
