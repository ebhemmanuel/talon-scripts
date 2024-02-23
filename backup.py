import shutil
import os
import subprocess
from datetime import datetime
from talon import Module, actions, app
import time

mod = Module()

folders = {
    'root': os.path.expanduser(r"C:\Users\Emmanuel\AppData\Roaming\talon\user\em"),
    'github-backup': os.path.expanduser(r"C:\Users\Emmanuel\Documents\GitHub\talon-scripts\talon-scripts")
}

@mod.action_class
class UserActions:
    def deploy_talon_scripts(source: str, destination: str):
        """Deploys scripts from the GitHub repository to the Talon user folder."""
        source_dir = folders.get(source, '')
        destination_dir = folders.get(destination, '')
        
        if not source_dir or not destination_dir:
            app.notify("Source or destination path is not defined.")
            return
        
        # Ensure the source directory exists
        if not os.path.exists(source_dir):
            app.notify(f"Source directory does not exist: {source_dir}")
            return
        
        try:
            # Clean destination directory before deploying
            for entry in os.listdir(destination_dir):
                full_path = os.path.join(destination_dir, entry)
                if os.path.isfile(full_path):
                    os.remove(full_path)
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
            
            # Copy each item from the source to the destination directory
            entries = os.listdir(source_dir)
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
            app.notify(f"Failed to deploy Talon scripts: {str(e)}")
