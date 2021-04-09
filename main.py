import time
from tqdm import tqdm

for i in tqdm(range(3)):
    time.sleep(6)

with open('file.txt', 'w') as f:
    f.write('TESTFILE')

print('Work done')