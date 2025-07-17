import streamlit as st
import pandas as pd
from agno_agents.collector_agent import CollectorAgent
# Importar os agentes Agno aqui quando eles estiverem prontos
# from agno_agents.analyzer_agent import AnalyzerAgent

st.set_page_config(layout="wide")

st.title("Garbo: Ações em Destaque no Mercado Financeiro 📈")

st.markdown("""
Bem-vindo ao Garbo! Aqui você encontra uma visualização simplificada das ações que,
segundo nossa análise, estão apresentando um bom desempenho no mercado.
""")

# --- Seção para exibir as ações em destaque ---
st.header("Ações Atualmente em Destaque")

st.subheader("Teste do Agente Coletor")
collector = CollectorAgent()
test_ticker_data = collector.get_historical_data("PETR4", period="1mo")
if not test_ticker_data.empty:
    st.write("Dados de PETR4.SA (último mês) via CollectorAgent:")
    st.dataframe(test_ticker_data.tail())
else:
    st.write("Não foi possível obter dados de PETR4.SA.")

# Por enquanto, vamos simular alguns dados.
# No futuro, esta seção será preenchida pelos resultados do Agente de Análise.
dados_simulados = {
    'Ticker': ['PETR4', 'VALE3', 'ITUB4', 'BBAS3', 'WEGE3'],
    'Nome da Empresa': ['Petrobras PN', 'Vale S.A.', 'Banco Itaú PN', 'Banco do Brasil ON', 'Weg S.A.'],
    'Preço Atual (R$)': [35.50, 68.20, 30.15, 55.80, 42.30],
    'Crescimento 5M (%)': [12.5, 8.1, 9.3, 15.0, 10.2],
    'Queda Máxima 12M (%)': [-5.0, -8.5, -3.2, -4.1, -6.0],
    'Status': ['Em Destaque', 'Em Destaque', 'Em Destaque', 'Em Destaque', 'Em Destaque']
}
df_destaque = pd.DataFrame(dados_simulados)

if not df_destaque.empty:
    st.dataframe(df_destaque, use_container_width=True)
else:
    st.info(
        "Nenhuma ação em destaque encontrada no momento. Tente novamente mais tarde.")

st.markdown("---")
st.markdown("Desenvolvido com Agno e Streamlit.")

# --- Área para futuras funcionalidades (ex: busca por ticker, detalhes) ---
st.sidebar.header("Opções")
# ticker_busca = st.sidebar.text_input("Buscar Ticker (ex: PETR4)", "")
# if ticker_busca:
#     st.sidebar.write(f"Buscando detalhes para: {ticker_busca}")
#     # Lógica para buscar e exibir detalhes de um ticker específico
