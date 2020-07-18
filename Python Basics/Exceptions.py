1/0

try: 
    1 / 0 
except:
    print('Exception')    

try:
    'hello' + 1
except TypeError as e:
    print(f'TypeError: {e}')

def my_add_function(x, y):
    if type(x) != type(y):
        raise Exception('Both arguments must be of the same type')
    return f'{x} + {y} = {x + y}'        


z = my_add_function(1, 1)

a = my_add_function(1, 'chicken')