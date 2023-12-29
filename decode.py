def decode(message_file): 
    file=open(message_file,"r")
    decode_dict=dict()
    nums=[]

    for line in file:
        num, word = line.split()
        nums.append(int(num))
        decode_dict[nums[-1]] = word

    nums.sort()

    i=0
    counter=1

    decoded_string=""

    while i<len(nums):
        decoded_string=decoded_string+decode_dict[nums[i]]+" "
        counter+=1
        i+=counter

    return decoded_string.strip()

print(decode("coding_qual_input.txt"))