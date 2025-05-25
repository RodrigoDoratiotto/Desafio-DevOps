import pandas as pd

class ReportGenerator:
    def __init__(self, df_cost_calculated):
        """
        df_cost_calculated: DataFrame vindo do CostCalculator
        Deve conter: nome, cpf, centro_custo, salario, github, google_workspace, unimed, gympass, valor_total
        """
        self.df = df_cost_calculated.copy()

    def generate_report(self, output_path="relatorio_final.xlsx"):
        # Renomear colunas conforme exemplo de resultado
        df_export = self.df.rename(columns={
            "nome": "Nome Colaborador",
            "cpf": "CPF",
            "centro_custo": "Centro de Custo",
            "salario": "Salario",
            "github": "Github",
            "google_workspace": "Google workspace",
            "unimed": "Unimed",
            "gympass": "Gympass",
            "valor_total": "Valor Total"
        })

        # Definir ordem final das colunas
        colunas_ordenadas = [
            "Nome Colaborador", "CPF", "Centro de Custo", "Salario",
            "Github", "Google workspace", "Unimed", "Gympass", "Valor Total"
        ]

        df_export = df_export[colunas_ordenadas]

        # Exportar para Excel
        df_export.to_excel(output_path, index=False)

        return output_path  # retorna caminho salvo
