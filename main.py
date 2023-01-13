from code.visualisation import gameboard 

parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("input", help = "input file (csv)")

# Read arguments from command line
args = parser.parse_args()

# Run main with provide arguments
puzzle = gameboard(args.input)

plt.imshow(puzzle)
plt.show()
