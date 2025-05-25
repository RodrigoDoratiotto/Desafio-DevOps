from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_joiner import DataJoiner
from cost_calculator import CostCalculator
from report_generator import ReportGenerator

def main():
    # Caminhos dos arquivos de entrada
    paths = {
        "colaboradores": "Dados Colaboradores.xlsx",
        "unimed": "Beneficio 1 - Unimed.xlsx",
        "gympass": "Beneficio 2 - Gympass.xlsx",
        "github": "Ferramenta 1 - Github.xlsx",
        "google": "Ferramenta 2 - Google workspace.xlsx"
    }

    print("🚀 Iniciando DataLoader...")
    loader = DataLoader(paths)
    dfs = loader.load_all()

    print("🧼 Iniciando DataCleaner...")
    cleaner = DataCleaner(dfs)
    dfs_clean = cleaner.clean_all()

    print("🔗 Iniciando DataJoiner...")
    joiner = DataJoiner(dfs_clean)
    df_merged = joiner.join_all()

    print("💰 Iniciando CostCalculator...")
    calculator = CostCalculator(df_merged)
    df_final = calculator.calculate()

    print("📄 Iniciando ReportGenerator...")
    reporter = ReportGenerator(df_final)
    output_file = reporter.generate_report("relatorio_final.xlsx")

    print(f"✅ Relatório gerado com sucesso: {output_file}")

if __name__ == "__main__":
    main()
