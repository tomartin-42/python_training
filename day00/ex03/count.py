# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/15 13:25:23 by tomartin          #+#    #+#              #
#    Updated: 2022/04/15 18:13:00 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(*args):

    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""

    if len(args) >= 2:
        print("ERROR", file=sys.stderr)
        return 
    if len(args) == 0:
        txt = input('What is the text to analyse?\n>> ')
    else:
        txt = args[0]
    counters = [0, 0, 0, 0]
    for char in txt:
        if char.isupper():
            counters[0] += 1
        elif char.islower():
            counters[1] += 1
        elif char in string.punctuation:
            counters[2] += 1
        elif char == ' ':
            counters[3] += 1
    print ("The text contain", len(txt), "characters:")
    print ("-", counters[0], "upper letters")
    print ("-", counters[1], "lower letters")
    print ("-", counters[2], "punctuation marks")
    print ("-", counters[3], "spaces")
