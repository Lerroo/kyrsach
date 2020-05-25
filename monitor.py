# 9.		Определение полной информации о мониторе средствами Pyton
import wmi
def get_monitor_info():
    list_in_txt = []
    a = wmi.WMI()
    class_info = a.Win32_DesktopMonitor()[0]
    if class_info.Bandwidth != None:
        list_in_txt.append("Bandwidth:" + repr(class_info.Bandwidth))
    if class_info.DeviceID != None:
        list_in_txt.append("DeviceID:" + class_info.DeviceID)
    if class_info.DisplayType != None:
        list_in_txt.append("DisplayType:" + repr(class_info.DisplayType))
    if class_info.ErrorCleared != None:
        list_in_txt.append("ErrorCleared:" + repr(class_info.ErrorCleared))
    if class_info.ErrorDescription != None:
        list_in_txt.append("ErrorDescription:" + repr(class_info.ErrorDescription))
    if class_info.MonitorManufacturer != None:
        list_in_txt.append("MonitorManufacturer:" + class_info.MonitorManufacturer[1:-1])
    if class_info.Name != None:
        list_in_txt.append("Name:" + class_info.Name)
    if class_info.PixelsPerXLogicalInch != None:
        list_in_txt.append("PixelsPerXLogicalInch:" + repr(class_info.PixelsPerXLogicalInch))
    if class_info.PixelsPerYLogicalInch != None:
        list_in_txt.append("PixelsPerYLogicalInch:" + repr(class_info.PixelsPerYLogicalInch))
    if class_info.PNPDeviceID != None:
        list_in_txt.append("PNPDeviceID:" + class_info.PNPDeviceID)
    if class_info.PowerManagementSupported != None:
        list_in_txt.append("PowerManagementSupported:" + repr(class_info.PowerManagementSupported))
    if class_info.ScreenHeight != None:
        list_in_txt.append("ScreenHeight:" + repr(class_info.ScreenHeight))
    if class_info.ScreenWidth != None:
        list_in_txt.append("ScreenWidth:" + repr(class_info.ScreenWidth))
    if class_info.Status != None:
        list_in_txt.append("Status:" + class_info.Status)
    if class_info.StatusInfo != None:
        list_in_txt.append("StatusInfo:" + repr(class_info.StatusInfo))
    return list_in_txt

if __name__ == "__main__":
    for x in get_monitor_info():
        print(x)