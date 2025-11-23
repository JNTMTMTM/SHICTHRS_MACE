
import wmi
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_cpu_vendor() -> None:
    try:
        c = wmi.WMI()
        for processor in c.Win32_Processor():
            name = processor.Name.lower()
            manufacturer = processor.Manufacturer.lower()
            if 'intel' in manufacturer or 'intel' in name:
                SHRMACEResult['CPUVendor'] = 'intel'
            elif 'amd' in manufacturer or 'amd' in name:
                SHRMACEResult['CPUVendor'] = 'amd'
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2004] unable to get CPU vendor.')