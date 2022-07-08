x = object()  # variable 'x' NameErrors

r = x

del x

try:
    # noinspection PyUnboundLocalVariable
    x
except NameError as e:
    the_name_in_the_message = str(e).split("'")[1]

x = r
