import wmi

def get_monitor_info():
    list_in_txt = []
    line = []
    a = wmi.WMI()
    class_info = a.Win32_NetworkAdapter()
    for x in class_info:
        if x.AdapterType != None:
            line.append("AdapterType:" + x.AdapterType)
        if x.AdapterTypeId != None:
            line.append("AdapterTypeId:" + repr(x.AdapterTypeId))
        if x.AutoSense != None:
            line.append("AutoSense:" + repr(x.AutoSense))
        if x.Availability != None:
            line.append("Availability:" + repr(x.Availability))
        if x.DeviceID != None:
            line.append("DeviceID:" + x.DeviceID)
        if x.Index != None:
            line.append("Index:" + repr(x.Index))
        if x.InterfaceIndex != None:
            line.append("InterfaceIndex:" + repr(x.InterfaceIndex))
        if x.LastErrorCode != None:
            line.append("LastErrorCode:" + repr(x.LastErrorCode))
        if x.MACAddress != None:
            line.append("MACAddress:" + x.MACAddress)
        if x.Manufacturer != None:
            line.append("Manufacturer:" + x.Manufacturer)
        if x.MaxSpeed != None:
            line.append("MaxSpeed:" + x.MaxSpeed)
        if x.Name != None:
            line.append("Name:" + x.Name)
        if x.NetConnectionID != None:
            line.append("NetConnectionID:" + x.NetConnectionID)
        if x.NetConnectionStatus != None:
            line.append("NetConnectionStatus:" + repr(x.NetConnectionStatus))
        line.append("NetworkAddresses:")
        strList = ""
        if x.NetworkAddresses != None:
            for objElem in x.NetworkAddresses:
                strList = strList + repr(objElem) + ","
            line.append(strList)
        if x.PermanentAddress != None:
            line.append("PermanentAddress:" + repr(x.PermanentAddress))
        if x.PNPDeviceID != None:
            line.append("PNPDeviceID:" + x.PNPDeviceID)
        if x.PowerManagementSupported != None:
            line.append("PowerManagementSupported:" + repr(x.PowerManagementSupported))
        if x.ProductName != None:
            line.append("ProductName:" + x.ProductName)
        if x.ServiceName != None:
            line.append("ServiceName:" + x.ServiceName)
        if x.Speed != None:
            line.append("Speed:" + x.Speed)
        if x.Status != None:
            line.append("Status:" + repr(x.Status))
        list_in_txt.append(line)
        line = []
    return list_in_txt

if __name__ == "__main__":
    for x in get_monitor_info():
        for a in x:
            print(a)
        print('---------')