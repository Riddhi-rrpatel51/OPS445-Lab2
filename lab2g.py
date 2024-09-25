#!/usr/bin/env python3
# Author: Riddhi Ritesh Patel
# Author ID: rrpatel51@myseneca.ca
# Date Created: 2024/09/24

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3  # Default value if no argument is provided

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')

