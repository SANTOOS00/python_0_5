# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: santoos <santoos@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 20:18:19 by moerrais          #+#    #+#              #
#    Updated: 2026/01/04 08:04:37 by santoos          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# class Plant():
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age
#     def print_input(self):
#         return f"{self.name} ({self.height}cm, {self.age} days)"
#     def print_data(self):
        
        
    
    
Plants_data = [
    ["Rose", 25, 30],
    ["Oak" , 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120],
]
size = len(Plants_data)
i = 0
while (i < size):
    print(Plants_data [i])
    i += 1
