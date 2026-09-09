from client import VariableEliminationInference

def main():
    print("=== Variable Elimination Bayesian Network Inference ===")
    ve = VariableEliminationInference()
    factor_vars = ["Cloudy", "Rain", "WetGrass"]
    # Joint distribution mock
    table = {
        (True, True, True): 0.144,
        (True, True, False): 0.016,
        (True, False, True): 0.016,
        (True, False, False): 0.024,
        (False, True, True): 0.054,
        (False, True, False): 0.006,
        (False, False, True): 0.040,
        (False, False, False): 0.700
    }

    # Eliminate Cloudy and Rain to query P(WetGrass)
    res = ve.query(factor_vars, table, ["Cloudy", "Rain"])
    print("Marginal P(WetGrass):", res)
    assert res["remaining_vars"] == ["WetGrass"]

    print("Variable Elimination verified successfully!")

if __name__ == "__main__":
    main()
