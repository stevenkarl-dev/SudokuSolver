def main():
    infile = open(r'C:\Users\fx075e\Desktop\lines.txt')
    outfile = open(r'C:\Users\fx075e\Desktop\lines_copy.txt', 'wt')

    for line in infile:
        print(line.rstrip(), file = outfile)
        print('.', end='')

    outfile.close()
    print('\ndone.')



if __name__ == '__main__':
    main()
