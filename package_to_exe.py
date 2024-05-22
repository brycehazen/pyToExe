import os
import subprocess
import sys

def package_directory_to_exe():
    # Ensure PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Please install it manually using 'pip install pyinstaller'.")
        return

    # Get the current directory
    directory = os.getcwd()

    # Check if the CSV file exists
    csv_file = 'master_donor.csv'
    if not os.path.exists(csv_file):
        print(f"{csv_file} not found in the directory.")
        return

    # Ensure donor_search_gui.py exists
    main_script = 'donor_search_gui.py'
    if not os.path.exists(main_script):
        print(f"{main_script} not found in the directory.")
        return

    # Create PyInstaller command
    pyinstaller_command = [
        'pyinstaller',
        '--onefile',
        '--name', 'EricsDonorSearch',
        '--add-data', f'{csv_file};.',
        main_script
    ]

    # Run PyInstaller to create an executable
    subprocess.run(pyinstaller_command)

    print("Packaging complete. Check the 'dist' directory for the executable.")

if __name__ == "__main__":
    package_directory_to_exe()
