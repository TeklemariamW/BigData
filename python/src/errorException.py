'''
ImportError: Appears when an import statement has trouble loading a module
ModuleNotFoundError: Happens when import can’t locate a given module
NameError: Appears when a global or local name isn’t defined
AttributeError: Happens when an attribute reference or assignment fails
IndexError: Occurs when an indexing operation on a sequence uses an out-of-range index
KeyError: Occurs when a key is missing in a dictionary
ZeroDivisionError: Appears when the second operand in a division or modulo operation is 0
TypeError: Happens when an operation, function, or method operates on an object of inappropriate type
ValueError: Occurs when an operation, function, or method receives the right type of argument but the wrong value 

...more
'''

# handling exception with try/except
def handle_exception():
    #while True:
    try:
        x = int(input("Please enter a number: "))
        print("Good, you entered: ", x)
        
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# See the log of exception
def log_exception():
    try:
        f = open('myfile.txt')
        #f = open()
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: ", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

# exception outside try clause
def fun_exception():
    def this_fails():
        x = 1/0
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)

# Custom exceptions (raise)
class GradeValueError(Exception):
    pass
def calculate_average_grade(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise GradeValueError(
                "grade values must be between 0 and 100 inclusive"
            )
        total += grade
        count += 1
    return round(total / count, 2)

#Exception chaining
#FileNotFoundError
#RuntimeError
def chain_exception():
    try:
        print(10/2)
    except OSError:
        raise RuntimeError("unable to handle error") #from None
    else:
        print("if this print, there is no error in my code")
'''
Clean up action with finally
'''
def clean_up_action(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

def multiple_unrelated_exc():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

#Add more information when an exception occurs
def add_note_toException():
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note("addiiiiiiiiiiiiiiiiiiiii")
        raise

if __name__ == "__main__":
    pass
    #handle_exception()
    #log_exception()
    #fun_exception()
    #calculate_average_grade([98, 95, 110])
    #chain_exception()
    #clean_up_action(2, 1) #(2 ,0) ('2', '1')
    #multiple_unrelated_exc()
    #add_note_toException()

for i in range(20):
    print(f"This is a cool script {i}")