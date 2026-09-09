def buscar_por_id(chamados, id_procurado):
    for chamado in chamados:
        if chamado["id"] == id_procurado:
            return chamado
    return None
//teste do Baugui

chamados = [
    {
        "id": 1,
        "titulo": "Impressora não imprime",
        "descricao": "A impressora do setor financeiro não responde.",
        "prioridade": "Média",
        "status": "Aberto",
        "solicitante": "Ana Souza",
    },
    {
        "id": 2,
        "titulo": "Sistema de login fora do ar",
        "descricao": "Usuários não conseguem autenticar no sistema interno.",
        "prioridade": "Alta",
        "status": "Em andamento",
        "solicitante": "Carlos Lima",
    },
    {
        "id": 3,
        "titulo": "Solicitação de novo monitor",
        "descricao": "Monitor atual apresenta falhas de imagem.",
        "prioridade": "Baixa",
        "status": "Resolvido",
        "solicitante": "Beatriz Alves",
    },
]

print("=== LISTAGEM ===")
for chamado in chamados:
    print(chamado)

print("=== BUSCA ===")
resultado = buscar_por_id(chamados, 2)
print(resultado if resultado else "Não encontrado")
