# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    megaphone.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lrocigno <lrocigno@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/29 13:36:13 by lrocigno          #+#    #+#              #
#    Updated: 2021/11/29 14:29:29 by lrocigno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = 1
argc = len(sys.argv)

if argc <= 1:
    sys.exit("* LOUD AND UNBEARABLE FEEDBACK NOISE *")

while i < argc:
    print(sys.argv[i].upper(), end='', sep='')
    i += 1

print('\n')
