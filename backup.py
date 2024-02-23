import shutil
import os
import subprocess
from datetime import datetime
from talon import Module, actions, app

mod = Module()

folders = {
    'root': os.path.expanduser(r"C:\\Users\\Emmanuel\\AppData\\Roaming\\talon\\user\\em"),
    'github-backup': os.path.expanduser(r"C:\\Users\\Emmanuel\\Documents\\GitHub\\talon-scripts\\talon-scripts")
}

@mod.action_class
class UserActions:
    def backup_and_commit_scripts(source: str, destination: str):
        """Copies scripts from the specified source folder to the specified destination folder and commits them."""
        source_dir = folders.get(source, '')
        destination_dir = folders.get(destination, '')
        
        if not source_dir or not destination_dir:
            app.notify("Source or destination path is not defined.")
            return
        
        # Ensure the destination directory exists
        os.makedirs(destination_dir, exist_ok=True)
        
        try:
            # List all files and directories in source directory
            entries = os.listdir(source_dir)
            
            # Copy each item to the destination directory
            for entry in entries:
                full_entry_name = os.path.join(source_dir, entry)
                if os.path.isfile(full_entry_name):
                    shutil.copy(full_entry_name, destination_dir)
                elif os.path.isdir(full_entry_name):
                    dest_dir = os.path.join(destination_dir, entry)
                    shutil.copytree(full_entry_name, dest_dir, dirs_exist_ok=True)
            
            # Create a temporary script with Git commands
            commit_message = datetime.now().strftime('%Y-%m-%d Backup')
            script_content = f'cd "{destination_dir}"\ngit add .\ngit commit -m "{commit_message}"\n'
            script_path = os.path.join(destination_dir, "temp_git_commands.sh")
            with open(script_path, "w") as script_file:
                script_file.write(script_content)
            
            # Open Git Bash and execute the script
            git_bash_path = r"C:\Program Files\Git\git-bash.exe"
            subprocess.Popen([git_bash_path, '--cd=' + destination_dir, '-c', f'bash {script_path}'])
            
            # Clean up the temporary script after a delay
            time.sleep(2)  # Wait for the script to likely finish
            os.remove(script_path)
            
            app.notify("Scripts backed up and committed successfully.")
        except Exception as e:
            app.notify(f"Failed to backup and commit scripts: {str(e)}")
