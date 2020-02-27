
#Author:    Aya Tamer Nabil
#Created:   26.02.2020

# The given ciphers in the assignment document
c1 = "AEDE0273C4C0DA3477F919018A05DA71A2530F5A0020E4E0ACA80FF2DE"
c2 = "A8C80426C2DEC16D31F90D1497129475A45447561D74EEF1B8BF0FFCDC"
c3 = "A9D30426D3C7CB202EB8050E9717C734A5484A13126CE0FDABA212FBDF"
c4 = "B49B166FDAC58E2A25F90A159914D134B84E0F551677A7FFB6A512FBC1"
c5 = "B49B126ED7C5C26D20EA07149D40C771B2555D565373E8F4ADBC07E1D7"
c6 = "B3DE1763C489DC2822EB0B40970ED134A54942565370E6F6F9A003EAC1"

ciphers = [c1, c2, c3, c4, c5, c6]

target_ciphers = [c1, c2, c3, c4, c5, c6]


broken_positions = []

final_key = [None for i in range(58)]


for main_idx, ciphertext in enumerate(ciphers):

    spaces_counter = {}

    for sub_idx, ciphertext2 in enumerate(ciphers):
        if main_idx != sub_idx: 
            for char_idx, char in enumerate(strxor(bytearray.fromhex(ciphertext).decode('latin-1'), bytearray.fromhex(ciphertext2).decode('latin-1'))): # Xor the two ciphertexts
               
                if char in string.ascii_letters or char in string.digits:
                    if spaces_counter.get(char_idx):
                        spaces_counter[char_idx] += 1 
                    else:
                        spaces_counter[char_idx]=1
    found_spaces = []
    
    #if a certain position outputed a space more than four times, then the space was probably included in the first cipher
    
    for ind, k in spaces_counter.items():
        if k >= 4:
            found_spaces.append(ind)

    ciphertext_xor_space = strxor(bytearray.fromhex(ciphertext).decode("latin-1"),''.join([" " for i in range(58)]))
    
    for index in found_spaces:
        
        final_key[index] = ciphertext_xor_space[index].encode('latin-1').hex()
        
        broken_positions.append(index)

partial_key_hex = ''.join([val if val is not None else '00' for val in final_key])

print("Now we use the partial key to try and guess one of the cipher texts")
print("====================================================================")
print("\n")

for elm in target_ciphers:
    
    output = strxor(bytearray.fromhex(elm).decode("latin-1"),bytearray.fromhex(partial_key_hex).decode("latin-1"))
    print( "".join([char if index in broken_positions else '+' for index, char in enumerate(output)]))


infered_text = "I will graduate in few months"

print("\n")
print("Now we use the infered text to retrieve the key")
print("====================================================================")
print("\n")

key = strxor(bytearray.fromhex(target_cipher).decode('latin-1'),infered_text)

print("the key is :",key)
print("\n")

print("Finally we retrieve all the ciphers by using the key:")
print("====================================================================")
print("\n")
for cipher in ciphers:
    print (strxor(bytearray.fromhex(cipher).decode('latin-1'),key))