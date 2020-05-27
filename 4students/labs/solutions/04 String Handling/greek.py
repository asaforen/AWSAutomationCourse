

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lamda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Final Sigma','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']
         
#Format required:
#    The hex value of the character
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character

pos = 0x03B1         
for v in greek:
    char = chr(pos)
    #print(v,":",char,char.upper())
    print("{:#x} - {:#^15}{} {}".format(pos, v ,char, char.upper()))
    pos += 1

