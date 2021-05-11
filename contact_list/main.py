class Contact:
    def __init__(self, name, num):
        self.num = num
        self.name = name

    def __str__(self):
        return self.name + ': ' + self.num


class ContactList:

    @property
    def data(self):
        tmp_data = list()
        with open('contacts.txt', 'r') as f:
            line = f.readline().rstrip()
            while line != '':
                name_num = line.split(',')
                tmp_data.append(Contact(name_num[0], name_num[1]))
                line = f.readline().rstrip()
        return tmp_data

    def __init__(self):

        while True:
            option = input("""
            1- Print contact list.
            2- Search a name.
            3- Add new contact.
            4- Remove contact.
            5- Update contact.
            6- Search a number.
            To exit enter 0.
            """)
            option = int(option)
            if option == 0:
                break
            if option == 1:
                self.print_list()
            if option == 3:
                if self.add_contact() == True:
                    print('Adding a new contact is successful')

    def print_list(self):
        print('Name: Number')
        for contact in self.data:
            print(contact)

    def add_contact(self):
        user_input = input(
            'Please enter "name,number" with the given format: ')
        user_input = user_input.split(',')
        with open('contacts.txt', 'a') as f:
            f.write('\n')
            if f.write(user_input[0] + ',' + user_input[1]):
                return True
            else:
                return False


c_list = ContactList()
