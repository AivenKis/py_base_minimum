# Программа расчета заработной платы, которая вычисляет заработную плату до удержаний, налог и сумму на руки
#                                   включая надбавку за сверхурочную работу.


BASE_HOURS = 40             # Базовые часы в неделю.
ON_MULTIPLAYER = 1.5        # Мультипликатор сверхурочного времени.
TAX_RATE = 0.13             # Налоговая ставка 13%

# Получить отработанные часы и почасовую ставку оплаты труда.

hours_worked = float(input("Введите количество отработанных часов"))
hourly_rate = float(input("Введите почасовую ставку"))



if hours_worked > BASE_HOURS: # - УСЛОВИЕ

   # Инструкция: получить количество отработанных сверхурочных часов.
    overtime_hours = hours_worked - BASE_HOURS

    # Инструкция: рассчитать оплату за работу в сверхурочное время.
    overtime_pay = overtime_hours * hourly_rate * ON_MULTIPLAYER
    
    # Инструкция: рассчитать заработную плату до удержаний.
    gross_pay = BASE_HOURS * hourly_rate + overtime_pay
    
else: # - УСЛОВИЕ

    # Инструкция: рассчитать заработную плату до удержаний без сверхурочных.
    gross_pay = hours_worked * hourly_rate
    
    # Расчет налога и чистой прибыли
tax_amount = gross_pay * TAX_RATE   # Сумма налога
net_pay = gross_pay - tax_amount    # Сумма "на руки"



print(f"Заработная плата до удержаний: ${gross_pay:,.2f}")
print(f"Налог ({TAX_RATE*100:.0f}%): ${tax_amount:,.2f}")
print(f"Сумма к выдаче (на руки): ${net_pay:,.2f}")