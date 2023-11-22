import os
import json

file_path = "F:/FRAS/NewRegistration/NewRegisterInfo.json"

try:
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)

    # Load user data from file
    with open(file_path, "r") as f:
        users = json.load(f)

except PermissionError:
    print("Error: Permission denied. Check file permissions or run the program with administrator privileges.")

except Exception as e:
    print(f"Error: {e}")
    users = {}