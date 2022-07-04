# 5. Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

my_string = '/bin:/usr/bin:/usr/local/bin'
my_list = list(my_string.split(':'))
print(my_list)
