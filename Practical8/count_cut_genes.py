import re
filename = input('Please type a filename:')
file = open("%s.fa"%filename,"x")
#Create a file to store the results. Ask the user to input a filename.

desired_genes = open(r'cut_genes.fa','r')
seq={}
for line in desired_genes:
    if line.startswith('>'):
        gene_name = line.split()[0]
        seq[gene_name]=''
#Find the gene names.
    else:
        seq[gene_name]+=line
desired_genes.close()
#Create a 'seq' dictionary to store the gene name and the DNA sequence.
 
for i in seq.keys():
    file.write(i)
    file.write('        ')
#Print the gene name
    pieces = len(re.findall(r'GAATTC',seq[i]))+1
#Calculate the number of fragments. You can divide a piece into two pieces by cutting it once. Make two cuts to divide into three sections. And so the number of fragments is equal to the number of cuts plus one.
    file.write(str(pieces))
#Change the type of 'pieces' from int to str and then print them.
    file.write('\n')
    file.write(seq[i])
    file.write('\n')
#Print the DNA sequence
file.close()

