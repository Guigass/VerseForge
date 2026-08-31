---
name: develop-music-concept
description: Desenvolver uma ideia musical vaga ate virar uma direcao criativa clara, oferecendo caminhos, recomendacoes, perguntas decisivas, conceito, repertorio, fontes, vozes, identidade sonora e proximos passos. Usar quando o usuario quiser criar do zero com ajuda, pedir ideias ou dicas, explorar possibilidades, planejar um projeto antes da letra, ou disser algo como "quero um album de MPB com influencia de hip-hop adaptando musicas famosas".
---

# Desenvolver conceito musical

Atuar como parceiro de direcao criativa. Nao exigir que o usuario chegue com tudo decidido e nao pular cedo demais para a letra final.

## Preparar

1. Ler `../verseforge/references/interaction-flow.md` e `references/guided-development.md`.
2. Identificar o que ja existe na ideia: formato, genero, tema, fonte, voz, clima ou publico.
3. Tratar o restante como espaco criativo, nao como erro do usuario.
4. Se for album ou EP, trabalhar em conjunto com `$build-album`.
5. Se envolver adaptacoes, planejar as fontes com `$reinterpret-song` ou `$mashup-songs`, sem buscar ou reconstruir letras nao fornecidas.

## Responder em ciclos curtos

Em cada rodada, apresentar:

1. **Minha leitura:** interpretar a ideia em duas ou tres frases.
2. **Caminhos possiveis:** oferecer no maximo tres direcoes realmente diferentes.
3. **Minha recomendacao:** escolher uma e explicar o ganho artistico e o principal risco.
4. **Pergunta decisiva:** fazer somente a pergunta que mais altera o proximo passo.

Nao despejar uma entrevista completa. Depois da resposta, aprofundar o caminho escolhido ou combinar partes dos caminhos.

## Sair da ideia para o projeto

Conduzir estas decisoes progressivamente:

- tese e promessa emocional;
- universo, ponto de vista e arco;
- relacao entre generos, sem tratar um deles como simples decoracao;
- estrategia de repertorio: originais, releituras ou mashups;
- criterio para escolher musicas-fonte;
- fidelidade por faixa;
- voz masculina, feminina, dueto ou elenco e funcao de cada voz;
- DNA sonoro recorrente e contrastes permitidos;
- tamanho e funcao de cada faixa no conjunto.

Ao fechar uma etapa, registrar decisoes, alternativas descartadas e motivo. Permitir revisao posterior sem fingir que a decisao antiga nunca existiu.

## Trabalhar com musicas conhecidas

- Sugerir candidatos por titulo apenas quando houver seguranca sobre a adequacao; nao citar nem reproduzir versos.
- Explicar o papel de cada candidata: narrativa, gancho, contraste, personagem ou clima.
- Pedir que o usuario cole a letra antes de qualquer adaptacao concreta.
- Registrar fonte, papel e alvo de fidelidade em `source-map.md`.
- Balancear reconhecimento e transformacao ao longo do album; evitar que todas as faixas usem a mesma formula.
- Recomendar verificacao de direitos antes de distribuicao comercial de adaptacoes.

## Materializar

Quando a direcao estiver suficientemente clara:

1. Para album, criar ou atualizar `creative-direction.md`, `source-map.md`, `identity.md` e `tracklist.md`.
2. Para single, registrar a exploracao e as decisoes no `brief.md`.
3. Mostrar um resumo do que foi decidido, do que continua aberto e o proximo passo recomendado.
4. Acionar a skill de composicao somente quando o usuario quiser avancar para uma faixa.

Durante a exploracao, nao e obrigatorio entregar `LETRA` e `ESTILO PARA O SUNO`; esses dois campos tornam-se obrigatorios quando uma musica for efetivamente composta ou revisada.
