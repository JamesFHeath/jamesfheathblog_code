Links:
https://blog.jamesfheath.com/2020/07/python-library-tenacity.html
Tenacity on PyPi: https://pypi.org/project/tenacity/
Tenacity Source on GitHub: https://github.com/jd/tenacity

# Introduction
Hi Everyone, SearingFrost here in the Python Library.
Today we'll be checking out the Tenacity project. 
Tenacity is an open source 3rd party library, and it's used for retrying code after exceptions. 
Let's dive in!

# Retrying After Exceptions
To get tenacity working, first just pip install tenacity from your terminal or command prompts,
and then import tenacity with  "from tenacity import asterix" 
Tenacity uses function decorators to tell a function to retry.
By default, @retry will work after any exception. 
@retry with nothing else will retry infinitely 

from tenacity import *

@retry
def exception_function():
    print('exception time!')
    raise Exception

Luckily, several time and execution count based parameters can be added to the decorator. 
Here we can specify tenacity to stop after 5 attempts before finally raising the exception. 

@retry(stop=stop_after_attempt(5))
def max_attempts():
    print('Runs 5 Times')
    raise Exception

This function will retry indefinitely, with 2 seconds elapsing between each retry. 

@retry(wait=wait_fixed(2))
def fixed_wait_attempts():
    print('Waits 2 Seconds Between Retries')
    raise Exception

We can also combine these parameters to generate more complex behaviors. 
This function will run 5 times, and wait 2 seconds between retries before finally raising the exception. 

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def max_and_fixed_wait_attempts():
    print('Runs 5 Times AND Waits 2 Seconds Between Retries')
    raise Exception

Expontential backoff is another piece of functionality tenacity implements
Expontential backoff means increasing the time between retries based on a multiplier, 2 by default. 
Exponential backoff is important for network calls where giving a server more time to recover may be important. 
This function retries immediately, then at 2, 4, 8 and 10 seconds before finally maxing out at retrying every 10 seconds. 
@retry(wait=wait_exponential(multiplier=1, max=10))
def exponential_backoff_attempts():
    print('Runs at second intervals of 0, 2, 4, 8, 10, 10, 10...')
    raise Exception

### Custom Retrying Logic
Retrying a function based on the type of exception raised can also be very useful. 
In this example, the function only retries on IOError and ConnectionError exceptions, but allows TypeError to be raised immediately. 
This would be useful for retrying failed input/output calls and network calls. 
We pass the IOError and ValueError as a tuple into the retry_if_exception_type function.
'IO Error because x is 1' printed 3 times before exception raised
'Connection Error because x is 2' printed 3 times before exception raised
Type Error is raised immediately because tenacity's retry ignores this error

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

different_exceptions_possible(1)
different_exceptions_possible(2)
different_exceptions_possible(3)

Sometimes a function should be retried even if it completes without an exception. 
Tenacity allows custom retrying functions to be used.
If the custom function returns True, the original function is retried. 
Let's create a function that returns true if an HTTP code is invalid
Then we can define two other functions, one for a successful 200 response and one for a failure 400 response
A 200 response from our success http request will not be retried.
But a 400 code from our failure http request WILL be retried indefinitely

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

# Thanks for Watching
Thanks for joining me in the Python library.
Tenacity or other retrying code is vital for Python programming today, because so many services are networked and have the potential to fail. 
It's easy to go down the happy path and assume your code will work, but planning for and mitigating failure will make you a better engineer. 
Links to the code and my blog post on tenacity are in the description. 
I'll see everyone next time. 