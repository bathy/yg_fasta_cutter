import re
import itertools
reg_ex='([KR](?=[^P]))|((?<=W)K(?=P))|((?<=M)R(?=P))'

cut_sequence=re.finditer(reg_ex,'MASFLAVVGAPGGVNSCVFDRFHYSVKMGDRSVYNENTSVVVSVQRAFVHPKFSTVTTIRNDLALLQLQHPVNFTSNIQPICIPQENFQVEGRFWGPLGL')
cleavagePosList = set(itertools.chain(map(lambda x: x.end(), cut_sequence)))

print cleavagePosList