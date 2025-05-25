import pandas as pd

class DataCleaner:
    def __init__(self, dataframes_dict):
        """
        dataframes_dict: dicionário de DataFrames vindo do DataLoader
        Espera as chaves:
            - colaboradores
            - unimed
            - gympass
            - github
            - google
        """
        self.dfs = dataframes_dict

    def clean_all(self):
        # Clonamos para não alterar o original
        cleaned = {}

        # 1. Colaboradores
        df_colab = self.dfs["colaboradores"].copy()
        df_colab["cpf"] = df_colab["cpf"].astype(str).str.strip()
        df_colab["salario"] = pd.to_numeric(df_colab["salario"], errors="coerce").fillna(0)
        cleaned["colaboradores"] = df_colab

        # 2. Unimed
        df_unimed = self.dfs["unimed"].copy()
        df_unimed["cpf"] = df_unimed["cpf"].astype(str).str.strip()
        df_unimed["unimed"] = pd.to_numeric(df_unimed["unimed"], errors="coerce").fillna(0)
        cleaned["unimed"] = df_unimed

        # 3. Gympass
        df_gym = self.dfs["gympass"].copy()
        df_gym["cpf"] = df_gym["cpf"].astype(str).str.strip()
        df_gym["gympass"] = pd.to_numeric(df_gym["gympass"], errors="coerce").fillna(0)
        cleaned["gympass"] = df_gym

        # 4. GitHub
        df_git = self.dfs["github"].copy()
        df_git["cpf"] = df_git["cpf"].astype(str).str.strip()
        df_git["github"] = pd.to_numeric(df_git["github"], errors="coerce").fillna(0)
        cleaned["github"] = df_git

        # 5. Google Workspace
        df_google = self.dfs["google"].copy()
        df_google["cpf"] = df_google["cpf"].astype(str).str.strip()
        df_google["google_workspace"] = pd.to_numeric(df_google["google_workspace"], errors="coerce").fillna(0)
        cleaned["google"] = df_google

        return cleaned
