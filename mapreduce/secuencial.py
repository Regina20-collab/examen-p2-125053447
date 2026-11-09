#!/usr/bin/env python3
import sys, time
t0 = time.time()
t = {}
with open(sys.argv[1]) as f:
    next(f)
    for line in f:
        p = line.strip().split(",")
        if len(p) != 8:
            continue
        try:
            t[p[4]] = t.get(p[4], 0.0) + int(p[5]) * float(p[6])
        except ValueError:
            continue
for k, v in sorted(t.items(), key=lambda x: -x[1])[:10]:
    print(f"{k}\t{v:.2f}")
print(f"TIEMPO: {time.time()-t0:.2f}s", file=sys.stderr)
