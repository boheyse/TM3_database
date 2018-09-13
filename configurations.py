from peewee import *
from general import general_info
from random import randint

db = SqliteDatabase('fakerM3.db')

colors = ['Solid Black', 'Red Multi-Coat', 'Midnight Silver Metallic', 'Deep Blue Metallic',
         'Pearl White Multi-Coat', 'Silver Metallic', 'Obsidion Black']
wheels = ['18" Aero Wheels', '19" Sport Wheels']
batteries = ['Long Range Battery', 'Standard Battery']
drivetrains = ['Rear Wheel Drive', 'Dual Motor', 'Performance']
interiors = ['Black', 'White']
choice = ['Yes', 'No']

class configuration(Model):
    customer_id = ForeignKeyField(general_info, to_field="customer_id")
    config_id = IntegerField(primary_key=True)
    color = CharField()
    wheel = CharField()
    battery = CharField()
    drivetrain = CharField()
    premium = CharField()
    interior = CharField()
    enhanced_AP = CharField()
    fsd = CharField()

    class Meta:
        database = db


def add_reservation():
    color_index = randint(0,6)
    wheel_index = randint(0,1)
    battery_index = randint(0,1)
    drivetrain_index = randint(0,2)
    interior_index = randint(0,1)
    premium_index = randint(0,1)
    eap_index = randint(0,1)
    fsd_index = randint(0,1)

    configuration.create(color = colors[color_index], wheel = wheels[wheel_index],
                         battery = batteries[battery_index], drivetrain = drivetrains[drivetrain_index],
                         premium = choice[premium_index], interior = interiors[interior_index],
                         enhanced_AP = choice[eap_index], fsd = choice[fsd_index])

if __name__ == '__main__':
    db.connect()
    db.drop_tables([configuration])
    db.create_tables([configuration])
    for reservation in range(10):
        add_reservation()
