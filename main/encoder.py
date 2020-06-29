import numpy as np    
import zlib


dtype = A.dtype

B = zlib.compress(A, 1)
C = np.fromstring(zlib.decompress(B), dtype)
