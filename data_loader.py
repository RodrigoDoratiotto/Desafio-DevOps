import pandas as pd

class DataLoader:
    def __init__(self, path_dict):
        """
        path_dict: dicionário com os caminhos dos arquivos. Exemplo:
        {
            "colaboradores": "Dados Colaboradores.xlsx",
            "unimed": "Benefício 1 - Unimed.xlsx",
            "gympass": "Benefício 2 - Gympass.xlsx",
            "github": "Ferramenta 1 - Github.xlsx",
            "google": "Ferramenta 2 - Google workspace.xlsx"
        }
        """
        self.paths = path_dict

    def load_all(self):
        # 1. Colaboradores
        df_colab = pd.read_excel(self.paths["colaboradores"])
        df_colab.columns = df_colab.columns.str.strip().str.lower()
        df_colab = df_colab.rename(columns={
            "departamento": "centro_custo"
        })
        df_colab = df_colab[["nome", "cpf", "centro_custo", "salario"]]

        # 2. Unimed
        df_unimed = pd.read_excel(self.paths["unimed"])
        df_unimed.columns = df_unimed.columns.str.strip().str.lower()
        df_unimed = df_unimed.rename(columns={
            "total": "unimed"
        })
        df_unimed = df_unimed[["cpf", "unimed"]]

        # 3. Gympass
        df_gym = pd.read_excel(self.paths["gympass"])
        df_gym.columns = df_gym.columns.str.strip().str.lower()
        df_gym = df_gym.rename(columns={
            "documento": "cpf",
            "valor mensal": "gympass"
        })
        df_gym = df_gym[["cpf", "gympass"]]

        # 4. GitHub
        df_git = pd.read_excel(self.paths["github"])
        df_git.columns = df_git.columns.str.strip().str.lower()
        df_git = df_git.rename(columns={
            "documento": "cpf",
            "valor mensal": "github"
        })
        df_git = df_git[["cpf", "github"]]

        # 5. Google Workspace
        df_google = pd.read_excel(self.paths["google"])
        df_google.columns = df_google.columns.str.strip().str.lower()
        df_google = df_google.rename(columns={
            "documento": "cpf",
            "valor mensal": "google_workspace"
        })
        df_google = df_google[["cpf", "google_workspace"]]

        # Retornar os DataFrames organizados
        return {
            "colaboradores": df_colab,
            "unimed": df_unimed,
            "gympass": df_gym,
            "github": df_git,
            "google": df_google
        }
