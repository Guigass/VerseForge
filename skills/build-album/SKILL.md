---
name: build-album
description: Planejar, criar e manter album ou EP com identidade coerente entre faixas, incluindo conceito, arco, paleta sonora, vozes, motivos recorrentes, regras liricas, tracklist e projetos de cada musica. Usar quando o usuario quiser criar um album, EP, conjunto conceitual, identidade musical compartilhada ou adicionar faixas mantendo unidade artistica.
---

# Construir album

Criar unidade sem tornar todas as faixas iguais. Tratar `identity.md` como contrato vivo do album.

## Iniciar o album

1. Ler `../verseforge/references/project-storage.md` e `references/album-identity.md`.
2. Se a ideia ainda estiver aberta, acionar `$develop-music-concept` antes de fechar identidade ou tracklist.
3. Descobrir em rodadas curtas: conceito, arco do ouvinte, generos, voz ou elenco vocal, escala do projeto e contrastes desejados.
4. Criar a pasta com `../verseforge/scripts/new_project.py album --title "..."`.
5. Preencher `creative-direction.md`, `source-map.md`, `album.yaml`, `identity.md` e `tracklist.md`.

## Desenvolver com o usuario

- Apresentar tres direcoes de album quando houver apenas uma ideia inicial.
- Recomendar uma, mas permitir mistura consciente entre caminhos.
- Dar dicas ligadas a escolhas concretas: narrativa, repertorio, arranjo, voz, ritmo e sequenciamento.
- Salvar o raciocinio aprovado em `creative-direction.md` para que sessoes futuras retomem do ponto correto.
- Se houver releituras de musicas conhecidas, construir `source-map.md` antes de definir toda a tracklist.
- Pedir as letras somente quando uma fonte for escolhida para adaptacao; nao bloquear o planejamento inicial por ainda nao ter todas elas.

## Definir as vozes

Registrar uma destas estrategias:

- voz masculina em todo o album;
- voz feminina em todo o album;
- dueto recorrente com papeis estaveis;
- elenco vocal com regras por faixa;
- voz principal fixa e participacoes pontuais.

Descrever timbre, entrega, registro, diccao e relacao entre vozes. Nao usar nomes de artistas no estilo do Suno.

## Projetar a tracklist

Dar a cada faixa uma funcao no arco: abertura, convite, tensao, mergulho, respiro, virada, climax ou desfecho. Variar BPM, densidade, perspectiva e estrutura dentro da paleta comum. Evitar duas faixas consecutivas com a mesma funcao emocional, salvo decisao consciente.

## Criar uma faixa

1. Ler `creative-direction.md`, `source-map.md`, `identity.md`, `album.yaml` e `tracklist.md` antes das perguntas.
2. Escolher original, releitura, mashup ou refinamento e acionar a skill correspondente.
3. Criar a pasta com `new_project.py track --album <slug> --track-number <n> --title "..."`.
4. Registrar no `brief.md`:
   - funcao da faixa no arco;
   - elementos da identidade preservados;
   - contraste exclusivo desta faixa;
   - voz e relacao com as outras faixas.
5. Atualizar `tracklist.md` e validar a faixa.

## Evoluir a identidade

Atualizar `identity.md` somente quando uma decisao aprovada se tornar regra do conjunto. Nao retroajustar silenciosamente faixas prontas. Se uma mudanca afetar outras musicas, listar o impacto antes de editar.
