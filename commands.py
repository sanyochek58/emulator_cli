import os

class CommandExecutor:
    def __init__(self, vfs_dir):
        self.vfs_dir = vfs_dir
        self.current_dir = vfs_dir

    def execute(self, command):
        parts = command.split()
        cmd = parts[0]

        if cmd == "ls":
            return self.ls(parts[1] if len(parts) > 1 else ".")
        elif cmd == "cd":
            return self.cd(parts[1] if len(parts) > 1 else "." )
        elif cmd == "du":
            return self.du(parts[1] if len(parts) > 1 else "." )
        elif cmd == "wc":
            return self.wc(parts[1] if len(parts) > 1 else "." )
        elif cmd == "chown":
            return self.chown(parts[1], parts[2] if len(parts) > 2 else ".")
        else:
            return f"Unknown command: {cmd}"

    def ls(self, path):
        full_path = os.path.join(self.current_dir, path)
        try:
            return "\n".join(os.listdir(full_path))
        except FileNotFoundError:
            return f"No such directory: {full_path}"

    def cd(self, path):
        if path == "..":
            new_dir = os.path.dirname(self.current_dir)
            if new_dir.startswith(self.vfs_dir):
                self.current_dir = new_dir
                return f"Changed directory to {self.current_dir}"
            else:
                return "You cannot go above the root directory."
        else:
            full_path = os.path.join(self.current_dir, path)
            if os.path.isdir(full_path):
                self.current_dir = full_path
                return f"Changed directory to {full_path}"
            else:
                return f"No such directory: {full_path}"

    def du(self, path):
        full_path = os.path.join(self.vfs_dir, path)
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(full_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return f"Total size: {total_size} bytes"

    def wc(self, path=None):
        if not path or path == ".":
            return "Error: No file specified for wc command."
        
        full_path = os.path.join(self.current_dir, path)
        try:
            with open(full_path, 'r') as f:
                contents = f.read()
                lines = contents.splitlines()
                return f"Lines: {len(lines)}, Words: {len(contents.split())}, Bytes: {len(contents.encode())}"
        except FileNotFoundError:
            return f"File not found: {full_path}"

    def chown(self, user, path):
        return f"Changed owner of {path} to {user} (not actually implemented)"