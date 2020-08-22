from random import random
import threading
import time

result = None


def background_calculation():
    print('waiting begins')
    # here goes some long calculation
    time.sleep(random() * 5)
    print('wait is over')

    # when calculation is done, result is stored in a global variable
    global result
    result = 42


def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # TODO: wait here for the result to be available before continuing

    # this method is not a good way to wait as python will constantly check
    # through this while loop until result is not None. it's burning a lot
    # of CPU cycles. This type of wait is called a busy wait and the CPU that
    # is stuck doing a lot of work over nothing is said to be spinning. Never
    # do this.
    while result is None:
        pass

    print(f'The result is: {result}')


if __name__ == '__main__':
    main()
