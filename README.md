# Projeto de Modernização de Sistema Legado Bancário com Golden Master Testing e Padrão Strategy

## 🚀 Visão Geral do Projeto

Este projeto demonstra uma abordagem robusta e segura para modernizar sistemas legados críticos, como os encontrados no setor bancário. Focamos na reestruturação de um sistema hipotético de cálculo de juros da década de 90, utilizando duas técnicas poderosas:

1.  **Golden Master Testing (Testes de Regressão):** Para garantir que as novas implementações se comportem *exatamente* como o sistema legado, minimizando riscos.
2.  **Padrão Strategy:** Para refatorar a lógica de cálculo de juros, tornando-a modular, flexível e fácil de estender.

O objetivo é permitir que instituições financeiras evoluam suas plataformas sem "quebrar" funcionalidades existentes, um desafio comum em ambientes de missão crítica.

## 💡 O Problema: Sistemas Legados no Setor Bancário

Sistemas bancários antigos, muitas vezes desenvolvidos em tecnologias como COBOL e rodando em mainframes, são a espinha dorsal de operações financeiras. Eles funcionam, mas são:

*   **Difíceis de Manter:** A lógica de negócio está emaranhada, tornando qualquer alteração arriscada.
*   **Rígidos à Mudança:** Adaptar-se a novas regulamentações ou produtos é lento e custoso.
*   **Barreiras à Inovação:** A complexidade impede a adoção de novas tecnologias e metodologias.

Qualquer tentativa de reescrever ou refatorar esses sistemas pode introduzir erros catastróficos, resultando em perdas financeiras, multas regulatórias e danos à reputação.

## ✨ A Solução Proposta

### 1. Golden Master Testing (O "Espelho Mágico")

Esta técnica é essencial para garantir a **compatibilidade de comportamento**. Antes de qualquer refatoração, capturamos o comportamento exato do sistema legado. É como tirar uma "fotografia" de todos os resultados que o sistema antigo produz para um conjunto de entradas. Essa "fotografia" é o nosso **Golden Master**.

*   **Como funciona:** Geramos um grande volume de casos de teste (perfis de clientes, valores de empréstimos, prazos) e os executamos no sistema legado. Os resultados são salvos como o Golden Master.
*   **Utilidade:** Qualquer nova implementação ou refatoração é testada contra este Golden Master. Se os resultados forem idênticos, temos a certeza de que o novo código replica fielmente o comportamento do antigo, sem introduzir regressões.

### 2. Padrão Strategy (A "Caixa de Ferramentas Inteligente")

Para tornar a lógica de cálculo de juros mais flexível e manutenível, aplicamos o Padrão Strategy. Em vez de uma única função monolítica que calcula todos os tipos de juros, separamos cada regra de cálculo em sua própria "estratégia".

*   **Como funciona:** Criamos interfaces para o cálculo de juros e implementações concretas para cada tipo de regra (ex: juros para clientes de Risco A, Risco B, Risco C). O sistema então seleciona a estratégia apropriada com base no perfil do cliente.
*   **Utilidade:** Permite adicionar novas regras de juros (ex: "Juros para Clientes VIP", "Juros para Empréstimos Sustentáveis") sem modificar o código existente, seguindo o Princípio Open/Closed. Facilita a manutenção e o teste de cada regra isoladamente.

## 🛠️ Estrutura do Projeto

```
modernizacao_legado_bancario/
├── legacy_calculator.py          # Simula o sistema legado de cálculo de juros (década de 90)
├── generate_test_cases.py        # Gera um conjunto de casos de teste aleatórios
├── golden_master_tester.py       # Ferramenta para gerar o Golden Master e executar testes de regressão
├── modern_interest_calculator.py # Implementação da nova arquitetura com Padrão Strategy
├── run_modernization_test.py     # Script para executar o teste de regressão da nova arquitetura
└── README.md                     # Este arquivo
```

## 🚀 Como Rodar o Projeto (Cenário Hipotético)

Este projeto foi desenvolvido em Python 3.11+.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd modernizacao_legado_bancario
    ```

2.  **Gerar Casos de Teste:**
    Primeiro, precisamos de dados para testar. Este script cria `test_cases.json` com 100 cenários de empréstimo.
    ```bash
    python3.11 generate_test_cases.py
    ```

3.  **Gerar o Golden Master:**
    Agora, usamos o `legacy_calculator.py` para processar esses casos de teste e gerar o `golden_master_data.json`. Este arquivo contém os resultados "corretos" do sistema legado.
    ```bash
    python3.11 golden_master_tester.py
    ```
    *Você verá uma mensagem de "Teste de Regressão PASSOU" aqui, pois estamos comparando o sistema legado consigo mesmo, apenas para validar a geração do Golden Master.*

4.  **Testar a Nova Arquitetura:**
    Finalmente, executamos o teste de regressão usando a `modern_interest_calculator.py` contra o `golden_master_data.json`. Isso verificará se a nossa nova implementação com Padrão Strategy produz os mesmos resultados que o sistema legado.
    ```bash
    python3.11 run_modernization_test.py
    ```

    *Se tudo estiver correto, você verá a mensagem: "Parabéns! A nova implementação com Padrão Strategy é compatível com o sistema legado."*

## 📈 Demonstração de uma Quebra (Opcional)

Para entender a importância do Golden Master, você pode simular uma quebra:

1.  Abra `modern_interest_calculator.py`.
2.  Localize a linha onde a taxa mensal é calculada para `risk_category == "A"` (ou qualquer outra categoria) e altere-a ligeiramente (ex: de `0.015` para `0.016`).
3.  Execute novamente:
    ```bash
    python3.11 run_modernization_test.py
    ```
    Você verá que o teste de regressão **FALHARÁ**, indicando exatamente quais casos de teste foram afetados pela sua mudança, provando a eficácia do Golden Master em detectar regressões.

## 🎯 Conclusão

Este projeto ilustra como a combinação de **Golden Master Testing** e **Padrões de Projeto (Strategy)** pode ser empregada para modernizar sistemas legados de forma controlada e segura. É uma estratégia fundamental para equipes de engenharia de software que buscam inovar em ambientes complexos e de alta responsabilidade, como o setor bancário.

--- 

**Autor:** [Seu Nome Aqui]
**Data:** Fevereiro de 2026
