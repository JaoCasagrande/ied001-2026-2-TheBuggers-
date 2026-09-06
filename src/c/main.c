#include <stdio.h>

struct Chamado {
    int id;
    char titulo[50];
    char prioridade[10];
    char status[20];
};

int main(void) {
    struct Chamado chamados[3] = {
        {1, "Impressora nao imprime", "Media", "Aberto"},
        {2, "Login fora do ar", "Alta", "Em andamento"},
        {3, "Solicitacao de monitor", "Baixa", "Resolvido"}
    };

    printf("=== LISTAGEM ===\n");
    for (int i = 0; i < 3; i++) {
        printf("id=%d | titulo=%s | prioridade=%s | status=%s\n",
               chamados[i].id, chamados[i].titulo,
               chamados[i].prioridade, chamados[i].status);
    }

    return 0;
}