
########################################
######### Day 1, Challenge 1 ###########
########################################

def getLineSum(line: str) -> int:
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


with open("input.txt") as file:
	outputSum = 0
	for currentLine in file:
		outputSum = outputSum + getLineSum(currentLine)

	print(outputSum)  # the final result
