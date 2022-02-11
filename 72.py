import re
mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiiii'''

# findall,search,split,sub,finditer
# patt=re.compile(r'fass')
# patt=re.compile(r'.')
# patt=re.compile(r'.adm')
# patt=re.compile(r'^Tata')
# patt=re.compile(r'Tata$')
# patt=re.compile(r'iin$')
# patt=re.compile(r'ai*')
# patt=re.compile(r'a*i*')
# patt=re.compile(r'ai+')
# patt=re.compile(r'ai{2}')
# patt=re.compile(r'(ai){2}')
# patt=re.compile(r'ai{1}|t')
# patt=re.compile(r'ai{1}|Fax')

#special sequences
# patt=re.compile(r'\ATata')
# patt=re.compile(r'\AFax')
# patt=re.compile(r'\bFax')
# patt=re.compile(r'Fax\b')
# patt=re.compile(r'27\b')
# patt=re.compile(r'\d{5}-\d{4}')
# task
# given a string with a lot of indian phone nos. starting from +91
# matches=patt.finditer(mystr)
# for match in matches:
#     print(match)
    # print(mystr[448:452])
# print(r"\n")

mystr="some string +911234567890 some more string +910987654321 some more +915678904321"
patt=re.compile(r'[+]91\d{10}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)