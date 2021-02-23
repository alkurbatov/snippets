import os
import pydevd

pydevd.settrace('172.16.45.157', port=9090, stdoutToServer=True, stderrToServer=True, suspend=False)
print('Hello world!')
