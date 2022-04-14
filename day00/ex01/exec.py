# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/14 17:26:44 by tomartin          #+#    #+#              #
#    Updated: 2022/04/14 20:15:57 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
    print("Error:")
    quit(1)
for word in reversed(sys.argv[1::-1]):
    new_argv = word.swapcase()
    print(new_argv)
