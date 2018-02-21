
def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt", "a")

    # Read the file contents
    f = open("textfile.txt", "r")

    # Write some lines of data to the file
    # for i in range(10):
    #     f.write("This is line " + str(i) + "\n")

    # Close the file when done
    # f.close()

    # Open the file back up and read the contents
    if f.mode == "r":
        # contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)

main()  