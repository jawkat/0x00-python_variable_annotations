"""_summary_"""
import time
import asyncio

start_time = time.time()

async def waiter(customer_request, delai):
    """ test """
    print(f"start request {customer_request}")
    await asyncio.sleep(delai)
    print(f"finish request {customer_request}")

async def main():
    """ main programm """
    customer_req =[
        {
            "req" : "coffe",
            "delai" : 3
        },
        {
            "req" : "tea",
            "delai":2
        },
        {
            "req":"water",
            "delai":1
        }
    ]

    tasks = []
    for cr in customer_req:
        tasks.append(asyncio.create_task(waiter(cr["req"],cr["delai"])))


    await asyncio.gather(* tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print(f"finish requests {round(time.time()-start_time,1)}")
