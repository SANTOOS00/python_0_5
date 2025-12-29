# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:47 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:48 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    Days = int(input("Days until harvest: "))
    i = 0
    while (i < Days):
        print("Days " + str(i + 1))
        i += 1
    print ("Harvest time!")