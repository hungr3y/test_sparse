import subprocess
import json

with open("my_asset_list.json", "r") as file:
    selected_assets = json.load(file)

selected_assets_str = ""

for i in selected_assets.keys():
    selected_assets_str += str(f"{i} ")


def set_chosen_assets() -> str:
    result = subprocess.run(f"git sparse-checkout set {selected_assets_str}",
                            capture_output=True,
                            shell=True)
    return result.stdout.decode().strip()


set_chosen_assets()

'''

import subprocess

selected_assets_str = 'test_folder2 test_folder4 '

def set_chousen_assets() -> str:
    result = subprocess.run(f'git sparse-checkout set {selected_assets_str},',
                                   capture_output=True,
                                   shell=True)
    return result.stdout.decode().strip()

set_chousen_assets()
'''
