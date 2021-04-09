import time
from tqdm import tqdm

for i in tqdm(range(10*60)):
    time.sleep(1)

with open('file.txt', 'w') as f:
    f.write('5 minutes expe')

print('Work done')
