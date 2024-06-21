
def my_function(my_list):
    try:
       my_list.reverse()
       print(my_list)
       
    except Exception as ex:
       print(ex)

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    my_function(my_list)