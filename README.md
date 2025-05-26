# Desafio-DevOps
**Agent de Manipulação de Dados**

**Descrição do Projeto**

Este projeto implementa um pipeline modular, orientado a objetos, para leitura, limpeza, transformação e consolidação de dados de colaboradores, benefícios e ferramentas. O resultado final é um relatório em Excel com o custo total por colaborador.

**Estrutura do Projeto**

data_loader.py - Classe DataLoader: lê e padroniza arquivos .xlsx

data_cleaner.py - Classe DataCleaner: trata tipos e remove valores inválidos

data_joiner.py - Classe DataJoiner: faz merge dos dados por CPF

cost_calculator.py - Classe CostCalculator: calcula custo total por colaborador

report_generator.py - Classe ReportGenerator: gera o relatório final em Excel

main.py - Orquestra todo o pipeline chamando as classes acima

requirements.txt - Dependências do projeto (pandas, openpyxl)

Dados Colaboradores.xlsx

Beneficio 1 - Unimed.xlsx

Beneficio 2 - Gympass.xlsx

Ferramenta 1 - Github.xlsx

Ferramenta 2 - Google workspace.xlsx

relatorio_final.xlsx - Exemplo de saída gerada

**Como Rodar**
1. Crie e ative um ambiente virtual

2. Instale as dependências, requirements.txt

3. Execute o arquivo main.py

4. O relatório será gerado em relatorio_final.xlsx.

**Arquivo de Saída**

O arquivo relatorio_final.xlsx contém as colunas:
- Nome Colaborador
- CPF
- Centro de Custo
- Salario
- Github
- Google workspace
- Unimed
- Gympass
- Valor Total

Observações sobre CrewAI

Inicialmente, foi proposta a orquestração dos módulos usando CrewAI, criando agentes para cada etapa do pipeline. Em testes locais, não foi possível estabelecer conexão estável com o LLM (via Together.ai ou HuggingFace), resultando em erros de autenticação e requisição. Por isso, o pipeline foi implementado e testado com programação orientada a objetos (POO), garantindo clareza, modularidade e facilidade de manutenção.
