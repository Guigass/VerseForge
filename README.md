# VerseForge

VerseForge e uma oficina musical interativa para criar letras e prompts de estilo prontos para o Suno. O agente entende a ideia em etapas, compoe, revisa, valida os limites e salva todo o trabalho no repositorio.

## Modos de criacao

- **Releitura:** transforma uma letra fornecida com fidelidade de 0 a 100.
- **Mashup:** combina duas ou mais letras, com peso e papel definidos para cada fonte.
- **Original:** desenvolve uma musica do zero a partir de uma ideia, cena ou emocao.
- **Oficina:** diagnostica e melhora uma letra existente sem apagar sua identidade.
- **Album/EP:** define uma identidade comum e mantem coerencia entre todas as faixas.
- **Direcao criativa:** parte de uma ideia vaga, apresenta caminhos, recomenda escolhas e desenvolve o projeto junto com voce antes da composicao.

Todos os modos aceitam voz masculina, feminina ou dueto. No dueto, o agente tambem define o papel de cada voz e marca as secoes da letra.

## Como usar

Inicie com algo simples, por exemplo:

> Quero criar uma musica original para um album novo. Quero um dueto e uma atmosfera noturna.

ou:

> Quero uma releitura desta letra com 70% de fidelidade, transformada em jazz rap com dub.

A skill `verseforge` conduz as perguntas que realmente alteram o resultado. Se o pedido ja estiver completo, ela cria diretamente.

Quando a ideia ainda estiver aberta, o agente nao responde com um questionario enorme. Ele apresenta ate tres caminhos criativos, recomenda um deles, explica o principal ganho e risco e faz uma pergunta decisiva. As escolhas ficam salvas para a proxima conversa.

Por exemplo, em um album de MPB com influencia de hip-hop baseado em musicas conhecidas, o agente pode ajudar a definir:

- se o album sera narrativo, tematico ou um dialogo entre epocas e vozes;
- como harmonia, instrumentos e narrativa de MPB encontram bateria, baixo, samples e flow de hip-hop;
- quais perfis de musicas-fonte servem para cada momento do arco;
- a fidelidade e a transformacao de cada releitura;
- quando usar voz masculina, feminina ou dueto;
- quais letras voce precisa fornecer antes da adaptacao.

## Onde o trabalho fica salvo

```text
projects/
  singles/<musica>/
  albums/<album>/
    creative-direction.md
    identity.md
    source-map.md
    tracklist.md
    songs/<faixa>/
```

Cada musica guarda briefing, letra atual, estilo do Suno, fontes fornecidas e versoes anteriores. Cada album possui um contrato de identidade lido antes da criacao de novas faixas.

## Limites garantidos

- Letra: maximo absoluto de 5.000 caracteres.
- Estilo do Suno: maximo absoluto de 1.000 caracteres.

O validador em `skills/verseforge/scripts/validate_suno.py` confere os dois limites antes da entrega.
