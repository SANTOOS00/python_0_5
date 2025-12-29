# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:52 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:53 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    garden_name = str(input("Enter garden name: "))
    number_plants = int(input("Enter number of plants: "))
    print("Garden: " + garden_name)
    print("Plants: " + str(number_plants))
    print("Status: Growing well!")