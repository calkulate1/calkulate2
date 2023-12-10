def bank(many, years, percent):
    a = many * (1 + (percent / 100) * years)
    print(f'в итоге вам придется выплотить...\n{a}')


bank(float(input('сколько денег вы берете... \n')), float(input('на сколько лет... \n')), float(input('под сколько процентов... \n')))
