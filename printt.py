customer_name = 'Chris'
inventory_count = 0
product = 'super_snowboard'

if inventory_count > 0 or (customer_name == 'Chris' and product =='super_snowboard'):
    print(True)


###With Nested Logic
inventory = 0
customer_name = 'Chris'
if inventory <= 0:
    if customer_name == 'Chris':
        print('You can have the display model, sir')
    else:
        print('Out of stock')
elif inventory <= 5:
        print('Low Stock')
else:
        print('In stock')


###Without Nested Logic
inventory = 0
customer_name = 'Chris'

if customer_name == 'Chris' and inventory <= 0:
    print('You can have the display model, sir')
    
elif inventory <= 0:
        print('Out of Stock')
elif inventory <= 5:
        print('Low Stock')
else:
        print('Out of stock')
inventory = 0
customer_name = 'Chris'
​
if customer_name == 'Chris' and inventory <= 0:
    print('You can have the display model, sir')
    
elif inventory <= 0:
        print('Out of Stock')
elif inventory <= 5:
        print('Low Stock')
else:
        print('Out of stock')


