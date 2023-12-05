########################################
######### Day 2, Challenge 1 ###########
########################################

# Just for the fun of it: lets try a more object oriented approach here!
from typing import List

numRedCubes = 12
numGreenCubes = 13
numBlueCubes = 14


class bag:
	def __init__(self, gameId: int):
		self.id = gameId

		self._redCubes: int = 0
		self._greenCubes: int = 0
		self._blueCubes: int = 0

		self.isPossible = True

	def set_blue(self, value: int):
		if self._blueCubes < value:
			self._blueCubes = value
			self.isPossible = self._contains_possible_game()

	def set_green(self, value: int):
		if self._greenCubes < value:
			self._greenCubes = value
			self.isPossible = self._contains_possible_game()

	def set_red(self, value: int):
		if self._redCubes < value:
			self._redCubes = value
			self.isPossible = self._contains_possible_game()

	def _contains_possible_game(self) -> bool:
		return not (self._redCubes > numRedCubes or self._greenCubes > numGreenCubes or self._blueCubes > numBlueCubes)


with open("Input.txt") as file:
	bags: List[bag] = []
	for idx, line in enumerate(file):
		bags.append(bag(idx + 1))

		sanitizedLine: str = line
		sanitizedLine = sanitizedLine.replace(" ", "")
		sanitizedLine = sanitizedLine[sanitizedLine.find(":") + 1:]
		sanitizedLine = sanitizedLine.replace(";", ",")
		sanitizedLine = sanitizedLine.replace("\n", "")
		cubeSets = sanitizedLine.split(",")
		for cubeSet in cubeSets:
			firstLetterIdx: int = max(cubeSet.find("red"), cubeSet.find("green"), cubeSet.find("blue"))
			color = cubeSet[firstLetterIdx:]
			if color == "red":
				bags[idx].set_red(int(cubeSet[:firstLetterIdx]))
			elif color == "green":
				bags[idx].set_green(int(cubeSet[:firstLetterIdx]))
			elif color == "blue":
				bags[idx].set_blue(int(cubeSet[:firstLetterIdx]))

	gameIdSum: int = 0
	for bag in bags:
		if bag.isPossible:
			gameIdSum = gameIdSum + bag.id

	print(gameIdSum)
