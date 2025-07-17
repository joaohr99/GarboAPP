import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


class CollectorAgent:
    """
    Agente responsável pela coleta de dados financeiros usando yfinance.
    """

    def __init__(self):
        # Isso não deveria estar aqui, mas para fins de teste no streamlit
        pass

    def get_historical_data(self, ticker: str, period: str = "1y") -> pd.DataFrame:
        """
        Baixa dados históricos de um ticker específico.

        Args:
            ticker (str): O símbolo da ação (ex: 'PETR4.SA' para Petrobras na B3).
            period (str): Período para baixar os dados (ex: '1y' para 1 ano, '5y' para 5 anos).
                          Verifique a documentação do yfinance para opções de período.

        Returns:
            pd.DataFrame: DataFrame com os dados históricos (Open, High, Low, Close, Volume).
                          Retorna um DataFrame vazio se houver erro ou dados não encontrados.
        """
        try:
            # Adiciona ".SA" para tickers da bolsa brasileira (B3)
            if not ticker.upper().endswith(".SA"):
                ticker_yf = f"{ticker.upper()}.SA"
            else:
                ticker_yf = ticker.upper()

            data = yf.download(ticker_yf, period=period)
            if data.empty:
                print(
                    f"Não foi possível baixar dados para {ticker_yf} no período {period}.")
                return pd.DataFrame()
            print(f"Dados baixados para {ticker_yf} com sucesso.")
            return data
        except Exception as e:
            print(f"Erro ao baixar dados para {ticker}: {e}")
            return pd.DataFrame()

    def get_multiple_tickers_data(self, tickers: list[str], period: str = "1y") -> dict[str, pd.DataFrame]:
        """
        Baixa dados históricos para múltiplos tickers.

        Args:
            tickers (list[str]): Lista de símbolos das ações.
            period (str): Período para baixar os dados.

        Returns:
            dict[str, pd.DataFrame]: Um dicionário onde a chave é o ticker e o valor é o DataFrame
                                     com os dados históricos.
        """
        all_data = {}
        for ticker in tickers:
            data = self.get_historical_data(ticker, period)
            if not data.empty:
                all_data[ticker] = data
        return all_data


# Exemplo de uso (para teste local, pode ser removido depois)
if __name__ == "__main__":
    collector = CollectorAgent()
    # Exemplo de um único ticker
    petr4_data = collector.get_historical_data(
        "PETR4", period="6mo")  # 6 meses para testar o crescimento
    if not petr4_data.empty:
        print("\nDados de PETR4.SA (últimos 6 meses):")
        print(petr4_data.head())

    # Exemplo de múltiplos tickers
    tickers_to_fetch = ["VALE3", "ITUB4", "BBAS3"]
    multiple_data = collector.get_multiple_tickers_data(
        tickers_to_fetch, period="1y")
    print("\nDados de múltiplos tickers:")
    for ticker, df in multiple_data.items():
        print(f"\n--- {ticker}.SA ---")
        print(df.head())
