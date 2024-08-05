"""_summary_"""
import time


start_time = time.time()

def waiter(customer_request, delai):
    """ test """
    print(f"start request {customer_request}")
    time.sleep(delai)
    print(f"finish request {customer_request}")

def main():
    """ main programm """
    waiter("coffe", 3)
    waiter("the",2)
    waiter("water",1)


if __name__ == '__main__':
    main()
    print(f"finish requests {round(time.time()-start_time,1)}")
