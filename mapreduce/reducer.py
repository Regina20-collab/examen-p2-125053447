#!/usr/bin/env python3
import sys
t = {}
for line in sys.stdin:
    try:
        k, v = line.strip().split("\t")
        t[k] = t.get(k, 0.0) + float(v)
    except ValueError:
        continue
for k, v in sorted(t.items(), key=lambda x: -x[1])[:10]:
    print(f"{k}\t{v:.2f}")
