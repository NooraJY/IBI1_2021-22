def find_percentage(i):
    a = i.upper()
    b = DNA.upper()
    #Change all letters in the DNA and in the basic group into uppercases.
    number_of_times = b.count(a)
    #Find the number of times that the nucleotide have appeared in the DNA sequence.
    total = len(b)
    #calculate the length of the DNA sequence
    percentage = number_of_times/total
    #calculate the percentage
    return percentage


DNA = input("The DNA sequence is:")
nucleotide = input("Please imput a nucleotide from A/T/C/G nucleotides:")  
print("The percentage of this nucleotide in the DNA sequence is:",find_percentage(nucleotide))
#Apply the find_percentage function.

