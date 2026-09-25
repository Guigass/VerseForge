---
name: reinterpret-song
description: Criar uma releitura de musica a partir da letra fornecida pelo usuario, com percentual de fidelidade controlavel, novo genero e presenca reconhecivel da obra-base. Usar quando o usuario pedir versao, adaptacao, releitura, troca de genero, nova roupagem ou preservacao graduada de historia, imagens, gancho, frases e emocao de uma musica.
---

# Reinterpretar musica

Transformar sem perder a linhagem. Tratar a porcentagem como alvo criativo mensuravel, nao como promessa matematica de similaridade.

## Preparar

1. Ler `../verseforge/references/output-contract.md`, `../verseforge/references/suno-guide.md` e `../verseforge/references/project-storage.md`.
2. Exigir a letra-fonte colada pelo usuario. Nao buscar nem completar letra comercial pelo titulo.
3. Perguntar, se ainda faltar: genero de destino, fidelidade de 0 a 100, voz e destino single/album.
4. Se o usuario disser apenas “originalidade”, esclarecer internamente com estes termos:
   - **fidelidade**: quanto da identidade da letra-fonte permanece;
   - **transformacao**: `100 - fidelidade`.
   Mostrar os dois no briefing para eliminar ambiguidade.

## Aplicar fidelidade

Usar `references/fidelity-scale.md`. Avaliar cinco dimensoes: historia, imagens, gancho/refrão, frases reconheciveis e emocao/personagem. Nao interpretar o percentual como porcentagem literal de versos copiados.

Antes de escrever, listar internamente:

- elementos inegociaveis;
- elementos que podem mudar;
- oportunidades naturais do novo genero;
- riscos de descaracterizacao.

## Compor

- Preservar primeiro o arco e os simbolos; preservar trechos literais apenas quando forem essenciais e fornecidos pelo usuario.
- Fazer o novo genero aparecer em metrica, flow, estrutura e dinamica, nao em referencias aleatorias.
- Adaptar a densidade silabica ao genero de chegada: rap aceita linhas densas e rimas internas; balada e bossa pedem linhas curtas e vogais longas. Nao manter a metrica da fonte se ela brigar com o novo groove.
- Em traducao ou versao para o portugues, reconstruir a prosodia: a silaba tonica precisa cair no tempo forte. Traducao literal quase sempre desloca acentos.
- No estilo, descrever o genero de **chegada**, nunca o genero ou a epoca da fonte (isso puxa o Suno de volta ao original). Colocar o genero de origem no Excluir quando houver risco de o Suno imita-lo.
- Evitar modernizacao automatica, cliches de produtividade, tecnologia, sucesso ou correria.
- Acrescentar cenas apenas quando aprofundarem o mesmo universo.
- Construir um refrão imediatamente associavel a fonte quando a fidelidade for media ou alta.
- Em dueto, definir se as vozes representam personagens da letra, tempos diferentes ou comentario e resposta.

## Revisar e salvar

Comparar o rascunho com cada dimensao da escala. Evitar reproduzir trechos longos da letra-fonte palavra por palavra acima do necessario para a fidelidade pedida; alem de criativamente fraco, o Suno pode bloquear letras comerciais reconheciveis. Se a musica parecer “outra musica inspirada”, recuperar ao menos dois marcadores fortes da fonte. Se parecer apenas uma copia sobre outro beat, transformar prosodia, estrutura e desenvolvimento.

Salvar a fonte em `sources/`, registrar fidelidade e transformacao no `brief.md`, validar limites e criar snapshot conforme `$verseforge`.
