class VariableEliminationInference:
    """Exact inference in discrete Bayesian Networks using Variable Elimination."""
    def marginalize(self, factor_vars: list[str], var_to_eliminate: str, table: dict) -> tuple[list[str], dict]:
        if var_to_eliminate not in factor_vars:
            return factor_vars, table
        var_idx = factor_vars.index(var_to_eliminate)
        new_vars = [v for v in factor_vars if v != var_to_eliminate]
        new_table = {}
        for key, prob in table.items():
            reduced_key = tuple(val for i, val in enumerate(key) if i != var_idx)
            new_table[reduced_key] = new_table.get(reduced_key, 0.0) + prob
        return new_vars, new_table

    def query(self, factor_vars: list[str], table: dict, eliminate_order: list[str]) -> dict:
        curr_vars = list(factor_vars)
        curr_table = dict(table)
        for var in eliminate_order:
            curr_vars, curr_table = self.marginalize(curr_vars, var, curr_table)

        # Normalize
        total = sum(curr_table.values())
        normalized = {str(k): round(v / total, 5) for k, v in curr_table.items()}
        return {
            "remaining_vars": curr_vars,
            "distribution": normalized
        }
