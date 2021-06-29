#!/usr/bin/python3
import os, sys

#initialize alphanumeric mappings
abc = list(map(str, [chr(i) for i in range(ord('A'), ord('Z') + 1)] + list(range(0, 10)) + [' ']))
pos_to_abc = dict(enumerate(abc))
abc_to_pos = {v: k for k, v in pos_to_abc.items()}

#default value is random so that out-of-dictionary characters won't mess up the randomness
#decrypt
def mod_add(text, key):
	return pos_to_abc.get((abc_to_pos.get(text, int.from_bytes(os.urandom(1),'little') % 36) + abc_to_pos.get(key)) % len(pos_to_abc))

#encrypt
def mod_sub(text, key):
	return pos_to_abc.get((abc_to_pos.get(text, int.from_bytes(os.urandom(1),'little') % 36) - abc_to_pos.get(key)) % len(pos_to_abc))
	
usage = sys.argv[0] + ': gen|enc|dec (otp_lines_num otp_name)|(plaintext key)|(cryptotext key)'

try:
	pos2, pos3 = sys.argv[2], sys.argv[3]
	if 'gen' in sys.argv:
		with open(pos3, 'w') as otp:
			for i in range(int(pos2)):
				otp.write(''.join([pos_to_abc.get(i % (len(pos_to_abc) - 1)) for i in os.urandom(50)]) + '\n')
			print('Wrote ' + pos2 + ' random lines to ' + pos3)
	elif 'enc' in sys.argv:
		if len(pos3) < len(pos2):
			raise Exception('Key is shorter than input text!')
		#padding is added if lengths differ
		print(''.join([mod_sub(i, j) for (i, j) in zip(pos2.upper() + ' ' * abs(len(pos3) - len(pos2)), pos3.upper())]))
	elif 'dec' in sys.argv:
		print(''.join([mod_add(i, j) for (i, j) in zip(pos2.upper(), pos3.upper())]))
	else:
		print(usage)
		exit(1)
except Exception as e:
	if len(sys.argv) != 4:
		print(usage)
		exit(1)
	print(usage,'\n',e)
	exit(2)
