# Network Router Configuration Store
# Uses tuples for fixed (immutable) configurations
# and dictionary to map device names to those configs

# Main storage
# Key   = device name
# Value = tuple (IP, Port, Description)
router_configs = {}


def add_device(device_name, ip, port, description=""):
    """Adds a new device configuration as a tuple."""
    if device_name in router_configs:
        print(f"Device '{device_name}' already exists.")
        return False

    config = (ip, port, description)          # tuple → immutable
    router_configs[device_name] = config
    print(f"Device '{device_name}' added successfully.")
    return True


def view_device(device_name):
    """Shows details of one device."""
    if device_name not in router_configs:
        print(f"Device '{device_name}' not found.")
        return

    ip, port, desc = router_configs[device_name]
    print("\n---------- Device Details ----------")
    print(f"Device Name  : {device_name}")
    print(f"IP Address   : {ip}")
    print(f"Port         : {port}")
    print(f"Description  : {desc if desc else 'N/A'}")
    print("------------------------------------")


def view_all_devices():
    """Displays all stored devices."""
    if not router_configs:
        print("No devices have been added yet.")
        return

    print("\n--------------- All Device Configurations ---------------")
    print(f"{'Device Name':15} | {'IP Address':15} | {'Port':5} | Description")
    print("-" * 60)
    for name, config in router_configs.items():
        ip, port, desc = config
        print(f"{name:15} | {ip:15} | {port:<5} | {desc}")
    print("-" * 60)


def try_modify_config(device_name, new_ip):
    """Tries to directly change the IP (this will fail intentionally)."""
    if device_name not in router_configs:
        print(f"Device '{device_name}' not found.")
        return

    print(f"\nTrying to change IP of '{device_name}' to {new_ip}...")
    try:
        router_configs[device_name][0] = new_ip     # This line will raise error
    except TypeError as e:
        print("Modification failed!")
        print("Reason:", e)
        print("This is expected because the configuration is stored in a tuple.")


def update_device(device_name, new_ip=None, new_port=None, new_desc=None):
    """Proper way to update by creating a new tuple."""
    if device_name not in router_configs:
        print(f"Device '{device_name}' not found.")
        return False

    old_ip, old_port, old_desc = router_configs[device_name]

    ip = new_ip if new_ip is not None else old_ip
    port = new_port if new_port is not None else old_port
    desc = new_desc if new_desc is not None else old_desc

    router_configs[device_name] = (ip, port, desc)   # replace with new tuple
    print(f"Device '{device_name}' updated successfully.")
    return True


def show_menu():
    print("\n========== Network Router Configuration Store ==========")
    print("1. Add New Device")
    print("2. View All Devices")
    print("3. View Specific Device")
    print("4. Try to Modify Config (Demonstration)")
    print("5. Update Device (Safe Way)")
    print("6. Exit")
    print("========================================================")


# ========== Main Program ==========
if __name__ == "__main__":

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Add New Device ---")
            name = input("Enter Device Name: ").strip()
            ip = input("Enter IP Address: ").strip()
            port = input("Enter Port Number: ").strip()
            desc = input("Enter Description (optional): ").strip()

            if name and ip and port:
                try:
                    port = int(port)
                    add_device(name, ip, port, desc)
                except ValueError:
                    print("Port must be a number.")
            else:
                print("Device name, IP and Port are required.")

        elif choice == "2":
            view_all_devices()

        elif choice == "3":
            name = input("\nEnter Device Name to view: ").strip()
            view_device(name)

        elif choice == "4":
            name = input("\nEnter Device Name: ").strip()
            new_ip = input("Enter New IP (this will fail): ").strip()
            try_modify_config(name, new_ip)

        elif choice == "5":
            print("\n--- Update Device (Safe Method) ---")
            name = input("Enter Device Name: ").strip()

            if name not in router_configs:
                print(f"Device '{name}' not found.")
                continue

            print("Leave blank if you don't want to change that field.")
            new_ip = input("New IP Address: ").strip()
            new_port = input("New Port: ").strip()
            new_desc = input("New Description: ").strip()

            # Convert empty inputs to None
            new_ip = new_ip if new_ip else None
            new_port = int(new_port) if new_port else None
            new_desc = new_desc if new_desc else None

            update_device(name, new_ip, new_port, new_desc)

        elif choice == "6":
            print("\nExiting program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")