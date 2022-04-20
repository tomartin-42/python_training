# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tomartin <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/20 11:13:43 by tomartin          #+#    #+#              #
#    Updated: 2022/04/20 11:28:40 by tomartin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
selection_menu = (1, 2, 3, 4, 5)

def print_menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    return input('>> ')

s = print_menu()
while(not(s in selection_menu)):
    s = print_menu()
    print(s)
