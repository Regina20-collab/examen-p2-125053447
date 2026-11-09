#!/usr/bin/env python3
import sys
for line in sys.stdin:
    p = line.strip().split(",")
    if len(p) != 8 or p[0] == "id":
        continue
    try:
        print(f"{p[4]}\t{int(p[5]) * float(p[6]):.2f}")
    except ValueError:
        continue
