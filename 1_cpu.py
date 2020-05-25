#1 Определение полной информации о ЦП средствами Python
import psutil
import cpuinfo

def get_cpu_info():
    """Определение полной информации о ЦП"""
    info = cpuinfo.get_cpu_info()
    line = []
    dikt_in_txt = {}
    # Чтение в словарь dikt_in_txt основной информации о цп: Specification, Arch, Bits, Cores, Vent_id, 
    #                                                       Family, Model, Fiz_cores, Stepping, CPU_Usage              
    # C ключом CPU_INFO.
    line.append("Specification:" + info.get("brand"))
    line.append("Arch:" + info.get("arch"))
    line.append("Bits:" + repr(info.get("bits")))
    line.append("Cores:" + repr(info.get("count")))
    line.append("Vent_id:" + info.get("vendor_id"))
    line.append("Family:" + repr(info.get("family")))
    line.append("Model:" + repr(info.get("model")))
    line.append("Fiz_cores:" + repr(psutil.cpu_count(logical=False)))
    line.append("Stepping:" + repr(info.get("stepping")))
    line.append("CPU_Usage:" + repr(psutil.cpu_percent()))
    dikt_in_txt.update({"CPU_INFO":line})
    line = []
    # Чтение в словарь dikt_in_txt данных о кэше: l2 size, l3 size. C ключом Cache
    line.append("l2 size:" + info.get("l2_cache_size"))
    line.append("l3 size:" + info.get("l3_cache_size"))
    dikt_in_txt.update({"Cache":line})
    line = []
    cpufreq = psutil.cpu_freq()
    # Создание экземпляра класса cpu_freq()
    # Чтение в словарь dikt_in_txt данных о макс, текущ частоте: cpufreq.max, cpufreq.max. C ключом Frequency
    line.append("Max:{}Mhz".format(cpufreq.max))
    line.append("Current:{}Mhz".format(cpufreq.max))
    dikt_in_txt.update({"Frequency":line})
    line = []
    # Чтение в словарь dikt_in_txt данных загруженности ядер цп в формате Core{Номер ядра}:{Процент загруженности}%
    la = psutil.cpu_percent(percpu=True, interval=1)
    for i in range(0, info.get("count")):
        line.append("Core{}:{}%".format(i+1, la[i]))
    dikt_in_txt.update({"CPU_Usage_Per_Core":line})
    return dikt_in_txt

# Для отладки результата
if __name__ == "__main__":
    print(get_cpu_info())




