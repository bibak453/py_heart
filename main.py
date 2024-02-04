import argostranslate.package
import argostranslate.translate
import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("argostranslate")

def get_directory():
    return ""
    
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

def translate(txt, verbose = False):
    translated = argostranslate.translate.translate(txt, from_code, to_code)
    if verbose:
        print(txt, " ==>", translated)
    return translated

def main():
    download_lang("jp", "en")
    
    cwd_directory = get_directory()
    lvns3dat_path = os.path.join(cwd_directory, "lvns3dat.pak")
    lvns3scn_path = os.path.join(cwd_directory, "lvns3scn.pak")
    
    extract_assets(lvns3dat_path)
    extract_scn(lvns3scn_path)
    parse_scn()
    
if __name__ == "__main__":
    #TODO: Add parameter for enabling and dissabling the checksum process
    
    main()