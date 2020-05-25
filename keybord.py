# 5.		Определение полной информации об использовании клавиатуры средствами Pyton
import win32com.client
import main

def get_keybord_info():
    list_in_txt = []
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_Keyboard")
    for objItem in colItems:
        if objItem.Availability != None:
            list_in_txt.append("Availability:" + repr(objItem.Availability))
        if objItem.Description != None:
            list_in_txt.append("Description:" + repr(objItem.Description))
        if objItem.DeviceID != None:
            list_in_txt.append("DeviceID:" + repr(objItem.DeviceID))
        if objItem.ErrorCleared != None:
            list_in_txt.append("ErrorCleared:" + repr(objItem.ErrorCleared))
        if objItem.ErrorDescription != None:
            list_in_txt.append("ErrorDescription:" + repr(objItem.ErrorDescription))
        if objItem.IsLocked != None:
            list_in_txt.append("IsLocked:" + repr(objItem.IsLocked))
        if objItem.LastErrorCode != None:
            list_in_txt.append("LastErrorCode:" + repr(objItem.LastErrorCode))
        if objItem.Layout != None:
            list_in_txt.append("Layout:" + repr(objItem.Layout))
        if objItem.Name != None:
            list_in_txt.append("Name:" + repr(objItem.Name))
        if objItem.NumberOfFunctionKeys != None:
            list_in_txt.append("NumberOfFunctionKeys:" + repr(objItem.NumberOfFunctionKeys))
        if objItem.Password != None:
            list_in_txt.append("Password:" + repr(objItem.Password))
        if objItem.ConfigManagerErrorCode != None:
            list_in_txt.append("ConfigManagerErrorCode:" + repr(objItem.ConfigManagerErrorCode))
        if objItem.PowerManagementSupported != None:
            list_in_txt.append("PowerManagementSupported:" + repr(objItem.PowerManagementSupported))
        if objItem.ConfigManagerUserConfig != None:
            list_in_txt.append("ConfigManagerUserConfig:" + repr(objItem.ConfigManagerUserConfig))
        if objItem.Status != None:
            list_in_txt.append("Status:" + repr(objItem.Status))
        if objItem.StatusInfo != None:
            list_in_txt.append("StatusInfo:" + repr(objItem.StatusInfo))
        list_in_txt.append("----------------------------------------")
    return list_in_txt

if __name__ == "__main__":
    for x in get_keybord_info():
        print(x)
    
    