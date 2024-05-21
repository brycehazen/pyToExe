import os
import subprocess

def package_directory_to_exe():
    # Ensure PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Get the current directory
    directory = os.getcwd()

    # Collect all Python files in the directory, excluding this script
    current_script = os.path.basename(__file__)
    py_files = [f for f in os.listdir(directory) if f.endswith('.py') and f != current_script]
    
    if not py_files:
        print("No Python files found in the directory.")
        return

    # Create a temporary main script that imports all the files
    main_script_path = os.path.join(directory, 'main_script.py')
    with open(main_script_path, 'w') as main_script:
        for py_file in py_files:
            module_name = os.path.splitext(py_file)[0]
            main_script.write(f"import {module_name}\n")

    # Run PyInstaller to create an executable
    subprocess.run([
        'pyinstaller',
        '--onefile',
        main_script_path
    ])

    # Clean up temporary main script
    os.remove(main_script_path)

    print("Packaging complete. Check the 'dist' directory for the executable.")

if __name__ == "__main__":
    package_directory_to_exe()
