---
name: mashup-songs
description: Criar uma letra-mashup coesa usando duas ou mais letras fornecidas pelo usuario, equilibrando contribuicao, narrativa, ganchos e identidade de cada fonte em um novo arranjo para Suno. Usar quando o usuario quiser fundir, cruzar, alternar, responder ou combinar varias musicas em uma unica faixa.
---

# Criar mashup

Fazer as fontes conversarem. Evitar colagem de trechos sem arco dramatico.

## Preparar

1. Ler `../verseforge/references/output-contract.md`, `../verseforge/references/suno-guide.md` e `../verseforge/references/project-storage.md`.
2. Receber no minimo duas letras completas do usuario; nao buscar nem reconstruir fontes ausentes.
3. Perguntar ou propor:
   - porcentagem de contribuicao de cada fonte, totalizando 100;
   - musica-ancora e funcao das demais;
   - genero de chegada;
   - voz masculina, feminina ou dueto e distribuicao das partes;
   - tipo de fusao: narrativa unica, dialogo, alternancia, medley evolutivo ou refrões cruzados.

## Mapear as fontes

Para cada musica, extrair: historia, ponto de vista, imagens, frase/gancho, emocao, ritmo verbal e elementos inegociaveis. Em seguida escolher uma espinha dorsal unica:

- **ancora/resposta:** uma fonte narra e outra contesta;
- **antes/depois:** cada fonte ocupa uma fase do arco;
- **dois personagens:** as fontes viram vozes em dialogo;
- **mundo compartilhado:** imagens das fontes compoem uma nova cena;
- **medley:** secoes mantem identidade propria, ligadas por transicoes planejadas.

## Compor e revisar

- Dar a cada fonte ao menos um marcador inequivoco quando sua contribuicao for relevante.
- Criar transicoes semanticas e musicais; nao apenas alternar estrofes.
- Usar um refrão unificador novo ou cruzar ganchos de modo cantavel.
- Marcar vozes somente quando isso ajuda a performance, seguindo as regras de dueto de `suno-guide.md`.
- Unificar a metrica: fontes com metricas diferentes precisam ser reescritas para o mesmo pulso, ou separadas por uma tag de transicao (`[Interlude]`, `[Breakdown: half-time]`).
- Estilo com um unico genero de chegada; fusoes de dois generos precisam dizer qual domina ("samba-rock with boom-bap drums"), senao o Suno alterna sem controle.
- Verificar se a participacao percebida acompanha aproximadamente os percentuais do briefing.
- Remover conflitos de pessoa, tempo, lugar ou tom que nao sejam deliberados.

Salvar cada fonte separadamente em `sources/`, registrar pesos e papeis no `brief.md`, validar e versionar conforme `$verseforge`.
