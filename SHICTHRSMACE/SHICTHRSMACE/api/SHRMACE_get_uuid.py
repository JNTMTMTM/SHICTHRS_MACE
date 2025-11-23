
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult

def get_uuid() -> None:
    try:
        c = wmi.WMI()
        for system in c.Win32_ComputerSystemProduct():
            SHRMACEResult['WindowsUUID'] = copy.deepcopy(system.UUID)
    except:
        SHRMACEResult['WindowsUUID'] = 'N/A'