import datetime

date = datetime.date(2017, 7, 31)
increment = datetime.timedelta(days=1)
days_in_quarters = {'Q1': 90, 'Q2': 91, 'Q3': 92, 'Q4': 92}
deliveries = {'Q3-17': 222, 'Q4-17': 1542, 'Q1-18': 8182, 'Q2-18': 18449}

quarter = 'Q3'
delivery_quarter = 'Q3-17'
start_deliveries = 30
count = 1
days_in = 0

deliveries_per_day = int(deliveries['Q3-17'] / days_in_quarters['Q3'])
deliveries_at_end =  deliveries['Q3-17'] % days_in_quarters['Q3']

#I might have to queue up the reservation numbers to add in the customer id

if delivery_quarter == 'Q3-17':
    days_in = 31
    deliveries_per_day = int(deliveries[delivery_quarter] / (days_in_quarters[quarter] - days_in))
    deliveries_at_end = ((deliveries[delivery_quarter] - start_deliveries) % (days_in_quarters[quarter] - days_in))

    for delivery in range(start_deliveries):
        #this would be a create delivery based on reservation number
        print("Delivery number: ", count, " - " , date)
        count +=1
    date = date + increment

    for days in range(days_in_quarters[quarter] - days_in):
        if (deliveries[delivery_quarter] - (deliveries_at_end + deliveries_per_day - 1) == count):
            deliveries_per_day = deliveries_at_end + deliveries_per_day
            print(deliveries_per_day, "\n\n\n")

        for delivery in range(deliveries_per_day):
            print("Delivery number: ", count, " - " , date)
            count+=1

        date = date + increment

    file = open('deliveries.txt','w')
    file.write(str(count))

else:
    for days in range(days_in_quarters[quarter] - days_in):
        if (deliveries[delivery_quarter] - (deliveries_at_end + deliveries_per_day - 1) == count):
            deliveries_per_day = deliveries_at_end + deliveries_per_day
            print(deliveries_per_day, "\n\n\n")

        for delivery in range(deliveries_per_day):
            print("Delivery number: ", count, " - " , date)
            count+=1

        date = date + increment
        days_in +=1


print(date)
print(deliveries_at_end)
