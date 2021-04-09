import time
from tqdm import tqdm

for i in tqdm(range(2*60)):
    time.sleep(1)

with open('file.txt', 'w') as f:
    f.write('2 minutes expe')

print('Work done')
