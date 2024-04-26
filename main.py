from colorama import Fore, Back, Style


def decimal_to_binary(n):
    return "{0:b}".format(int(n))


def binary_to_decimal(n):
    return int(n, 2)


def complement(s):
    d = {'0': '1', '1': '0'}
    e = ''.join(d[x] for x in s)
    length = len(e)
    s = bin(int(e, 2) + int("1", 2))
    s = s[2:]
    return s.zfill(length)


def shift_left(s):
    s = s[1:]
    s = s + "0"
    return s


def add_binary_with_carry(bin1, bin2):
    result = bin(int(bin1, 2) + int(bin2, 2))[2:]
    carry = '1' if len(result) > max(len(bin1), len(bin2)) else '0'
    if carry == "1":
        return result[1:]
    else:
        return result


def is_binary(num):
    return all(bit == '0' or bit == '1' for bit in num)


while True:
    print(Fore.LIGHTBLUE_EX + "Enter the decimal value of dividend : ", end="")
    q = int(input())
    # while True:
    #
    #     if q == 0:
    #         print(Fore.RED + f"{0} is a invalid dividend")
    #     else:
    #         break

    while True:
        print(Fore.LIGHTBLUE_EX + "Enter decimal value of divisor : ", end="")
        m = int(input())
        if m == 0:
            print(Fore.RED + f"{0} is a invalid divisor")
        else:
            break
    Q = decimal_to_binary(q)
    M = decimal_to_binary(m)

    if len(M) > len(Q):
        Q = Q.zfill(len(M) + 1)
    else:
        M = M.zfill(len(Q) + 1)


    a = "0"

    A = "0".zfill(len(Q) + 1)

    print(
        Fore.LIGHTWHITE_EX + Back.BLACK + "We're going to calculate " + Back.BLUE + Fore.LIGHTWHITE_EX + " Q % M " + Style.RESET_ALL)

    print("Binary Value Of Q" + Fore.GREEN + "(Divisor) :", Fore.GREEN + Q + Style.RESET_ALL)
    print("Binary Value Of M" + Fore.GREEN + "(Divisor) :", Fore.GREEN + M + Style.RESET_ALL)
    print("Binary Value Of A :", Fore.GREEN + A + Style.RESET_ALL)
    l = len(Q)
    count = l
    M = M.zfill(len(A))
    print(f"A: {A}, Q: {Q}")
    while count > 0:
        print(Fore.LIGHTYELLOW_EX + f"Step: {l - count + 1}" + Style.RESET_ALL)
        SHL_AQ = shift_left(A + Q)
        A = SHL_AQ[:len(A)]
        Q = SHL_AQ[len(A):]
        print(f"A: {A}, Q: {Q} <-- " + Fore.LIGHTCYAN_EX + "Left shift AQ" + Style.RESET_ALL)
        As = A[0]

        if As == "0":
            # A = bin(int(A, 2) + int(complement(M), 2))[2:]
            A = add_binary_with_carry(A, complement(M))
            print(f"A: {A}, Q: {Q} <-- " + Fore.MAGENTA + "As = 0" + Style.RESET_ALL + " ==> "
                  + Fore.RED + "A = A - M" + Style.RESET_ALL)

        else:
            # A = bin(int(A, 2) + int(M, 2))[2:]
            A = add_binary_with_carry(A, M)
            print(f"A: {A}, Q: {Q} <-- " + Fore.MAGENTA + "As = 1" + Style.RESET_ALL + " ==> "
                  + Fore.RED + "A = A + M" + Style.RESET_ALL)
        As = A[0]

        if As == "0":
            Q = Q[:-1] + '1'
            print(f"A: {A}, Q: {Q} <-- " + Fore.MAGENTA + "As = 0" + Style.RESET_ALL
                  + " ==> " + Fore.LIGHTGREEN_EX + "q0 = 1" + Style.RESET_ALL)
        else:
            Q = Q[:-1] + '0'
            print(f"A: {A}, Q: {Q} <-- " + Fore.MAGENTA + "As = 1" + Style.RESET_ALL
                  + " ==> " + Fore.LIGHTGREEN_EX + "q0 = 0" + Style.RESET_ALL)

        count = count - 1
        input()

    print(Fore.LIGHTYELLOW_EX + "Final Step: " + Fore.LIGHTGREEN_EX +
          "We Check sign bit of A, if " + Fore.MAGENTA + "As = 1" + Fore.LIGHTGREEN_EX +
          " we must calculate " + Fore.LIGHTRED_EX + "A = A + M" + Style.RESET_ALL)

    if A[0] == "1":
        print(Fore.MAGENTA + "As = 1" + Style.RESET_ALL
              + f" => A = A + M = {A} + {M} = {add_binary_with_carry(A, M)}, so A holds the remaining value")
        A = add_binary_with_carry(A, M)
    else:
        print(Fore.MAGENTA + "As = 0" + Style.RESET_ALL + " => A holds the remaining value")

    print("\n-------------------------------------------------------------------------------")
    print(
        "A holds the remaining witch is: " + Fore.LIGHTYELLOW_EX + A + Style.RESET_ALL + " It's " + Fore.LIGHTYELLOW_EX
        + "decimal" + Style.RESET_ALL + " equivalent is: " +
        Fore.LIGHTYELLOW_EX + f"{binary_to_decimal(A)}" + Style.RESET_ALL)
    print("Q holds the quotient witch is: " + Fore.LIGHTYELLOW_EX + Q + Style.RESET_ALL + " It's " + Fore.LIGHTYELLOW_EX
          + "decimal" + Style.RESET_ALL + " equivalent is: " +
          Fore.LIGHTYELLOW_EX + f"{binary_to_decimal(Q)}" + Style.RESET_ALL)
    print("-------------------------------------------------------------------------------")
    input()
    end_program = False

    while True:
        phase1a = input("Do you want to continue? " + Fore.LIGHTBLUE_EX + "y/n" + Style.RESET_ALL)
        if phase1a.upper() == "Y":
            break
        elif phase1a.upper() == "N":
            end_program = True
            break

    print("\n\n")
    if end_program:
        break
