# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: santoos <santoos@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 22:34:02 by moerrais          #+#    #+#              #
#    Updated: 2026/01/04 06:19:22 by santoos          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    print ("=== Garden Plant Registry ===")
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    data1 = Plant("Rose", 25, 30)
    data2 = Plant("Sunflower", 80, 45)
    data3 = Plant("Cactus", 15, 120)
    
    
    data1.print_data()
    data2.print_data()
    data3.print_data()
