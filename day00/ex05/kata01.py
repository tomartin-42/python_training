# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/20 08:30:57 by tomartin          #+#    #+#              #
#    Updated: 2022/04/20 08:39:07 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

lenguages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }

for leng in lenguages:
    print(leng, 'was create by', lenguages.get(leng))
