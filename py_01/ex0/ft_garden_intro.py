# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 20:18:29 by moerrais          #+#    #+#              #
#    Updated: 2025/12/31 15:55:39 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

Plant = "Rose"
Height = 25
Age = 30


def ft_garden_intro():
    print("=== Welcome to My Garden ===")
    print(f"Plant: {Plant}")
    print(f"Height: {Height}cm")
    print(f"Age: {Age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
