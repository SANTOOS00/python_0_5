# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:43 by moerrais          #+#    #+#              #
#    Updated: 2025/12/29 08:25:44 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days <= 2:
        print ("Plants are fine")
    else:
        print ("Water the plants!")