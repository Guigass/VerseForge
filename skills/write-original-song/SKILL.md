---
name: write-original-song
description: Compor letra musical original e prompt de estilo pronto para o Suno por meio de descoberta interativa, conceito, gancho, estrutura, prosodia, voz e producao. Usar quando o usuario quiser criar uma musica nova do zero, desenvolver uma ideia, cena, titulo, refrão ou conceito sem depender de uma obra-base.
---

# Compor musica original

Criar uma canção especifica, humana e memoravel, evitando texto generico que apenas descreve uma emocao.

## Descobrir

1. Ler `../verseforge/references/interaction-flow.md`, `../verseforge/references/output-contract.md`, `../verseforge/references/suno-guide.md` e `../verseforge/references/project-storage.md`.
2. Obter ou propor: nucleo da musica, cena concreta, curva emocional, genero, voz e destino single/album.
3. Escolher um ponto de vista e um tempo verbal consistentes.
4. Definir uma frase-ima, uma imagem central e algo que a musica deliberadamente evita.

## Projetar

Antes da letra completa, formar internamente:

- premissa em uma frase;
- transformacao entre inicio e fim;
- funcao de cada secao e duracao alvo (ver estruturas em `suno-guide.md`);
- gancho principal e onde ele aparece pela primeira vez (idealmente antes de 0:45);
- paleta de palavras e imagens;
- desenho vocal, inclusive papeis no dueto;
- arco de energia, que vira a frase de dinamica do estilo ("sparse verses, lifted chorus, stripped bridge").

## Escrever

- Abrir com acao, imagem ou voz; evitar introducao abstrata previsivel.
- Fazer cada verso mover a historia, a ideia ou a tensao; o Verso 2 deve avancar, nao repetir o Verso 1 com outras palavras.
- Construir refrao simples o bastante para lembrar e especifico o bastante para pertencer apenas a esta musica. O titulo deve aparecer no refrao, de preferencia na primeira ou ultima linha.
- Refrao com 2–6 linhas e vogais abertas nas notas longas (`a`, `o`, `e`); evitar terminar frase sustentada em consoante dura ou em palavra atona.
- Respeitar a tonicidade do portugues: a silaba forte da palavra deve cair no tempo forte da frase. Evitar deslocar acento para rimar (`amôr` → `ámor`).
- Linhas de 4–10 palavras; linhas correspondentes entre versos com silabas equivalentes (±2) para que a melodia se repita.
- Usar rimas internas, repeticoes e pausas conforme o genero, sem sacrificar fala natural. Rima nao pode depender de inversao sintatica.
- Variar comprimento das linhas com intencao performatica: pre-refrao encurta e acelera; refrao abre.
- Inserir nuances pessoais somente quando reforcarem a cena.
- Dar a ponte uma descoberta, inversao ou mudanca de perspectiva, com textura diferente marcada na tag (`[Bridge: stripped, half-time]`).
- Evitar cliches de IA: `neon`, `ecos`, `alma em chamas`, `sussurros do vento`, `dancar na chuva`, `coracao partido em mil pedacos`, `a noite e uma crianca`, salvo se forem subvertidos com intencao.

## Revisar e salvar

Fazer uma leitura em voz alta mental: cortar inversoes, palavras de enchimento e rimas que so funcionam no papel. Substituir pelo menos uma abstracao generica por detalhe sensorial quando necessario. Confirmar que titulo, gancho e final pertencem ao mesmo nucleo. Contar silabas das linhas correspondentes dos versos.

Escrever o estilo e o excluir conforme o contrato, rodar o validador e versionar conforme `$verseforge`.
