class IdentifiedObject:

    @property
    def oid(self):
        return self._oid

    def __init__(self, oid):
        self._oid = oid

    def __eq__(self, oid):
        """SPEC: two IdentifiedObjects are equal if they have the same type and the same oid"""
        return self._oid == oid

    def __hash__(self):
        """SPEC: return hash code based on object's oid"""
        return hash(self._oid)
