# get file object reference to the file
file = open('rosalind_dna.txt')

# read content of file to string
DNA = file.read()

#get number of occurrences of the substring in the string
occurrences1 = DNA.count("A")
occurrences2 = DNA.count("T")
occurrences3 = DNA.count("G")
occurrences4 = DNA.count("C")

print('A', occurrences1, 'T', occurrences2, 'G', occurrences3, 'C', occurrences4)

# without file and only a string of data
data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

count1 = data.count('A')
count2 = data.count('T')
count3 = data.count('G')
count4 = data.count('C')

print('A', count1, 'T', count2, 'G', count3, 'C', count4)
