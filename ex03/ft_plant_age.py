# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:40 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:41 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    days = int(input("Enter plant age in dyas: "))
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print ("Plant needs more time to grow.")
ft_plant_age()