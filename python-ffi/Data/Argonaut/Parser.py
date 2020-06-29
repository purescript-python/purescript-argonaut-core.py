import json


def _jsonParser(fail, succ, s):
    try:
        return succ(json.loads(s))
    except Exception as e:
        return fail(str(e))
