import pandas as pd
from peewee import *
from faker import Faker
from random import randint
from models import BaseModel, id, customer_info, configuration, payment

#These initialize the data base and create an object to be able to create fake data
db = SqliteDatabase('fakerM3.db')
p_i = Faker()

# These are lists to hold the current possible configurations for a model 3
colors = ['Solid Black', 'Red Multi-Coat', 'Midnight Silver Metallic', 'Deep Blue Metallic',
         'Pearl White Multi-Coat', 'Silver Metallic', 'Obsidion Black']
wheels = ['18" Aero Wheels', '19" Sport Wheels']
batteries = ['Long Range Battery', 'Standard Battery']
drivetrains = ['Rear Wheel Drive', 'Dual Motor', 'Performance']
interiors = ['Black', 'White']
choice = ['Yes', 'No']
vehicle_num = [1]

# Creates a new customer that is unique to the customer outside of their email
# and returns the customer object which holds the customer_id for all other tables to user

def new_id():
    customer = id.create(customer_id=randint(1,99999999))

    return customer

# Creates a customers personal information
def add_info(customer):
    with db.atomic():
        fn = p_i.first_name()
        ln = p_i.last_name()
        emails = ['@yahoo.com', '@gmail.com', '@aol.com', '@msn.com', '@outlook.com',
                  '@mail.com', '@'+ln+'.com']
        email_index = randint(0,6)
        customer_info.create(customer_id=customer, first_name = fn, last_name = ln, address=p_i.address(),
                             email= fn + ln + emails[email_index], primary_phone=p_i.phone_number(),
                             secondary_phone=p_i.phone_number())

# Creates a customers configuration, all fields are able to be null until the customer is able
# to configure their car, this function returns the drivetrain to be used in creating the vin
def add_configuration(customer):
    with db.atomic():
        color_index = randint(0,6)
        wheel_index = randint(0,1)
        battery_index = randint(0,1)
        drivetrain_index = randint(0,2)
        interior_index = randint(0,1)
        premium_index = randint(0,1)
        eap_index = randint(0,1)
        fsd_index = randint(0,1)

        configuration.create(customer_id = customer, color = colors[color_index], wheel = wheels[wheel_index],
                             battery = batteries[battery_index], drivetrain = drivetrains[drivetrain_index],
                             premium = choice[premium_index], interior = interiors[interior_index],
                             enhanced_AP = choice[eap_index], fsd = choice[fsd_index])

    if drivetrain_index == 1 or drivetrain_index == 2:
        return 'B'
    else:
        return 'A'

# This will make a new vin
def new_vin(v):
    v[0] +=1
    vin = v[0]
    while len(vin) is not 6:
    
    return vin

#This will add a new vin to a customers configuration
def create_vin(v, drivetrain):
    #B = dual_motor, A = rwd
    v_id = '5YJ3E1E' + drivetrain + 'XJF' + v
    configuration.create(vin = v_id)

# Adds a customers payment info to the payment table using their customer_id as reference
def add_payment(customer):
    payment_index = randint(0,1)
    if payment_index == 0:
        cash_payment = 1
    else:
        cash_payment = 0
    bank_index = randint(0, 27606)
    banks = pd.read_csv('INSTITUTIONS2.csv')
    banks = banks.iloc[:, 4]
    b_i = banks[bank_index]
    route = str(randint(11111110, 326000000))
    if len(route) == 8:
        route = '0' + route
    payment.create(customer_id = customer, loan = choice[payment_index], cash = choice[cash_payment], bank = b_i,
                   routing_num = route)


#confiugres everything
if __name__ == '__main__':
    db.connect()
    db.drop_tables([id, customer_info, configuration, payment])
    db.create_tables([id, customer_info, configuration, payment])
    with db.atomic():
        for config in range(10):
            customer = new_id()
            add_info(customer)
            add_configuration(customer)
            add_payment(customer)

#This is only used when we want to add in a new vin...
# for v in range(10):
#     f = open('testfile.txt','w')
#     add = add_vin(vin_number)
#     create_vin(add)
#     print(add)
#     f.write(str(add))
#     f.write(', ')
