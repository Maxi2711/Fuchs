def validate_id(id: int) -> bool:
    if len(str(id)) != 18:
        return False
    return True