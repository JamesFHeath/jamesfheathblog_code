from tenacity import *

# Basic Retrying
@retry
def exception_function():
    print('exception time!')
    raise Exception

@retry(stop=stop_after_attempt(5))
def max_attempts():
    print('Runs 5 Times')
    raise Exception

@retry(wait=wait_fixed(2))
def fixed_wait_attempts():
    print('Waits 2 Seconds Between Retries')
    raise Exception

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def max_and_fixed_wait_attempts():
    print('Runs 5 Times AND Waits 2 Seconds Between Retries')
    raise Exception

# Exponential Backoff
@retry(wait=wait_exponential(multiplier=1, max=10))
def exponential_backoff_attempts():
    print('Runs at second intervals of 0, 2, 4, 8, 10, 10, 10...')
    raise Exception

# Custom Retrying Logic
@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type((IOError, ValueError)))
def different_exceptions_possible(x):
    if x == 1:
        print('IO Error because x is 1')
        raise IOError
    elif x == 2:
        print('Connection Error because x is 2')
        raise ConnectionError
    elif x == 3:
        print('Type Error because x is 3')
        raise TypeError
    else:
        return 'success'

print(different_exceptions_possible(1))
print(different_exceptions_possible(2))
print(different_exceptions_possible(3))

def is_invalid_code(code):
    success_range = range(200, 300)
    return code not in success_range

@retry(retry=retry_if_result(is_invalid_code))
def my_success_http_request():
    print('success')
    return 200

my_success_http_request()

@retry(retry=retry_if_result(is_invalid_code))
def my_failure_http_request():
    print('failure')
    return 400

my_failure_http_request()
