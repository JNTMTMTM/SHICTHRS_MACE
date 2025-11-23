
import wmi
import copy
from ..SHRMACE_ErrorBase import SHRMACEException

def get_mb_info(var) -> None:
    try:
        c = wmi.WMI()
        MB_INFO = ''
        for board in c.Win32_BaseBoard():
            MB_INFO = board.Manufacturer + board.Product
        var.SHRMACEResult['MotherBoardINFO'] = copy.deepcopy(MB_INFO)
    except Exception as e:
        raise SHRMACEException(f'SHRMACEException [ERROR.2005] unable to get MotherBoard info. | {str(e)}')