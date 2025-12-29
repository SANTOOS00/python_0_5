# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:55 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:56 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if "packets" == unit:
        print ("Tomato seeds: " + str(quantity) +" " +unit + " available")
    elif "grams" == unit:
        print ("Tomato seeds: " + str(quantity) +" " +unit + " total")
    elif "area" == unit:
        print ("Tomato seeds: covers " + str(quantity) + " square meters")
    else:
        print("Unknown unit type")