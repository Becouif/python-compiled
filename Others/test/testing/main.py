def do_stuff(num):
    try:
        if num:
            return int(num)+ int(num)
        else:
            return 'please enter number'
    except ValueError as err:
        return f"check your value {err}"
