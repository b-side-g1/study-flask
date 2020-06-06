import uuid


def getUniqueId():
    return uuid.uuid4().hex[:20].upper()
