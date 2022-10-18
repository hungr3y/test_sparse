import json

# read presets from git-tracked .json
with open("asset_presets.json", "r") as file:
    list_pattern = json.load(file)
list_pattern_keys = sorted(list_pattern.keys())

# print list of present
print("\nChoose presets to work with:\n")
for count, value in enumerate(list_pattern_keys, 1):
    print(f"{count}. {value}------->{list_pattern[value]}")

# input of values and their validation
while True:
    print("\nEnter the numbers of the required presets ( \'0\' to exit):")
    choice = list(input().split())

    if len(choice) == 1 and (choice[0]) == '0':  # 'zero' to exit logic
        exit(0)

    was_invalid_values = False

    for i in choice:
        try:
            int(i)
        except ValueError:
            print(f"\nValue must be integer. \"{i}\" - is not integer, try again")
            was_invalid_values = True

        if was_invalid_values is False:
            if int(i) > len(list_pattern_keys):
                print(f"\n{i} - value is out of range, try again")
                was_invalid_values = True

    if was_invalid_values is False:
        break

result_dict = {}

# write the selected keys to the list
for i in choice:
    print(list_pattern_keys[int(i) - 1])
    result_dict[list_pattern_keys[int(i) - 1]] = list_pattern[list_pattern_keys[int(i) - 1]]

print("was added to my_asset_list")  # output
with open("my_asset_list.json", "w") as file:
    json.dump(result_dict, file, indent=3)
    exit(0)
