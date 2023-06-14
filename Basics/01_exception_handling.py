import logging
# https://www.tutorialsteacher.com/python/error-types-in-python
values = [1,2,3,4,0,5,6,7,8,"Hello"]
for value in values:
    try:
        print(10/value)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

for value in values:
    try:
        print(10/value)
        # raise
        # raise AttributeError
    except (ZeroDivisionError,ValueError) as e:
        pass
    except AttributeError as e:
        print("Testing Error handling!")
    except Exception as e:
        logging.exception(e)
    finally:
        print("No exception")  
else:
    print("No exception!!")

# while (True):
#     try:
#         x = int(input("Enter any number"))
#         break
#     except (ZeroDivisionError ,ValueError) as e:
#         print("Unsupported data type!")



