def solveEquation():
    base = 667
    exp = 937
    modular = 2537
    binary = bin(exp)
    multiply = 1
    for digit in range(len(binary) - 1, 1, -1):
        possibleExpo = len(binary) - 1 - digit
        if binary[digit] == '1':
            targetExp = possibleExpo
            powerOfTwo = pow(2, targetExp)
            resultAfterMod = pow(base, powerOfTwo, modular)

            multiply *= resultAfterMod

    finalResult = multiply % modular

    return finalResult
def main():
    print(solveEquation())

main()