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
print("When the DNA sequence is ",DNA,",the percentage of",nucleotide," in the DNA sequence is:",find_percentage(nucleotide,DNA))
#Apply the find_percentage function.

#example
DNA1= 'ACGTatcgtATAGcta'
nucleotide1 = 'T'
print("When the DNA sequence is ",DNA1,"the percentage of",nucleotide1," in the DNA sequence is:",find_percentage(nucleotide1,DNA1))
