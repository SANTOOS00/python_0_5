# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:49 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:50 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_recursive(days):
    i = 0;
    if (days > 0):
        i += ft_recursive(days - 1)
        print ("Day " + str(i))
    return i + 1
def ft_count_harvest_recursive():
    days = int (input("Days until harvest: "))
    ft_recursive(days)