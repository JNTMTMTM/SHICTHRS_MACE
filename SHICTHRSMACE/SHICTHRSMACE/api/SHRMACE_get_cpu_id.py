
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_cpu_id() -> None:
    try:
        c = wmi.WMI()
        cpuid : str = ''
        for cpu in c.Win32_Processor():
            cpuid += cpu.ProcessorId.strip() + ' '
        SHRMACEResult['CPUID'] = copy.deepcopy(cpuid.strip().upper())
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2003] unable to get CPU id.')