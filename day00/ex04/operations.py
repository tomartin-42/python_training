# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/15 18:16:18 by tomartin          #+#    #+#              #
#    Updated: 2022/04/18 12:17:16 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class too_arguments(Exception):
    pass

def my_msg():
    """Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3"""

try:
    assert len(sys.argv) <= 3, 'InputError: too many arguments'
except AssertionError as msg:
    print(msg)
    quit(1)

try:
    assert len(sys.argv) > 2
except AssertionError:
    print(my_msg.__doc__)
    quit(1)

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError as err:
    print('ImputError:', end=' ')
    print(my_msg.__doc__)
    quit(1)

try:
    q = a / b
    r = a % b
except ZeroDivisionError:
    q = 'ERROR (div by zero)'
    r = 'ERROR (modulo by zero)'

print('Sum:         ', a + b)
print('Difference:  ', a - b)
print('Product:     ', a * b)
print('Quotient:    ', q)
print('Remainder:   ', r)

