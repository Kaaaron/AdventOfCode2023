########################################
######### Day 1, Challenge 1 ###########
########################################

def getNumOnlyLineSum(line: str) -> int:
	firstDigit: str = ""
	lastDigit: str = ""

	for char in line:
		if char.isnumeric():
			firstDigit = char
			break

	for char in line[::-1]:
		if char.isnumeric():
			lastDigit = char
			break

	return int(firstDigit + lastDigit)


with open("Input.txt") as file:
	outputSum = 0
	for currentLine in file:
		outputSum = outputSum + getNumOnlyLineSum(currentLine)

	print(outputSum)  # the final result

########################################
######### Day 1, Challenge 2 ###########
########################################

writtenNumbers = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"


def getStringAndNumLineSum(line: str) -> int:
	firstDigit: str = ""
	firstDigitIdx: int = -1
	lastDigit: str = ""
	lastDigitIdx: int = -1

	for idx, char in enumerate(line):
		if char.isnumeric():
			firstDigit = char
			firstDigitIdx = idx
			break

	for idx, char in enumerate(line[::-1]):
		if char.isnumeric():
			lastDigit = char
			lastDigitIdx = len(line) - idx - 1
			break

	for num in writtenNumbers:
		foundIdx = line.lower().find(num)
		if foundIdx != -1:
			if foundIdx < firstDigitIdx or firstDigitIdx == -1:
				firstDigit = str(writtenNumbers.index(num) + 1)
				firstDigitIdx = foundIdx

		rfoundIdx = line.lower().rfind(num)
		if rfoundIdx != -1:
			if rfoundIdx > lastDigitIdx or lastDigitIdx == -1:
				lastDigit = str(writtenNumbers.index(num) + 1)
				lastDigitIdx = rfoundIdx

	return int(firstDigit + lastDigit)


with open("Input.txt") as file:
	outputSum = 0

	for currentLine in file:
		outputSum = outputSum + getStringAndNumLineSum(currentLine)

	print(outputSum)  # the final result
