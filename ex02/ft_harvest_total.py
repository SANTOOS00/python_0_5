# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:37 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:38 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    i = 0
    res = 0
    while i < 3:
        res += int(input("Day "+ str(i + 1) +" harvest: "))
        i += 1
    print ("Total harvest: ",res)
ft_harvest_total()