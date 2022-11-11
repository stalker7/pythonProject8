import re
import csv

DATA_FILE = "phonebook_raw.csv"
PATTERN = "(\+7|8)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w.)*\s*(\d{4})*(\))*"


def input_data():
    with open(DATA_FILE, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def parse_contact_list(contacts_list):
    new_contacts_list = list()
    for contact in contacts_list:
        new_contact = list()
        full_name_str = ",".join(contact[:3])
        result = re.findall(r'(\w+)', full_name_str)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone_pattern = re.compile(PATTERN)
        changed_phone = phone_pattern.sub(r"+7(\3)\6-\8-\10 \12\13", contact[5])
        new_contact.append(changed_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    return new_contacts_list


def delete_duplicates_contact(new_contacts_list):
    contact_book = dict()
    for contact in new_contacts_list:
        if contact[0] in contact_book:
            contact_value = contact_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            contact_book[contact[0]] = contact
    return list(contact_book.values())


def write_data(new_contacts_list):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(new_contacts_list)

if __name__=='__main__':
    
    new_contacts_list = input_data()
    new_parsed_list = parse_contact_list(new_contacts_list)
    contact_book_values = delete_duplicates_contact(new_parsed_list)
    write_data(contact_book_values)
























