import wmi

def get_mother_info():
    """Определение полной информации о системной плате"""
    list_in_txt = []
    # Создание экземпляра класса WMI
    a = wmi.WMI()
    # Чтение данных из класса Win32_BaseBoard который хранит информацию о материнской плате
    class_info = a.Win32_BaseBoard()[0]
    # Чтение в список list_in_txt основной информации о материнской плате: 
    #     Caption, HostingBoard, HotSwappable, Manufacturer, Name, PoweredOn, 
    #     Product, Removable, Replaceable, RequiresDaughterBoard, SerialNumber, Status, 
    #     Tag, Version
    if class_info.Caption != None:
        list_in_txt.append("Caption:{}".format(class_info.Caption))
    if class_info.HostingBoard != None:
        list_in_txt.append("HostingBoard:" + repr(class_info.HostingBoard))
    if class_info.HotSwappable != None:
        list_in_txt.append("HotSwappable:" + repr(class_info.HotSwappable))
    if class_info.Manufacturer != None:
        list_in_txt.append("Manufacturer:" + class_info.Manufacturer)
    if class_info.Name != None:
        list_in_txt.append("Name:" + class_info.Name)
    if class_info.PoweredOn != None:
        list_in_txt.append("PoweredOn:" + repr(class_info.PoweredOn))
    if class_info.Product != None:
        list_in_txt.append("Product:" + class_info.Product)
    if class_info.Removable != None:
        list_in_txt.append("Removable:" + repr(class_info.Removable))
    if class_info.Replaceable != None:
        list_in_txt.append("Replaceable:" + repr(class_info.Replaceable))
    if class_info.RequiresDaughterBoard != None:
        list_in_txt.append("RequiresDaughterBoard:" + repr(class_info.RequiresDaughterBoard))
    if class_info.SerialNumber != None:
        list_in_txt.append("SerialNumber:" + class_info.SerialNumber)
    if class_info.Status != None:
        list_in_txt.append("Status:" + class_info.Status)
    if class_info.Tag != None:
        list_in_txt.append("Tag:" + class_info.Tag)
    if class_info.Version != None:
        list_in_txt.append("Version:" + class_info.Version)
    return {"MotherBoard":list_in_txt}

# Для отладки результата
if __name__ == "__main__":
    for x in get_mother_info():
        print(x)