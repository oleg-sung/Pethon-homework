import re

import csv

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def format_data(contact_list: list):
    new_contacts_list = []
    for items in contact_list[1:]:
        lastname = items[0].split(" ")[0]
        firstname = items[1].split(' ')[0]
        surname = items[2]
        organization = items[3]
        position = items[4]
        phone = items[5]
        email = items[6]
        if firstname == '':
            firstname = items[0].split(" ")[1]
        if surname == '':
            if len(items[0].split(' ')) > 2:
                surname = items[0].split(" ")[2]
            elif len(items[1].split(' ')) > 1:
                surname = items[1].split(' ')[1]
            else:
                pass
        pattern = r'(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?\(?(\w{3})?(\.)?\s?(\d{4})?\)?'
        repl = r'+7(\2)\3-\4-\5 \6\7\8'
        phone = re.sub(pattern, repl, phone)
        new_contacts_list.append([
            lastname,
            firstname,
            surname,
            organization,
            position,
            phone.strip(),
            email
        ])
    return new_contacts_list


def del_duplicates(contact_list: list):
    new_contacts_list = format_data(contact_list)
    for item_1 in new_contacts_list:
        for item_2 in new_contacts_list:
            if item_1[:2] == item_2[:2] and item_1 != item_2:
                if item_1[2] == '':
                    item_1[2] = item_2[2]
                if item_1[3] == '':
                    item_1[3] = item_2[3]
                if item_1[4] == '':
                    item_1[4] = item_2[4]
                if item_1[5] == '':
                    item_1[5] = item_2[5]
                if item_1[6] == '':
                    item_1[6] = item_2[6]
    clients_list = []
    for item_3 in new_contacts_list:
        if item_3 not in clients_list:
            clients_list.append(item_3)
    return clients_list


with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(del_duplicates(contacts_list))
