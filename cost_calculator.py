class CostCalculator:
    def __init__(self, df_merged):
        """
        df_merged: DataFrame unificado vindo do DataJoiner
        Deve conter: salario, github, google_workspace, unimed, gympass
        """
        self.df = df_merged.copy()

    def calculate(self):
        # Calcula o custo total (salário + ferramentas + benefícios)
        self.df["valor_total"] = (
            self.df["salario"] +
            self.df["github"] +
            self.df["google_workspace"] +
            self.df["unimed"] +
            self.df["gympass"]
        )

        return self.df
