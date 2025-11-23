
import winreg
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

WindowsProductID_REG_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"

def get_pdc_id() -> None:
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE , WindowsProductID_REG_PATH)
        value , _ = winreg.QueryValueEx(key, "ProductId")
        winreg.CloseKey(key)
        SHRMACEResult['WindowsProductId'] = copy.deepcopy(value)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2001] unable to get WindowsProductID.')