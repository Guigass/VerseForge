# Guia Suno (v6)

Base de conhecimento para transformar letra e direcao musical em uma geracao previsivel. Atualizado em 2026-09 para a familia v6. Tags e prompts de v5/v5.5 continuam validos no v6.

## Modelos

- **v6**: padrao para entrega. Preciso, obedece estilo e estrutura.
- **v6-wild**: exploracao; menos previsivel. Sugerir apenas quando o usuario quiser surpresa ou textura incomum.
- **v6-mini**: rapido e gratuito; bom para rascunho de melodia, pior em voz e mix.
- **Max Mode**: mais creditos; recomendado para faixas acima de 2 minutos, covers e consistencia vocal. Usar na geracao candidata a final, nao nos testes.

## Campos do modo avancado

| Campo | Limite | Uso |
|---|---:|---|
| Titulo | 80 | Nome da faixa; o gancho quando possivel. |
| Letra | 5.000 | Letra + tags de secao. Ponto ideal: 1.500–3.000 caracteres. |
| Estilo | 1.000 | Direcao sonora global, sempre positiva. Ponto ideal: 350–750. |
| Excluir | curto | O que o modelo tende a errar para esta faixa. 3–8 itens. |

## Controles

| Controle | Padrao VerseForge | Quando mudar |
|---|---|---|
| Weirdness | 30–45% | 15–25% para genero tradicional e releitura fiel; 55–70% para fusao experimental. |
| Style Influence | 65–80% | 85%+ quando o estilo e preciso e o Suno esta desviando; 45–55% para deixar o modelo propor. |
| Variety | 0 | Aumentar so para pedir ao Suno variacoes do prompt; acima de 0 ele reescreve o estilo. |
| Audio Influence | 50–70% | Apenas com audio enviado ou cover. |

Registrar os valores escolhidos em `project.yaml` e no bloco `CONFIGURACOES` da entrega.

## Estilo: como escrever

1. **Escrever em ingles.** Os descritores do Suno sao mais bem entendidos em ingles. A letra continua no idioma da musica.
2. **Genero principal primeiro.** A primeira expressao pesa mais. Genero principal, depois subgenero ou fusao.
3. **Ordem recomendada:** genero e fusao → BPM e groove → instrumentos-chave (2–4) → voz (genero, timbre, entrega, idioma) → clima/energia → arco de dinamica → producao/mix.
4. **Idioma da voz:** incluir `Brazilian Portuguese vocals` (ou o idioma/sotaque correto). Isso melhora pronuncia e sotaque.
5. **8–15 descritores fortes.** Menos que isso deixa o modelo no padrao; mais que isso gera contradicao e som embolado.
6. **Somente afirmacoes positivas.** Nada de `no trap`, `without EDM`, `evitar sax`. Nomear o que se quer evitar pode puxar justamente aquilo. Tudo que for negativo vai para **Excluir**.
7. **Sem nomes de artistas, bandas, produtores ou musicas.** Descrever a impressao digital: epoca, instrumentacao, tecnica de gravacao, timbre e entrega.
8. **Prosa compacta ou lista com virgulas.** No v6, frases curtas descrevendo o arco funcionam bem ("sparse verses, full band on the chorus, stripped bridge"). Nao contar a historia da letra.
9. **Nao contradizer:** "lo-fi" com "crisp modern mix", "aggressive" com "calm", 70 BPM com "high energy dance".
10. **Coerencia com a letra:** clima, densidade silabica e energia do estilo precisam combinar com a letra; um verso muito denso em estilo lento fica corrido.

### Modelo

```text
<Genero principal> with <fusao/influencia>, <BPM> BPM, <groove>. <Instrumento 1>, <instrumento 2>, <instrumento 3>. <Genero da voz> <timbre> vocals in Brazilian Portuguese, <entrega>. <Clima>. <Arco: verses X, chorus Y, bridge Z>. <Producao/mix>.
```

### Exemplo (ruim → bom)

Ruim (prosa em PT, com negativos):

> Hip-hop boom-bap com jazz, 90 BPM. [...] Evitar trap, drop de EDM e nomes de artistas.

Bom:

> Jazz boom-bap hip-hop, 90 BPM, laid-back swung groove. Dusty drums with dry snare and heavy kick, deep round upright bass, warm tenor sax hooks answering the vocal, muted trumpet and Rhodes underneath. Confident male rap vocals in Brazilian Portuguese, relaxed pocket flow, group chant on the chorus. Celebratory and defiant. Sparse verses, full horns on the chorus, spiritual sax-led bridge with choir pads. Vinyl warmth, wide drums, bass-forward mix, clear vocals.
>
> Excluir: trap hi-hats, 808, EDM drop, autotune

## Excluir: como escrever

- Listar o desvio **mais provavel** para aquela combinacao, nao uma lista infinita de proibicoes.
- Itens curtos em ingles, separados por virgula: `autotune, trap hi-hats, EDM drop, spoken intro`.
- Nunca repetir no Excluir algo que esteja no Estilo.
- Desvios comuns: genero vizinho (reggae → `dancehall`; boom-bap → `trap`), instrumento generico (`acoustic strumming`), producao (`autotune`, `lo-fi`), voz errada (`female vocals` em faixa masculina).

## Letra: formatacao

### Tags de secao (em ingles)

Usar sempre as tags em ingles, uma por linha, sozinha, com uma linha em branco antes de cada secao:

`[Intro]` `[Verse 1]` `[Verse 2]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Hook]` `[Bridge]` `[Breakdown]` `[Build-Up]` `[Drop]` `[Interlude]` `[Instrumental Break]` `[Outro]` `[End]`

Solos e instrumentais: `[Guitar Solo]` `[Sax Solo]` `[Piano Solo]` `[Drum Break]` `[Percussion Break]` `[Instrumental]`.

Tags em portugues (`[Verso]`, `[Refrão]`, `[Ponte]`) sao menos confiaveis e podem ser cantadas.

### Uma tag por secao, com modificador

Combinar funcao, voz e direcao local em **uma unica tag**, em vez de empilhar varias linhas de tags:

```text
[Intro: tenor sax, soft drums]
[Verse 1: male rap, laid-back]
[Chorus: male vocal and group chant]
[Bridge: drums drop out, whispered female vocal]
[Outro: fade out]
[End]
```

Regras:

- Modificador curto (ate ~6 palavras), em ingles.
- Usar modificadores apenas onde a secao precisa **mudar** algo em relacao ao estilo global; nao repetir o estilo em toda tag.
- `[End]` depois do outro evita que o Suno invente mais musica.

### Parenteses = vozes de apoio

Tudo entre `( )` e **cantado** como backing vocal, eco ou ad-lib: `(oh-oh)`, `(vem, vem)`, `(tamo no som)`.

- Nunca usar parenteses para instrucoes (`(sussurrado)`, `(2x)`, `(solo de sax)`).
- Instrucoes vao em colchetes.

### Linhas e secoes

- 4–10 palavras por linha; linhas longas fazem o Suno correr ou quebrar a frase.
- Versos ate 8 linhas; refrao 2–6 linhas; ponte 2–4 linhas.
- **Paridade silabica:** linhas correspondentes entre Verso 1 e Verso 2 devem ter contagem de silabas parecida (±2). O Suno reaproveita a melodia do verso; se a metrica mudar, a melodia quebra.
- Escrever as repeticoes por extenso. Nunca `(x2)`, `2x`, `bis` ou `repete`.
- Tamanho total: 150–350 palavras para 3–4 minutos. Rap denso pode chegar a ~450. Acima disso o Suno corta ou atropela.
- MAIUSCULAS podem gerar entrega mais intensa; usar raramente e com intencao.
- Pontuacao guia respiracao: virgula = micro-pausa; reticencias = sustentacao.
- Vocalizes escritos como se cantam: `oh-oh-oh`, `lalaia`, `uô-uô`, `hey!`.

### Estrutura padrao por duracao

- **2:30–3:00:** Intro curta, Verso 1, Refrao, Verso 2, Refrao, Ponte, Refrao, Outro.
- **3:30–4:00:** acrescentar Pre-Refrao ou um solo/instrumental.
- Evitar mais de 12 secoes em uma geracao; usar **Extend** ou edicao de secao para faixas longas.

## Vozes e duetos

Voz solo:

- Definir a voz no Estilo (`warm female alto vocals in Brazilian Portuguese, intimate, close-mic`).
- Tags de secao so mudam a voz quando necessario.

Dueto:

1. Definir as duas vozes **no Estilo**, uma frase cada: `Duet: male baritone, calm and grounded; female alto, airy, slightly behind the beat.`
2. Declarar a regra de distribuicao no Estilo: `each verse sung by one singer alone, chorus together in harmony`.
3. Marcar cada secao: `[Verse 1: Male Vocal]`, `[Verse 2: Female Vocal]`, `[Chorus: Duet, harmony]`, `[Bridge: call and response]`.
4. Troca linha a linha: prefixar a linha com o papel, mantendo a linha curta (ate ~6 silabas por troca):

```text
[Bridge: call and response]
[Male Vocal] Onde voce tava?
[Female Vocal] Tava te esperando
```

5. Evitar letras diferentes cantadas ao mesmo tempo; o Suno ainda erra contracanto com palavras distintas.
6. Com a funcao Voices (voz salva do usuario), usar a voz salva no papel principal e descrever a segunda voz no Estilo.

Coro: `[Chorus: group chant]`, `[Choir]`, ou backing em parenteses.

## Portugues do Brasil: pronuncia

- Declarar `Brazilian Portuguese vocals` no Estilo; opcionalmente o sotaque (`carioca accent`, `northeastern Brazilian accent`) quando fizer parte da identidade.
- Manter acentos graficos (`coração`, `você`, `pé`): eles orientam a tonicidade.
- Numeros por extenso: `dois mil e vinte`, nao `2020`.
- Siglas soletradas com pontos ou hifens: `D.J.`, `M-P-B`.
- Palavras estrangeiras que devem soar abrasileiradas: escrever como se fala (`rip-rópi`, `fãn-qui`) apenas se o teste falhar.
- Contracoes da fala (`tô`, `pra`, `cê`, `tamo`) funcionam e deixam a entrega natural; manter a mesma grafia em toda a letra.
- Evitar encontros de vogais ambiguos no fim de frase longa; quebrar a linha ou trocar a palavra.
- Um idioma por secao em faixas bilingues; declarar no Estilo (`Portuguese verses, English chorus`).

## Fluxo de geracao recomendado

1. Gerar 2–4 vezes com v6 (sem Max Mode) e a configuracao registrada.
2. Escolher a melhor base pelo **refrao e voz**, nao pela mix.
3. Consertar partes com **edicao de secao** ou troca de palavras/linhas em linguagem natural, em vez de regenerar tudo.
4. Usar **Extend** a partir da versao mais recente para faixas longas.
5. Usar **Persona** ou **Voices** para manter a mesma voz entre faixas de um album.
6. Gerar a versao final com Max Mode quando a faixa passar de 2 minutos.

## Problemas comuns

| Sintoma | Causa provavel | Correcao |
|---|---|---|
| Genero errado domina | genero secundario primeiro; Style Influence baixo | reordenar; subir Style Influence; genero vizinho no Excluir |
| Tag cantada como letra | tag fora do padrao ou em portugues | tag em ingles, sozinha na linha, com colchetes |
| Instrucao cantada | instrucao em parenteses | mover para colchetes |
| Letra atropelada | linhas longas; letra grande; BPM alto e letra densa | encurtar linhas; cortar secoes; ajustar BPM |
| Melodia do Verso 2 quebra | metrica diferente do Verso 1 | igualar silabas das linhas correspondentes |
| Musica nao termina ou continua sozinha | sem `[Outro]`/`[End]` | adicionar `[Outro]` e `[End]` |
| Final abrupto | outro sem indicacao | `[Outro: fade out]` ou `[Outro: final chord ring out]` |
| Voz errada no dueto | papeis so na letra; linhas trocadas longas | definir vozes no Estilo; tag por secao; linhas curtas |
| Pronuncia errada | numero, sigla, estrangeirismo, homografo | escrever por extenso ou foneticamente |
| Instrumento indesejado | estilo aberto ou mencionado em negativo | tirar o negativo do Estilo; incluir no Excluir |
| Resultado generico | poucos descritores; so adjetivos | trocar adjetivos por instrumentos, groove e tecnica |
| Resultado embolado | muitos descritores conflitantes | reduzir para 8–12; remover contradicoes |
