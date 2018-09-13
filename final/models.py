from peewee import *

db = SqliteDatabase('fakerM3.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class id(BaseModel):
    customer_id = IntegerField(primary_key=True, unique=True)

class customer_info(BaseModel):
    customer_id = ForeignKeyField(id, backref="customer")
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    email = CharField()
    primary_phone = CharField()
    secondary_phone = CharField()
    #employee = BooleanField()
    #tesla_owner = BooleanField()

class configuration(BaseModel):
    customer_id = ForeignKeyField(customer_info, backref="config")
    config_id = IntegerField(primary_key=True)
    color = CharField()
    wheel = CharField()
    battery = CharField()
    drivetrain = CharField()
    premium = CharField()
    interior = CharField()
    enhanced_AP = CharField()
    fsd = CharField()
    vin = CharField(null=True)

class payment(BaseModel):
    customer_id = ForeignKeyField(customer_info, backref="pay")
    payment_id = IntegerField(primary_key=True)
    deposit = BooleanField(default=True)
    config_deposit = BooleanField(default=False)
    trade_in = BooleanField(default=False)
    loan = CharField()
    cash = CharField()
    bank = CharField()
    routing_num = CharField()

class delivery(BaseModel):
    customer_id = ForeignKeyField(customer_info, backref="delivery")
    scheduled_delivery = CharField()
    delivery_date = CharField()
    delay = BooleanField(default=False)
    service_needed = BooleanField(default=False)

    def add_delivery():
        
        delivery.create(customer_id = customer_info.customer_id, )
        num +=1
