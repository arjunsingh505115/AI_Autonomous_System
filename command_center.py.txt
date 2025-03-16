import os
from config_manager import ConfigManager

class CommandCenter:
    INBOX_FILE = "inbox/commands.txt"

    def __init__(self):
        self.config_manager = ConfigManager()

    def process_commands(self):
        if os.path.exists(self.INBOX_FILE):
            with open(self.INBOX_FILE, "r") as f:
                commands = f.readlines()

            if commands:
                for command in commands:
                    command = command.strip().lower()
                    if "install" in command:
                        tech = command.split("install")[1].strip()
                        self._install_technology(tech)
                    elif "upgrade" in command:
                        self._upgrade_system()
                    elif "check errors" in command:
                        self._check_errors()
                    elif "configure" in command:
                        self._handle_configure(command)
                    else:
                        print(f"📥 Executing: {command}")
                os.remove(self.INBOX_FILE)

    def _install_technology(self, tech):
        print(f"🔧 Installing {tech}...")
        # Add logic to install new technology here

    def _upgrade_system(self):
        print("🔄 Upgrading system...")
        # Add logic to upgrade the system here

    def _check_errors(self):
        print("🔍 Checking for errors...")
        # Add logic to check for errors here

    def _handle_configure(self, command):
        parts = command.split()
        if len(parts) == 3 and parts[0] == "configure":
            key = parts[1]
            value = parts[2]
            try:
                # Convert value to appropriate type (bool, int, or str)
                if value.lower() in ["true", "false"]:
                    value = value.lower() == "true"
                elif value.isdigit():
                    value = int(value)
                self.config_manager.update_config(key, value)
            except Exception as e:
                print(f"⚠️ Configuration failed: {e}")
        else:
            print("⚠️ Invalid configure command. Usage: configure <key> <value>")
