def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    al = len(a)
    bl = len(b)
    if al == bl:
        return True
    else:
        return False