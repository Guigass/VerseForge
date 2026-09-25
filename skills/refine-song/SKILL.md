---
name: refine-song
description: Diagnosticar, revisar e fortalecer letra musical existente sem perder sua identidade, corrigindo gancho, estrutura, narrativa, prosodia, rimas, cliches, vozes e prompt de estilo para Suno. Tambem diagnostica geracoes do Suno que sairam erradas (genero, voz, pronuncia, letra atropelada, tag cantada, final) e ajusta letra, estilo, excluir e configuracoes. Usar quando o usuario pedir para melhorar, lapidar, encurtar, expandir, tornar cantavel, trocar partes, criar nova versao, ou relatar que o resultado do Suno nao ficou como esperado.
---

# Refinar musica

Editar com preservacao: mudar somente o necessario e manter o que ja da identidade a composicao.

## Diagnosticar a letra

1. Ler o projeto existente e a ultima versao, se houver.
2. Ler `../verseforge/references/output-contract.md`, `../verseforge/references/suno-guide.md` e `../verseforge/references/project-storage.md`.
3. Rodar `../verseforge/scripts/validate_suno.py --project <pasta>` e considerar os avisos como parte do diagnostico.
4. Perguntar qual resultado esta incomodando apenas se nao estiver claro.
5. Classificar cada trecho como: preservar, lapidar, substituir, mover ou cortar.
6. Avaliar: conceito, arco, gancho, especificidade, prosodia, rimas, estrutura, coerencia vocal e compatibilidade com o estilo.

## Diagnosticar uma geracao do Suno

Quando o usuario disser o que saiu errado no audio:

1. Identificar o sintoma com uma pergunta curta se necessario: em qual secao, o que aconteceu, qual modelo e controles foram usados.
2. Localizar a causa na tabela "Problemas comuns" de `suno-guide.md`.
3. Escolher a **menor intervencao** que resolve, nesta ordem:
   - editar so a secao no Suno (edicao por linguagem natural ou troca de palavra/linha) quando o resto da faixa esta bom;
   - ajustar controles (Style Influence, Weirdness) ou `Excluir`;
   - reescrever a tag ou as linhas problematicas;
   - reordenar ou reescrever o estilo;
   - regenerar a faixa inteira apenas se a base (voz, groove, refrao) estiver errada.
4. Explicar em uma frase a causa provavel e o que foi mudado.
5. Quando a edicao for feita no proprio Suno, fornecer o texto exato da instrucao ou da linha substituta.
6. Registrar no `brief.md`, em `## Revisoes`, o sintoma, a causa e o ajuste, para orientar faixas futuras.

## Migrar projetos antigos

Letras com tags em portugues (`[Verso]`, `[Refrão]`, `[Voz masculina]`), tags empilhadas, estilo em portugues ou negativos no estilo devem ser convertidas ao formato atual ao serem revisadas: tags em ingles combinadas, estilo em ingles, negativos para `suno-exclude.txt`. Isso nao muda o conteudo artistico e deve ser registrado como revisao tecnica.

## Editar

- Preservar titulo, imagens, linhas ou secoes aprovadas pelo usuario.
- Resolver primeiro problemas estruturais; polimento de palavras vem depois.
- Manter voz, pessoa, tempo verbal e nivel de linguagem.
- Se alterar o refrao, conferir como os versos o preparam.
- Manter a paridade silabica entre versos correspondentes ao editar um deles.
- Se houver album, checar `identity.md` antes de introduzir novos elementos.
- Quando a mudanca for ampla, explicar em uma frase o eixo da nova versao antes de reescrever.

## Comparar e salvar

Conferir se a versao nova melhora o alvo pedido sem apagar a personalidade anterior. Atualizar os arquivos correntes, validar e criar um novo snapshot com nota objetiva. Nunca substituir arquivo dentro de `versions/`.
