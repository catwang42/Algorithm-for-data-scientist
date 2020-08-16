#EMAIL Mapping 

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails= ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
email_map =set()
for i in emails:
    import re
    host, domain = i.split("@")
    host = re.sub(r'\.','',host)
    host = host.split("+",1)[0]
    email_map.add(host+'@'+domain)

#Licese key formatting 
"""
S = "w95F3Z-2e-9-w", K = 4
 "W9-5F3Z-2E9W"
"""
def licenseKeyFormatting(S: str, K: int) -> str:
    clean_s = S.replace('-','').upper()[::-1]
    plate_list = [clean_s[i:i+K] for i in range(0,len(clean_s),K)]
    result = '-'.join(plate_list)
    return result[::-1]
