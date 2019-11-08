class ContactList(list):
    all_contacts = ['Meder', 'Dastan', 'Nurbek', 'Akram', 'Maksat', 'Nurbek']

    def search_by_name(self, name):
        total = []

        for i in range(self.all_contacts.__len__()):
            if name in self.all_contacts[i]:
                total.append(name + f' {i} | ')

        return total

name = input('Введите имя: ')

contact = ContactList()
total_contact = contact.search_by_name(name)

print(''.join(total_contact))
      

    