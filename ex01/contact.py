# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    contact.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lrocigno <lrocigno@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/29 14:56:42 by lrocigno          #+#    #+#              #
#    Updated: 2021/11/29 15:16:23 by lrocigno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# To follow (mostly) the rules of "My Awsome PhoneBook", "contact" will be a
# class which will be composed of mainly strings.

from datetime import date

class Contact:
    def __init__(self, info: dict):
        self.created = date.today()
        self.first_name = info["fst_nm"]
        self.last_name = info["lst_nm"]
        self.nickname = info["nick"]
        self.phone_number = info["number"]
        self.darkest_secret = info["scrt"]
