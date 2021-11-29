# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lrocigno <lrocigno@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/29 14:28:10 by lrocigno          #+#    #+#              #
#    Updated: 2021/11/29 15:16:57 by lrocigno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import add_contact
import sys

contacts = []

while True:
    command = input()

    if command == "EXIT":
        sys.exit()
    elif command == "ADD":
        if len(contacts) < 8:
            contacts.append(add_contact())
