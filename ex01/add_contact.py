# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_contact.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lrocigno <lrocigno@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/29 14:39:47 by lrocigno          #+#    #+#              #
#    Updated: 2021/11/29 15:17:26 by lrocigno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import contact

def add_contact():
    info = dict.fromkeys(["first_name", "last_name", "nickname", 
                          "phone_number", "darkest_secret"])

    info["first_name"] = input("Contact first name: ")
    info["last_name"] = input("Contact last name: ")
    info["nickname"] = input("Contact nickname: ")
    info["phone_number"] = input("Contact phone number: ")
    info["darkest_secret"] = input("Contact darkest secret: ")

    contact = Contact(info)
    return contact
