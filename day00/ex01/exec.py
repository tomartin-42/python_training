# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/14 17:26:44 by tomartin          #+#    #+#              #
#    Updated: 2022/04/15 12:18:26 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
    print("Error:")
    quit(1)
new_arg = str()
for word in reversed(sys.argv[1:]):
    new_arg = new_arg + (word.swapcase()[::-1]) + " "
print(new_arg[:-1])
