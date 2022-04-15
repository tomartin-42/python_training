# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/15 12:21:23 by tomartin          #+#    #+#              #
#    Updated: 2022/04/15 13:22:30 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.tracebacklimit = 0
if len(sys.argv) == 1:
    quit()
elif sys.argv[1] == '0':
    print("I’m Zero.")
    quit()
assert len(sys.argv) <= 2, "more than one argument is provided"
assert sys.argv[1].isnumeric(), "argument is not integer"
print("I’m", ['Even', 'Odd'][int(sys.argv[1]) % 2])
