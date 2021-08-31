import collections

stats = collections.defaultdict(int)

stats["ccc"] = 2
stats["aaa"] = 10
stats["bbb"] = 5
stats["ddd"] = 0

# Sort defaultdict by keys.
print(sorted(stats.items(), key=lambda kv: kv[1], reverse=True))
