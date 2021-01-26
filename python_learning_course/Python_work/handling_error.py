def read_int(min,max):
    try:
        num = int(input('Enter a number from {}..{}'.format(min,max)))
        assert num in range(min,max+1)
        print('The number is: {}'.format(num))
    except AssertionError:
        print('Error: the value is not within permitted range (-10..10)')
    except ValueError:
        print('Error: wrong input')
        

read_int(-10,10)