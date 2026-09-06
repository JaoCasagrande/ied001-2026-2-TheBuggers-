# Central de Chamados de Suporte

## Grupo
- PM: Elizeu Ribeiro
- Tech Lead: João Victor de Oliveira Nunes Casagrande
- Team Members: Gabriella Galdino Araujo, Sana Soraes Hachem, Caroline de Farias

## Problema
Sistema para abertura, acompanhamento e gestão de chamados de suporte técnico,
com dois perfis de usuário (administrador e usuário final), permitindo registrar
solicitações, consultar status e organizar chamados por prioridade.

## Entidade do primeiro incremento
Chamado - representa uma solicitação de suporte aberta por um usuário, com
título, descrição, prioridade, status e solicitante.

## Executar Python
python src/python/main.py

## Compilar e executar C
mkdir build
gcc -Wall -Wextra -std=c17 src/c/main.c -o build/main.exe
./build/main.exe

## Sprint atual
Sprint 01 - Setup inicial e primeiro incremento executável (entidade Chamado).