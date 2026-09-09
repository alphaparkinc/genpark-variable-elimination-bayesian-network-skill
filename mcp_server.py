import sys
import json
from client import VariableEliminationInference

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "query":
        ve = VariableEliminationInference()
        table = {tuple(k.split(",")): v for k, v in params.get("table", {}).items()}
        return ve.query(params.get("vars", []), table, params.get("eliminate", []))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
