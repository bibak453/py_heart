#import argostranslate.package
#mport argostranslate.translate
import os
import subprocess
import sys
import crossfiledialog

# GLOBAL
cwd_directory = ""

def find_file(cmp):
    
    std_path = os.path.join(cwd_directory, cmp)
    
    if os.path.isfile(std_path):
        print("File was found in the script directory.", std_path)
        return std_path
    
    print("File not found in the script directory.")
    print("Opening file dialog...")
    
    file = crossfiledialog.open_file(title="Pick " + cmp, start_dir=cwd_directory)
    
    if os.path.isfile(file):
        if cmp.upper() in file or cmp.lower() in file:
            print("File found in:", file)
            return file

    return None

def get_directory():
    return os.path.dirname(os.path.realpath(__file__))

"""
def download_lang(from_code, to_code):
    argostranslate.package.update_package_index()
    
    available_packages = argostranslate.package.get_available_packages()
    
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
"""

"""
    extract_assets(path):

    This function will open the LVNS3DAT.PAK file
    and attempt to extract and convert all file formats
    and also put them into a specific directory.
    It will also checksum the final files for integrity.
"""

def extract_assets(path):
    print("Extracting assets from", path)

def extract_scn(path):
    print("Extracting scenario from", path)

def parse_scn():
    print("Parsing scenario to Renpy format...")

def translate(txt):
    #translated = argostranslate.translate.translate(txt, from_code, to_code)
    return txt

def main():
    global cwd_directory
    #download_lang("jp", "en")
    
    cwd_directory = get_directory()
    
    lvns3dat_path = find_file("lvns3dat.pak")
    lvns3scn_path = find_file("lvns3scn.pak")
    
    if lvns3dat_path is None or lvns3scn_path is None:
        print("One or more files were picked uncorrect.")
        print("Exiting...")
        exit()
    
    extract_assets(lvns3dat_path)
    extract_scn(lvns3scn_path)
    parse_scn()
    
if __name__ == "__main__":
    #TODO: Add parameter for enabling and dissabling the checksum process
    
    main()