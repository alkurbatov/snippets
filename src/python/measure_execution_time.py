import datetime
import time

import humanize

started_at = time.perf_counter()

time.sleep(5)

elapsed = datetime.timedelta(seconds=(time.perf_counter() - started_at))
print(humanize.precisedelta(elapsed))
