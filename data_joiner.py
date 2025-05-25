import pandas as pd

class DataJoiner:
    def __init__(self, cleaned_dfs):
        """
        cleaned_dfs: dicionário de DataFrames vindos do DataCleaner
        """
        self.dfs = cleaned_dfs

    def join_all(self):
        # Começa com a base de colaboradores
        df_final = self.dfs["colaboradores"].copy()

        # Junta com cada benefício/ferramenta, preenchendo ausentes com 0
        for key in ["unimed", "gympass", "github", "google"]:
            df_to_merge = self.dfs[key]
            df_final = pd.merge(df_final, df_to_merge, on="cpf", how="left")

        # Substitui valores NaN por 0 nas colunas numéricas adicionadas
        for col in ["unimed", "gympass", "github", "google_workspace"]:
            if col in df_final.columns:
                df_final[col] = df_final[col].fillna(0)

        return df_final
