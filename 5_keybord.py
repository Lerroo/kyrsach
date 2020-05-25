import wmi

def get_keybord_info():
    """Определение полной информации об клавиатуре"""
    list_in_txt = []
    # Создание экземпляра класса WMI
    c = wmi.WMI()
    # Чтение данных из класса Win32_Keyboard который хранит информацию о клавиатуре
    for x in c.Win32_Keyboard():
        line = []
        # Чтение в список line собранной информации о клавиатуре:
        #     Availability, Description, DeviceID, IsLocked, Layout, Name, NumberOfFunctionKeys, Password, 
        #     ConfigManagerErrorCode, PowerManagementSupported, ConfigManagerUserConfig, Status, StatusInfo
        if x.Availability != None:
            line.append("Availability:" + repr(x.Availability))
        if x.Description != None:
            line.append("Description:" + x.Description)
        if x.DeviceID != None:
            line.append("DeviceID:" + x.DeviceID)
        if x.IsLocked != None:
            line.append("IsLocked:" + x.IsLocked)
        if x.Layout != None:
            line.append("Layout:" + x.Layout)
        if x.Name != None:
            line.append("Name:" + x.Name)
        if x.NumberOfFunctionKeys != None:
            line.append("NumberOfFunctionKeys:" + repr(x.NumberOfFunctionKeys))
        if x.Password != None:
            line.append("Password:" + repr(x.Password))
        if x.ConfigManagerErrorCode != None:
            line.append("ConfigManagerErrorCode:" + repr(x.ConfigManagerErrorCode))
        if x.PowerManagementSupported != None:
            line.append("PowerManagementSupported:" + repr(x.PowerManagementSupported))
        if x.ConfigManagerUserConfig != None:
            line.append("ConfigManagerUserConfig:" + repr(x.ConfigManagerUserConfig))
        if x.Status != None:
            line.append("Status:" + x.Status)
        if x.StatusInfo != None:
            line.append("StatusInfo:" + repr(x.StatusInfo))
        list_in_txt.append(line)
    return {"Keyboard":list_in_txt}
    
# Для отладки результата
if __name__ == "__main__":
    for x in get_keybord_info():
        print(x)
    
    