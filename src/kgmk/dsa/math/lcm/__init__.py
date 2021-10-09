from kgmk.dsa.math.gcd.recursive import gcd
# TODO cut below


def lcm(a: int, b: int) -> int: return a // gcd(a, b) * b