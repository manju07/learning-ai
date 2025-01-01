import sys

try:
    raise ValueError('ValueError')
    # if 10 / 0 == 0:
    #     print(1)
    # elif 10 / 1 == 1:
    #     print(2)
    # else:
    #     print(3)
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as e:
    print("Unexpected error:", e)
else:
    print("All good")
finally:
    print("All done")
