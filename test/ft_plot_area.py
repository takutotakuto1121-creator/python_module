# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsugimot <tsugimot@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 16:52:40 by tsugimot          #+#    #+#              #
#    Updated: 2026/05/09 18:17:50 by tsugimot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = input("Enter length: ")
	width = input("Enter width: ")
	print("Plot area:", int(length)*int(width))

ft_plot_area()