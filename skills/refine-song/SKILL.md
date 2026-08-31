---
name: refine-song
description: Diagnosticar, revisar e fortalecer letra musical existente sem perder sua identidade, corrigindo gancho, estrutura, narrativa, prosodia, rimas, cliches, vozes e prompt de estilo para Suno. Usar quando o usuario pedir para melhorar, lapidar, encurtar, expandir, tornar cantavel, trocar partes ou criar nova versao de uma letra em andamento.
---

# Refinar musica

Editar com preservacao: mudar somente o necessario e manter o que ja da identidade a composicao.

## Diagnosticar

1. Ler o projeto existente e a ultima versao, se houver.
2. Ler `../verseforge/references/output-contract.md` e `../verseforge/references/project-storage.md`.
3. Perguntar qual resultado esta incomodando apenas se nao estiver claro.
4. Classificar cada trecho como: preservar, lapidar, substituir, mover ou cortar.
5. Avaliar: conceito, arco, gancho, especificidade, prosodia, rimas, estrutura, coerencia vocal e compatibilidade com o estilo.

## Editar

- Preservar titulo, imagens, linhas ou secoes aprovadas pelo usuario.
- Resolver primeiro problemas estruturais; polimento de palavras vem depois.
- Manter voz, pessoa, tempo verbal e nivel de linguagem.
- Se alterar o refrão, conferir como os versos o preparam.
- Se houver album, checar `identity.md` antes de introduzir novos elementos.
- Quando a mudanca for ampla, explicar em uma frase o eixo da nova versao antes de reescrever.

## Comparar e salvar

Conferir se a versao nova melhora o alvo pedido sem apagar a personalidade anterior. Atualizar os arquivos correntes, validar limites e criar um novo snapshot com nota objetiva. Nunca substituir arquivo dentro de `versions/`.
