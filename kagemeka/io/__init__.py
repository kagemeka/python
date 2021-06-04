# data structure and algorithm



from ..gen import(
  Constant,
  Numeric,
)





import sys
from heapq import (
  heappush, 
  heappop, 
  heapify,
)
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import (
  deque, 
  Counter, 
  defaultdict,
)
import itertools 
import string 
import math 

from functools import (
  lru_cache, 
  reduce,
)
from dataclasses import (
  dataclass,
)
from typing import (
  Union, 
  List,
)
import typing

from scipy.sparse.csgraph import (
  shortest_path, csgraph_to_dense, maximum_flow, minimum_spanning_tree,
  connected_components
)

from scipy.sparse import (
  csr_matrix,
)

from scipy.spatial import (
  ConvexHull,
)

from scipy import optimize
from scipy.special import comb
from scipy.ndimage import (
  distance_transform_cdt,
)




'''Comment Tags
TODO (
  MILESTONE, MLSTN, DONE, 
  YAGNI, TBD, TOBEDONE) 
FIXME (
  XXX, DEBUG, BROKEN, REFACTOR,
  REFACT, RFCTR, OOPS, SMELL, 
  NEEDSWORK, INSPECT)
BUG (BUGFIX)
NOBUG (
  NOFIX, WONTFIX, DONTFIX,
  NEVERFIX, UNFIXABLE, CANTFIX)
REQ (REQUIREMENT, STORY)
RFE (FEETCH, NYI, FR, FTRQ, FTR)
IDEA 
??? (QUESTION, QUEST, QSTN, WTF)
!!! (ALERT)
HACK (CLEVER, MAGIC)
PORT (PORTABILITY, WKRD)
CAVEAT (CAV, CAVT, WARNING, CAUTION)
NOTE (HELP)
FAQ 
GLOSS (GLOSSARY)
SEE (REF, REFERENCE)
TODOC (
  DOCDO, DODOC, NEEDSDOC, 
  EXPLAIN, DOCUMENT)
CRED (CREDIT, THANKS)
STAT (STATUS)
RVD (REVIEWED, REVIEW)
'''