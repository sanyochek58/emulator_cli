import json
import os
import subprocess
import zipfile
from commands import CommandExecutor


class ShellSim:
    def __init__(self, conf_path):
        self.load_config(conf_path)
        self.vfs_dir = self.extract_vfs()
        self.executor = CommandExecutor(self.vfs_dir)

    def load_config(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        self.username = config['username']
        self.vfs_path = config['vfs_path']
        self.startup_script = config['startup_script']

    def extract_vfs(self):
        temp_dir = "vfs_temp"
        with zipfile.ZipFile(self.vfs_path, 'r') as Myzip:
            Myzip.extractall(temp_dir)
        return temp_dir

    def run(self):
        if self.startup_script:
            self.execute_startup_script()
        while True:
            command = input(f"{self.username}@emulator:~$ ")
            if command.strip() == "exit":
                break
            # Добавляем вывод результата команды
            result = self.executor.execute(command)
            print(result)

    def execute_startup_script(self):
        with open(self.startup_script) as f:
            for command in f:
                self.executor.execute(command.strip())


if __name__ == "__main__":
    emulator = ShellSim("conf.json")
    emulator.run()