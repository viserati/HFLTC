
import random
customers = ['Luke', 'Leia', 'Darth', 'C3PO', 'R2D2', 'Lando', 'Han', 'Chewy', 'Kewei', 'C0D1' ]
winner = random.choice(customers)
flavor = 'vanilla'
print('Congratulations, ' + winner + ' you have won an ice cream sundae from the Creamery!!!')
prompt = 'Would you like a chilled cherry  on top (yes/no)? '
wants_cherry = input(prompt)
order = flavor + ' sundae '

if(wants_cherry == 'yes'):
    order = order + ' with a cherry on top '

print('One ' + order + 'for ' + winner + ' coming up!!!')
