import requests

def test_api_jikan_responde_com_sucesso():
    # Testa se a API pública de animes está online e respondendo
    url = "https://api.jikan.moe/v4/anime?q=Black Clover&limit=1"
    resposta = requests.get(url)
    
    # Valida se o status do código é 200 (Sucesso)
    assert resposta.status_code == 200
    
    # Valida se a API retornou dados na busca
    dados = resposta.json()
    assert "data" in dados
    assert len(dados["data"]) > 0