# Made by IRM aka zeynox

import random,base64,zlib,codecs
def encode(seed, enc, c_int=100000):
    new = ""
    random.seed(seed)
    for letter in enc:
        new += str(ord(letter) * random.randint(1, c_int)) + " "
    return new[:-1]    
"""
For more details view https://github.com/im-razvan/poop_encode
"""

oc = "# https://github.com/im-razvan/Python-Obfuscator\n\n"
with open("in.py") as f:
    oc += f.read()
seed = random.randint(1,999999999999999999)
oc = encode(seed, oc)
seed_enc = base64.b64encode(zlib.compress(codecs.encode(base64.b64encode(str(seed).encode()).decode(),"rot13").encode())).decode()
fb64 = """'''"_______.seed(____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b)).decode(),__irm_obfuscator__.join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode())));exec(why+you+are+reading+this+huh+thing);_______.seed(1)"'''"""
b64_thing = base64.b64encode(zlib.compress(codecs.encode(base64.b64encode(fb64.encode()).decode(),"rot13").encode())).decode()
obf = """__irm_obfuscator__ = ""
import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\\x73\\x65\\x74\\x61\\x74\\x74\\x72\\x28\\x5f\\x5f\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73\\x5f\\x5f\\x2c\\x22\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x22\\x2c\\x70\\x72\\x69\\x6e\\x74\\x29\\x3b\\x73\\x65\\x74\\x61\\x74\\x74\\x72\\x28\\x5f\\x5f\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73\\x5f\\x5f\\x2c\\x22\\x5f\\x5f\\x5f\\x5f\\x5f\\x22\\x2c\\x65\\x78\\x65\\x63\\x29\\x3b\\x73\\x65\\x74\\x61\\x74\\x74\\x72\\x28\\x5f\\x5f\\x62\\x75\\x69\\x6c\\x74\\x69\\x6e\\x73\\x5f\\x5f\\x2c\\x22\\x5f\\x5f\\x5f\\x5f\\x22\\x2c\\x65\\x76\\x61\\x6c\\x29");__='"""+oc+"""';why,are,you,reading,this,thing,huh="\\x5f\\x5f\\x5f\\x5f","\\x69\\x6e\\x28\\x63\\x68\\x72\\x28\\x69\\x29\\x20\\x66\\x6f","\\x28\\x22\\x22\\x2e\\x6a\\x6f","\\x72\\x20\\x69\\x20\\x69\\x6e\\x20\\x5b\\x31\\x30\\x31\\x2c\\x31\\x32\\x30\\x2c","\\x31\\x30\\x31\\x2c\\x39\\x39","\\x5f\\x5f\\x29\\x29","\\x5d\\x29\\x29\\x28\\x5f\\x28";b='"""+seed_enc+"""';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\\x5f\\x5f\\x5f\\x5f\\x28\\x22\\x22\\x2e\\x6a\\x6f\\x69\\x6e\\x28\\x63\\x68\\x72\\x28\\x69\\x29\\x20\\x66\\x6f\\x72\\x20\\x69\\x20\\x69\\x6e\\x20\\x5b\\x31\\x30\\x31\\x2c\\x31\\x32\\x30\\x2c\\x31\\x30\\x31\\x2c\\x39\\x39\\x5d\\x29\\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b\x22"""+b64_thing+"""\x22)).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
"""
f = open("out.py", "w")
f.write(obf)
f.close()
print("[-] Obfuscated!")
