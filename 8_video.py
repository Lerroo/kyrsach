import wmi

def get_graphics_card_info():
    """Определение полной информации о видеокарте"""
    list_in_txt = []
    # Создание экземпляра класса WMI
    a = wmi.WMI()
    # Чтение данных из класса Win32_VideoController который хранит информацию о видеокарте
    class_info = a.Win32_VideoController()[0]
    # Чтение в список list_in_txt основной информации о BIOS:
    #     AdapterCompatibility, AdapterDACType, AdapterRAM, Availability, Caption, ConfigManagerUserConfig,
    #     CurrentBitsPerPixel, CurrentHorizontalResolution, CurrentNumberOfColors, CurrentNumberOfColumns,
    #     CurrentNumberOfRows, CurrentRefreshRate, CurrentScanMode, CurrentVerticalResolution, DeviceID,
    #     DitherType, DriverDate, DriverVersion, InfFilename, InfSection, InstalledDisplayDrivers,
    #     MinRefreshRate, Monochrome, PNPDeviceID, Status, VideoArchitecture, MaxRefreshRate, VideoMemoryType,
    #     VideoModeDescription, VideoProcessor
    if class_info.AdapterCompatibility != None:
        list_in_txt.append("AdapterCompatibility:{}".format(class_info.Caption))
    if class_info.AdapterDACType != None:
        list_in_txt.append("AdapterDACType:" + class_info.AdapterDACType)
    if class_info.AdapterRAM != None:
        list_in_txt.append("AdapterRAM:" + repr(class_info.AdapterRAM))
    if class_info.Availability != None:
        list_in_txt.append("Availability:" + repr(class_info.Availability))
    if class_info.Caption != None:
        list_in_txt.append("Caption:" + class_info.Caption)
    if class_info.ConfigManagerUserConfig != None:
        list_in_txt.append("ConfigManagerUserConfig:" + repr(class_info.ConfigManagerUserConfig))
    if class_info.CurrentBitsPerPixel != None:
        list_in_txt.append("CurrentBitsPerPixel:" + repr(class_info.CurrentBitsPerPixel))
    if class_info.CurrentHorizontalResolution != None:
        list_in_txt.append("CurrentHorizontalResolution:" + repr(class_info.CurrentHorizontalResolution))
    if class_info.CurrentNumberOfColors != None:
        list_in_txt.append("CurrentNumberOfColors:" + class_info.CurrentNumberOfColors)
    if class_info.CurrentNumberOfColumns != None:
        list_in_txt.append("CurrentNumberOfColumns:" + repr(class_info.CurrentNumberOfColumns))
    if class_info.CurrentNumberOfRows != None:
        list_in_txt.append("CurrentNumberOfRows:" + repr(class_info.CurrentNumberOfRows))
    if class_info.CurrentRefreshRate != None:
        list_in_txt.append("CurrentRefreshRate:" + repr(class_info.CurrentRefreshRate))
    if class_info.CurrentScanMode != None:
        list_in_txt.append("CurrentScanMode:" + repr(class_info.CurrentScanMode) )
    if class_info.CurrentVerticalResolution != None:
        list_in_txt.append("CurrentVerticalResolution:" + repr(class_info.CurrentVerticalResolution))
    if class_info.DeviceID != None:
        list_in_txt.append("DeviceID:" + class_info.DeviceID)
    if class_info.DitherType != None:
        list_in_txt.append("DitherType:" + repr(class_info.DitherType))
    if class_info.DriverDate != None:
        list_in_txt.append("DriverDate:" + class_info.DriverDate)
    if class_info.DriverVersion != None:
        list_in_txt.append("DriverVersion:" + class_info.DriverVersion)
    if class_info.InfFilename != None:
        list_in_txt.append("InfFilename:" + class_info.InfFilename)
    if class_info.InfSection != None:
        list_in_txt.append("InfSection:" + class_info.InfSection)
    if class_info.InstalledDisplayDrivers != None:
        list_in_txt.append("InstalledDisplayDrivers:" + class_info.InstalledDisplayDrivers)
    if class_info.MaxRefreshRate != None:
        list_in_txt.append("MaxRefreshRate:" + repr(class_info.MaxRefreshRate))
    if class_info.MinRefreshRate != None:
        list_in_txt.append("MinRefreshRate:" + repr(class_info.MinRefreshRate))
    if class_info.Monochrome != None:
        list_in_txt.append("Monochrome:" + repr(class_info.Monochrome))
    if class_info.PNPDeviceID != None:
        list_in_txt.append("PNPDeviceID:" + class_info.PNPDeviceID)
    if class_info.Status != None:
        list_in_txt.append("Status:" + class_info.Status)
    if class_info.VideoArchitecture != None:
        list_in_txt.append("VideoArchitecture:" + repr(class_info.VideoArchitecture))
    if class_info.VideoMemoryType != None:
        list_in_txt.append("VideoMemoryType:" + repr(class_info.VideoMemoryType))
    if class_info.VideoModeDescription != None:
        list_in_txt.append("VideoModeDescription:" + class_info.VideoModeDescription)
    if class_info.VideoProcessor != None:
        list_in_txt.append("VideoProcessor:" + class_info.VideoProcessor) 
    return {"Video":list_in_txt}
    
# Для отладки результата
if __name__ == "__main__":
    for x in get_graphics_card_info():
        print(x)