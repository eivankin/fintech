from sha3 import keccak_256
from itertools import product
import json

variables = ['uint256', 'bool', 'bytes32', 'address']
variants = input().split()
contract = json.loads(input())
for action in contract['logs']:
    r = len(action['data'][2:]) // 64
    for variant in variants:
        for v in product(variables, repeat=r):
            s = variant + f'({",".join(v)})'
            if keccak_256(s.encode()).hexdigest() == action['topics'][0][2:]:
                print(f'event {variant}({", ".join(v)})')
