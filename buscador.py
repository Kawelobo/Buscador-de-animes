import requests

def buscar_anime(nome):
    # A URL da API usando o nome do anime como parâmetro de busca
    url = f"https://api.jikan.moe/v4/anime?q={nome}&sfw"
    
    print(f"Buscando informações para: {nome}...\n")
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        resultados = dados.get("data", [])
        
        if resultados:
            # Pegando o primeiro resultado da busca
            anime = resultados[0]
            titulo = anime.get("title")
            episodios = anime.get("episodes")
            nota = anime.get("score")
            sinopse = anime.get("synopsis")
            
            print(f"🎯 Título: {titulo}")
            print(f"📺 Episódios: {episodios}")
            print(f"⭐ Nota: {nota}")
            print(f"📖 Sinopse: {sinopse[:250]}...") # Mostra apenas os primeiros 250 caracteres
        else:
            print("Nenhum anime encontrado com esse nome.")
    else:
        print("Erro ao conectar com a API.")

# Testando o nosso buscador
buscar_anime("Black Clover")