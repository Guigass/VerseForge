# VerseForge

Este repositorio e uma oficina musical baseada em skills.

## Regra principal

Ao receber um pedido musical, usar primeiro `skills/verseforge/SKILL.md`. Ela seleciona a skill especializada, conduz as perguntas e define salvamento, validacao e entrega.

Quando o usuario trouxer uma ideia vaga, pedir dicas ou quiser desenvolver um conceito do zero, usar `skills/develop-music-concept/SKILL.md` antes de iniciar a composicao.

## Persistencia

- Salvar singles em `projects/singles/`.
- Salvar albuns e suas faixas em `projects/albums/`.
- Salvar a exploracao aprovada do album em `creative-direction.md` e o planejamento das musicas-fonte em `source-map.md`.
- Ler a identidade de um album antes de criar ou revisar qualquer faixa dele.
- Preservar `versions/`; criar nova versao em vez de sobrescrever historico.

## Qualidade

- Fazer perguntas em rodadas curtas e nao repetir informacoes ja dadas.
- Seguir `skills/verseforge/references/suno-guide.md` ao escrever letra, estilo, excluir e configuracoes.
- Validar com `skills/verseforge/scripts/validate_suno.py --project <pasta>` antes de entregar; corrigir erros e resolver ou justificar avisos.
- Ao compor ou revisar uma musica, sempre entregar `LETRA`, `ESTILO PARA O SUNO`, `EXCLUIR` e `CONFIGURACOES`. Em rodadas apenas de direcao criativa, registrar decisoes e terminar com o proximo passo.
- Tags de secao em ingles; estilo em ingles e sem negativos; parenteses apenas para backing vocals.
- Nunca usar nomes de artistas no campo de estilo.
- Nao buscar ou reconstruir letras comerciais nao fornecidas pelo usuario.
