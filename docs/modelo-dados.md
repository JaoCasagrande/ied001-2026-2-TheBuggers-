# Modelo de Dados - Entidade Principal

## Entidade
Chamado

## Finalidade
Representa uma solicitação de suporte aberta por um usuário, que a equipe acompanha até a resolução.

## Atributos
- id: identificador único do chamado
- titulo: resumo curto do problema relatado
- descricao: detalhamento do problema
- prioridade: nível de urgência (Baixa, Média, Alta)
- status: situação atual (Aberto, Em andamento, Resolvido, Fechado)
- solicitante: usuário que abriu o chamado

## Operações
- cadastrar(chamado)
- buscar_por_id(id)
- listar()
- atualizar_status(id, novo_status)

## Regras / invariantes
1. O id de cada chamado deve ser único.
2. O status só pode assumir um dos valores previstos (Aberto, Em andamento, Resolvido, Fechado).

## Operação provavelmente frequente
buscar_por_id - justificativa: usuários e administradores consultam o andamento de um chamado específico com mais frequência do que listam todos os chamados.