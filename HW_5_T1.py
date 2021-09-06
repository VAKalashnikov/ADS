import collections

# используем класс namedtuple

enterprise = collections.namedtuple('enterprise', ['designation', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'sum_ent'])
enterprises = []
n = int(input('Сколько будет предприятий'))
sum_all = 0

for i in range(n):
	designation = input('Введите название {}  - компании: '.format(i + 1))
	profit_1 = int(input('Прибыль за первый кваратал: '))
	profit_2 = int(input('Прибыль за второй кваратал: '))
	profit_3 = int(input('Прибыль за третий кваратал: '))
	profit_4 = int(input('Прибыль за четвертый кваратал: '))
	sum_ent = profit_1 + profit_2 + profit_3 + profit_4
	sum_all += sum_ent
	enterprises.append(enterprise(designation = designation, profit_1 = profit_1, profit_2 = profit_2, 
                               profit_3 = profit_3,  profit_4 = profit_4, sum_ent =  sum_ent))
	average = sum_all / n
	
# вывыедем предприятия с прибылью, превосходящей среднюю

for enterprise in enterprises:
	if enterprise.sum_ent > average:
		print(enterprise.designation, 'имеет прибыль выше среднего')

# аналогично вывыедем предприятия с прибылью, не превосходящей среднюю

for enterprise in enterprises:
	if enterprise.sum_ent <= average:
		print(enterprise.designation, 'имеет прибыль меньше среднего')		