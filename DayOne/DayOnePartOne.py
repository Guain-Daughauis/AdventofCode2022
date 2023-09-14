'''
    Copyright (C) 2023 Guain-Daughauis

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
'''

# Read the input file into a list of elves
with open("in.txt", "r", encoding="utf8") as f:
    elves = f.read().split("\n\n")

# Initialize variables
max_calories = 0
fat_elf = 0

# Iterate through the elves
for index, elf in enumerate(elves, start=1):
    print(f"Checking Elf Nº {index}'s bag")
    calories = [int(calory) for calory in elf.splitlines()]
    total_calories = sum(calories)
    print(f"In total, Elf Nº {index} is carrying {total_calories} calories")
    
    if total_calories > max_calories:
        print(f"Elf Nº {index} was carrying more than {max_calories} calories and now is the fattest elf.")
        max_calories = total_calories
        fat_elf = index

print(f"The fattest elf is Elf Nº {fat_elf}, he's carrying {max_calories} calories")