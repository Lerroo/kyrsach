import wmi

def WMIDateStringToDate(comp_data):
    """Функция для конвертации из системной даты в привычный вид"""
    str_result = ""
    if (comp_data[4] == 0):
        str_result = comp_data[5] + '/'
    else:
        str_result = comp_data[4] + comp_data[5] + '/'
    if (comp_data[6] == 0):
        str_result = str_result + comp_data[7] + '/'
    else:
        str_result = str_result + comp_data[6] + comp_data[7] + '/'
        str_result = str_result + comp_data[0] + comp_data[1] + comp_data[2] + comp_data[3] + " " + comp_data[8] + comp_data[9] + ":" + comp_data[10] + comp_data[11] +':' + comp_data[12] + comp_data[13]
    return str_result

def get_bios_info():
    """Функция собирания информации о BIOS"""
    list_in_txt = []
    str_result = ""
    # Создание экземпляра класса WMI
    c = wmi.WMI()
    # Чтение данных из класса Win32_BIOS который хранит информацию о BIOS
    for x in c.Win32_BIOS():
        # Чтение в словарь dikt_in_txt основной информации о BIOS: 
        #     BiosCharacteristics, BuildNumber, CodeSet, CurrentLanguage, IdentificationCode, PrimaryBIOS, 
        #     ReleaseDate, SerialNumber, SMBIOSBIOSVersion, InstallableLanguages, InstallDate, LanguageEdition, 
        #     ListOfLanguages, Manufacturer, OtherTargetOS, SMBIOSMajorVersion, SMBIOSMinorVersion, SMBIOSPresent, 
        #     SoftwareElementID, Status, Version           
        # C ключом Bios. 
        try:
            for obj_elem in x.BiosCharacteristics:
                str_result = str_result + repr(obj_elem) + ','
        except:
            str_result = str_result + 'None'
        list_in_txt.append("BiosCharacteristics:" + str_result[:-1])
        if x.BuildNumber != None:
            list_in_txt.append("BuildNumber:" + repr(x.BuildNumber))
        if x.CodeSet != None:
            list_in_txt.append("CodeSet:" + repr(x.CodeSet))
        if x.CurrentLanguage != None:
            list_in_txt.append("CurrentLanguage:" + x.CurrentLanguage)
        if x.IdentificationCode != None:
            list_in_txt.append("IdentificationCode:" + repr(x.IdentificationCode))
        if x.InstallableLanguages != None:
            list_in_txt.append("InstallableLanguages:" + repr(x.InstallableLanguages))
        if x.InstallDate != None:
            list_in_txt.append("InstallDate:" + WMIDateStringToDate(x.InstallDate))
        if x.LanguageEdition != None:
            list_in_txt.append("LanguageEdition:" + repr(x.LanguageEdition))
        str_result = ""
        try :
            for obj_elem in x.ListOfLanguages :
                str_result = str_result + obj_elem + ","
        except:
            str_result = str_result + 'None'
        list_in_txt.append("ListOfLanguages:" + str_result[:-2].replace(",,,",""))
        if x.Manufacturer != None:
            list_in_txt.append("Manufacturer:" + x.Manufacturer)
        if x.OtherTargetOS != None:
            list_in_txt.append("OtherTargetOS:" + repr(x.OtherTargetOS))
        if x.PrimaryBIOS != None:
            list_in_txt.append("PrimaryBIOS:" + repr(x.PrimaryBIOS))
        if x.ReleaseDate != None:
            list_in_txt.append("ReleaseDate:" + WMIDateStringToDate(x.ReleaseDate))
        if x.SerialNumber != None:
            list_in_txt.append("SerialNumber:" + x.SerialNumber)
        if x.SMBIOSBIOSVersion != None:
            list_in_txt.append("SMBIOSBIOSVersion:" + x.SMBIOSBIOSVersion)
        if x.SMBIOSMajorVersion != None:
            list_in_txt.append("SMBIOSMajorVersion:" + repr(x.SMBIOSMajorVersion))
        if x.SMBIOSMinorVersion != None:
            list_in_txt.append("SMBIOSMinorVersion:" + repr(x.SMBIOSMinorVersion))
        if x.SMBIOSPresent != None:
            list_in_txt.append("SMBIOSPresent:" + repr(x.SMBIOSPresent))
        if x.SoftwareElementID != None:
            list_in_txt.append("SoftwareElementID:" + x.SoftwareElementID)
        if x.Status != None:
            list_in_txt.append("Status:" + x.Status)
        if x.Version != None:
            list_in_txt.append("Version:" + x.Version)
    return {"Bios":list_in_txt}

# Для отладки результата
if __name__ == "__main__":
    print(get_bios_info())