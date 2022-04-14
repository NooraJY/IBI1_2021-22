import re
all_genes = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
desired_genes = open(r'cut_genes.fa','w')

seq={}
for line in all_genes:
	if line.startswith('>'):
#Check whether the string starts with '>'.
		gene_name = line.split()[0]
#Only find the gene names.
		seq[gene_name]=''
#Put the gene names in the 'seq' dictionary.
	else:
		seq[gene_name]+=line.replace('\n','')
#Replace the new line character with a space. Combine several lines of DNA sequence into one line and put it into the 'seq' dictionary too.
all_genes.close()


for i in seq.keys():
        if re.findall('GAATTC',seq[i]):
#Find the DNA sequences that contain 'GAATTC'.
                desired_genes.write(i)
                desired_genes.write('        ')
                desired_genes.write(str(len(seq[i])))
                desired_genes.write('\n')
#print the gene name and the length of the sequence
                desired_genes.write(seq[i])
                desired_genes.write('\n')
#print the DNA sequence
desired_genes.close()

