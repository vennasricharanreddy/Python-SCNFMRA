def validate_capacity(cap):
    if cap <= 0:
        raise ValueError("Capacity must be positive")