import sys
import subprocess
import importlib.metadata

def check_and_install_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        required_packages = file.readlines()

    installed_packages = {dist.metadata['Name'].lower(): dist.version for dist in importlib.metadata.distributions()}

    missing_packages = []
    for package in required_packages:
        package = package.strip()
        if package and not package.startswith("#"):
            package_name = package.split('==')[0].lower()
            if package_name not in installed_packages:
                missing_packages.append(package)

    if missing_packages:
        print("Missing packages:")
        for pkg in missing_packages:
            print(pkg)
        do_installation = input('Do you want to install missing modules? [Y/n] ').upper()
        if do_installation == 'Y':
            print("Installing missing packages...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
        elif do_installation == 'N':
            print('Cancelling...')
            exit(1)
        else:
            print('Invalid input...')
            exit(2)
    else:
        print("All packages are installed.")

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    check_and_install_requirements(requirements_file)
