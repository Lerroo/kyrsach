#11.		Определение информации о запущенных приложениях средствами Pyton
from subprocess import Popen, PIPE
def get_graphics_card_info():
    list_in_txt = []
    # 'Имя образа, PID Имя сессии, № сеанса, Память'
    for line in Popen('tasklist', stdout=PIPE).stdout.readlines()[3:]:
        app_info = str(line.decode('cp866', 'ignore')).split()
        app_info[-2] = app_info[-2]+app_info[-1]
        list_in_txt.append(app_info[:-1])
    return list_in_txt

if __name__ == "__main__":
    for x in get_graphics_card_info():
        print(x)