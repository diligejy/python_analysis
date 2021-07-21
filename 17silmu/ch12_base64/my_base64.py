from bitstring import BitArray
import re


def open_json_file(filename):
    with open(filename, mode='rb') as file:
        return file.read()


data = open_json_file('../ch08_json/message1.json')
bit_str = BitArray(data).bin  # 비트 코드를 문자열로 변환

print(bit_str)

pad_count = 0
while len(bit_str) % 24 != 0:
    bit_str += '00000000'
    pad_count += 1

b64_str = ''
b64_chs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+"

bit_list = re.findall(r'(\d{6})', bit_str)
if pad_count > 0:
    # 마지막에 추가된 0은 'A'가 아니라 '='여야 합니다.
    # 그래서 여기서 제외된 후 나중에 다시 추가합니다.
    bit_list = bit_list[:-pad_count]

for bit in bit_list:
    v = int(bit, 2)
    b64_str += b64_chs[v]

b64_str += ('=' * pad_count)
print('my_base64={0}'.format(b64_str))
