import psutil
def get_disks():
    """Определение полной информации о разделах HDD"""
    list_in_txt = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        # Эти две строки можно удалить прост конкретно у меня тут трабл с этим диском, у тебя не будет
        if str(partition.device)=="D:\\":
            continue
        p = psutil.disk_usage(partition.mountpoint)
        # Чтение в список list_in_txt данных о разделах HDD:
        #     p.fstype, p.used, p.free, p.total
        list_in_txt.append({str(partition.device):'File_system_type:{},Used:{:.2f},FreeSpace:{:.2f}Gb,Size:{:.2f}Gb'.format(
            p.fstype, p.used/1024/1024/1024, int(p.free)/1024/1024/1024, int(p.total)/1024/1024/1024)})
    return {"Disks":list_in_txt}

# Для отладки результата
if __name__ == '__main__':
    print(get_disks())