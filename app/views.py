from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"nome": "Endrick Felipe", "idade": "18 anos",
         "nascimento": "Taguatinga - DF",
         "posicao": "Atacante", "foto": "endrick.png" },
         {"nome": "Rodrygo Silva", "idade": "23 anos",
         "nascimento": "Osasco - SP",
         "posicao": "Atacante", "foto": "rodrygo.png" },
         {"nome": "Vinicius Júnior", "idade": "24 anos",
         "nascimento": "Rio de Janeiro - RJ",
         "posicao": "Ponta esquerda", "foto": "vini.png" },
         {"nome": "Lucas Paquetá", "idade": "26 anos",
         "nascimento": "Ilha de paquetá - RJ",
         "posicao": "Meio-campista", "foto": "paqueta.png" },
         {"nome": "Bruno Guimarães", "idade": "26 anos",
         "nascimento": "Rio de Janeiro - RJ",
         "posicao": "Volante e meio-campista", "foto": "bruno.png" },
         {"nome": "João Gomes", "idade": "23 anos",
         "nascimento": "Rio de Janeiro - RJ",
         "posicao": "Volante", "foto": "joao.png" },
         {"nome": "Danilo Silva", "idade": "33 anos",
         "nascimento": "Bicas - MG",
         "posicao": "Lateral-direito e zagueiro", "foto": "danilo.png" },
         {"nome": "Marquinhos", "idade": "30 anos",
         "nascimento": "São Paulo - SP",
         "posicao": "Zagueiro", "foto": "marquinhos.png" },
         {"nome": "Guilherme Arana", "idade": "27 anos",
         "nascimento": "São Paulo - SP",
         "posicao": "Lateral esquerdo", "foto": "arana.png" },
         {"nome": "Eder Militão", "idade": "26 anos",
         "nascimento": "Sertãozinho - SP",
         "posicao": "Zagueiro", "foto": "militao.png" },
         {"nome": "Alisson Becker", "idade": "31 anos",
         "nascimento": "Novo Hamburgo - RS",
         "posicao": "Goleiro", "foto": "alisson.png" }
    ]
    context = {
        "jogadores": jogadores,
    }
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")