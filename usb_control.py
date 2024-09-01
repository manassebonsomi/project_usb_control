
import subprocess
def disable_usb_ports():
    try:
        # Commande pour désactiver les ports USB
        subprocess.run('reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" /v Start /t REG_DWORD /d 4 /f', shell=True, check=True)
        print("Les ports USB ont été désactivés.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la désactivation des ports USB : {e}")

### Activation des ports USB

def enable_usb_ports():
    try:
        # Commande pour activer les ports USB
        subprocess.run('reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" /v Start /t REG_DWORD /d 3 /f', shell=True, check=True)
        print("Les ports USB ont été activés.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'activation des ports USB : {e}")

### Execution du script
if __name__ == "__main__":
    choice = input("Voulez-vous activer ou désactiver les ports USB ? (activer/desactiver) : ").strip().lower()
    if choice == 'activer':
        enable_usb_ports()
    elif choice == 'desactiver':
        disable_usb_ports()
    else:
        print("Choix non reconnu.")
