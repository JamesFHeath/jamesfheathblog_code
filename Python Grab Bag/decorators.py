# Simple Decorator
def decorator(f):
    print('Decorated!')
    return f

@decorator
def to_decorate():
    print('To Decorate')
    return 1

to_decorate()

to_decorate = decorator(to_decorate)

# Decorator with Wrapper
def decorator(f):
    def wrapper():
        print('Decorated!')
        f()
    return wrapper

@decorator
def to_decorate():
    print('To Decorate')
    return 1

to_decorate()

to_decorate = decorator(to_decorate)

# Decorator that can handle function parameters
def decorator(f):
    def wrapper(*args, **kwargs):
        print('Decorated!')
        f(*args, **kwargs)
    return wrapper

@decorator_with_wrapper
def to_decorate(x, y, **kwargs):
    print('To Decorate')
    print(x)
    print(y)
    print(kwargs)
    return 1

to_decorate('searingfrost', 'another parameter', **{'key': 'value'})

to_decorate = decorator(to_decorate)

# Decorator factory to handle decorator parameters
def decorator_factory(*factory_args, **factory_kwargs):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print(f'Args Passed to factory: {factory_args}')
            print(f'KeywordArgs passed to factory: {factory_kwargs}')
            print('Decorated!')
            f(*args, **kwargs)
        return wrapper
    return decorator_with_wrapper

@decorator_factory('someargument', a=5, b=10)
def to_decorate(x, y, **kwargs):
    print('To Decorate')
    print(x)
    print(y)
    print(kwargs)

to_decorate('searingfrost', 'another parameter', **{'key': 'value'})

to_decorate = decoratory_factory('someargument', a=5, b=10)(to_decorate)