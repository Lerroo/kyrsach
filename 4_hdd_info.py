# 4.Определение полной информации об HDD средствами Python
import wmi

def get_hdd_info():
    """Определение полной информации об HDD"""
    list_in_txt = []
    # Создание экземпляра класса WMI
    c = wmi.WMI()
    # Чтение данных из класса Win32_PhysicalMedia который хранит данные о hdd 
    for item in c.Win32_PhysicalMedia():
        line =[]
        # Чтение в список line данных SerialNumber, Tag
        line.append("SerialNumber:"+ str(item.SerialNumber).replace(" ",''))
        line.append("Tag:"+ item.Tag[repr(item.Tag).rfind("\\"):])
        list_in_txt.append(line)
    return {"HDD":list_in_txt}

# Для отладки результата
if __name__ == "__main__":
    print(get_hdd_info())
    
    