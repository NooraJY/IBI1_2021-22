seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
import re

marked_seq = re.sub(r'GAATTC','G^AATTC',seq)
#mark the cutting site
cut = marked_seq.split('^')
#cut all the marked cutting site
print(cut)
print("The total number of feagments is:",len(cut))
