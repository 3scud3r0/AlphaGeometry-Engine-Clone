"""Differential result comparison; runs must refer to identical formal problems."""
def differences(reference,candidate):
    keys=set(reference)|set(candidate)
    return {key:{"reference":reference.get(key),"candidate":candidate.get(key)}
            for key in sorted(keys) if reference.get(key)!=candidate.get(key)}
