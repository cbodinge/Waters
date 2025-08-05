def to_str(val: any) -> str:
    try:
        return str(val)
    except (ValueError, TypeError):
        return ''


def to_float(val: any) -> float:
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0


def to_int(val: any) -> int:
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0
