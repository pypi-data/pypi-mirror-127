import vpncmd
import re
import time


vc = vpncmd.VPNCMD(r"C:\Program Files\SoftEther VPN Client\vpncmd_x64.exe", True)
vc.setup_cmd("/client", "localhost")
# vc.VPN_Client_Management.NicCreate("VPN2")
# vc.connect_random_vpn("VPN2")
vc.connect_random_vpn()
while not vc.is_connected_to_vpn():
    time.sleep(0.5)
time.sleep(5)
vc.disconnect_vpn()



