import random
import subprocess
from talon import Module, actions, app
import os

mod = Module()

app_paths = {
    "firefox": r"C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "vscode": r"C:\Users\Emmanuel\AppData\Local\Programs\Microsoft VS Code\\Code.exe",
    "discord": r"C:\\Users\\Emmanuel\AppData\\Local\Discord\\Update.exe",  
    "spotify": r"C:\\Users\\Emmanuel\AppData\\Roaming\Spotify\Spotify.exe",  
    "slack": r"C:\\Users\\Emmanuel\AppData\\AppData\\Local\slack\Slack.exe",
    "obsidian": r"C:\\Users\\Emmanuel\\AppData\\Local\\Obsidian\\Obsidian.exe",
    "steam": r"C:\\Program Files (x86)\\Steam\\steam.exe",
    # Add more applications here
}

folders = {
    "aimset": r"C:\\Users\\Emmanuel\\Documents\\GitHub\\aimset-main-site-with-admin"
    # Add more folder shortcuts here
}

# List of cool websites
cool_websites = [
    "https://asoftmurmur.com/",
    "https://www.window-swap.com/",
    "http://radio.garden/",
    "https://thisissand.com/",

]

@mod.action_class
class Actions:
    # When opening browser start on a website from the list
    def open_random_cool_site():
        """Opens a random cool website in Firefox."""
        site = random.choice(cool_websites)
        firefox_path = app_paths["firefox"]  # Use the dictionary for consistency
        subprocess.Popen([firefox_path, site], creationflags=subprocess.CREATE_NO_WINDOW)


    def new_tab():
        """Opens a new tab in Firefox using nircmd"""
        # Using nircmd without specifying its path, as it's in the System32 folder
        cmd = 'nircmd execmd "C:\\Program Files\Mozilla Firefox\\firefox.exe" -new-tab about:newtab'
        os.system(cmd)

    def open_last_tab():
        """Reopens the last closed tab in Firefox"""
        # Simulates the Ctrl+Shift+T keystroke
        actions.key("ctrl-shift-t")

    def close_tab():
        """Reopens the last closed tab in Firefox"""
        # Simulates the Ctrl+Shift+T keystroke
        actions.key("ctrl-w")   

    def open_url_with_firefox(url: str):
        """Opens a specified URL with Firefox using nircmd"""
        # Corrected the command by ensuring proper space before -new-tab
        cmd = f'nircmd execmd "C:\\Program Files\\Mozilla Firefox\\firefox.exe" -new-tab {url}'
        print(f"Executing: {cmd}")  # Debugging print
        os.system(cmd)

    # Open folder with path name
    def open_folder_by_name(folder_name: str):
        """Opens a folder specified by its name."""
        if folder_name in folders:
            folder_path = folders[folder_name]
            subprocess.Popen(['explorer', folder_path])
        else:
            app.notify(f"Folder '{folder_name}' not found.")


    def focus_or_launch_app(app_name: str, app_key: str):
        """Attempts to focus on an application window; launches it if not found"""
        cmd_focus = f'nircmd win activate ititle "{app_name}"'
        os.system(cmd_focus)

        if app_key in app_paths:
            try:
                # Set up the startup info to suppress the command window
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE

                # Launch the application without showing a command window
                subprocess.Popen([app_paths[app_key]], startupinfo=startupinfo)
            except Exception as e:
                app.notify(f"Failed to launch '{app_key}': {str(e)}")
        else:
            app.notify(f"Executable path for '{app_key}' not defined.")

    # Aimset server start
    def open_cloud_sql_and_run_batch():
        """Opens cloud_sql_proxy_x64.exe and runs start_proxy_and_psql-windows.bat in the specified directory"""
        directory_path = r"C:\\Users\\Emmanuel\\Documents\\GitHub\\aimset-main-site-with-admin"
        exe_path = os.path.join(directory_path, "cloud_sql_proxy_x64.exe")
        batch_path = os.path.join(directory_path, "start_proxy_and_psql-windows.bat")
        
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            app.notify("Directory does not exist.")
            return

        try:
            subprocess.Popen([exe_path], cwd=directory_path, creationflags=subprocess.CREATE_NO_WINDOW)
            subprocess.Popen([batch_path], cwd=directory_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as e:
            app.notify(f"Failed to execute commands: {str(e)}")

            
    # Aimset local start
    def open_git_bash_and_run_npm_dev():
        """Opens Git Bash in a specific directory and runs 'npm run dev'"""
        directory_path = r"C:\\Users\\Emmanuel\Documents\\GitHub\\aimset-main-site-with-admin"
        git_bash_path = app_paths["gitbash"]  # Assuming you've added the path to the app_paths dictionary
        
        # Command to run in Git Bash
        command = f'--cd="{directory_path}" -c "npm run dev"'
        
        try:
            subprocess.Popen([git_bash_path, command], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            app.notify(f"Failed to run 'npm run dev': {str(e)}")
