# File: initials.py
# Description: Print out my initials in stylized large letters.
# Assignment Number: 2
#
# Name: Gabriel Edem Kumadey
# STUDENT ID:  2425402908
# Email: 2425402908@live.gctu.edu.gh
# Grader: Sir Augustus
#
# On my honor, Gabriel Edem Kumadey, this programming assignment is my own work
# and I have not provided this code to any other student.



def main():
    # This function prints the initials G E K horizontally in small and large stylized format
    # Each large letter is 12 chars wide, 10 chars high, made of the letter itself
    # Each large period is 4 asterisks
    # Output is 10 lines high, 60 chars wide total

    # Small initials line (with three periods on each side)
    print()
    print("..." + "GEK" + "...")
    print()

    # Large letters printed horizontally - each line exactly 60 characters
    # Line 1
    print("...GGGGGGGGGGGG........EEEEEEEEEEEE........KK........KK.....")
    # Line 2
    print("...GGGGGGGGGGGG........EEEEEEEEEEEE........KK......KK.......")
    # Line 3
    print("...GG..................EE..................KK....KK.........")
    # Line 4
    print("...GG..................EE..................KK..KK...........")
    # Line 5
    print("...GG...GGGGGG.........EEEEEEEEEEEE........KKKK.............")
    # Line 6
    print("...GG...GGGGGG.........EEEEEEEEEEEE........KKKK.............")
    # Line 7
    print("...GG...GG..GG.........EE..................KK..KK...........")
    # Line 8
    print("...GG...GG..GG.........EE..................KK....KK.........")
    # Line 9
    print("...GGGGGGGGGGGG...**...EEEEEEEEEEEE...**...KK......KK.....**")
    # Line 10
    print("...GGGGGGGGGGGG...**...EEEEEEEEEEEE...**...KK........KK...**")

    print()

main()
