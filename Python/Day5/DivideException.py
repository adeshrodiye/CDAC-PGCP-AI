import sys
import traceback as tb

try:
    dividend = int(input('Enter a divisidend : '))
    divisor = int(input('Enter a divisor : '))
    result = dividend/divisor
    print(result)

except ValueError as er:
    print(er)
    cause, e_type, tb = sys.exc_info()
    print(f'{cause},{e_type}')

except ZeroDivisionError as er:
    print(er)
    tb.print_exc()

else:
    print("If try is successful")

finally:
    print("Executes always")