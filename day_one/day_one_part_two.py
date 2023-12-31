# Copyright (C) 2023 Guain-Daughauis <guain_daughauis@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Read the input file into a list of elves
with open(file="in.txt", mode="r", encoding="utf8") as f:
    elves: list[str] = f.read().split("\n\n")

# Calculate the total calories for each elf and sort them in descending order
elf_calories: list[int] = [sum(map(int, elf.splitlines())) for elf in elves]
elf_calories.sort(reverse=True)

# Calculate the sum of the top three fattest elves
total_calories: int = sum(elf_calories[:3])

print(total_calories)