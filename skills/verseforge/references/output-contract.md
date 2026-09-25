# Contrato de saida Suno

Ler `suno-guide.md` antes de escrever letra ou estilo. Consultar `style-vocabulary.md` ao montar o estilo.

## Arquivos

| Arquivo | Conteudo |
|---|---|
| `lyrics.md` | somente a letra, pronta para colar no campo Letra |
| `suno-style.txt` | somente o estilo, pronto para colar no campo Estilo |
| `suno-exclude.txt` | somente os itens do Excluir, separados por virgula |
| `project.yaml` | titulo, voz e bloco `suno:` com modelo e controles |

## Letra

- Limite absoluto: 5.000 caracteres. Meta: 1.500–3.000; acima de 3.500 so com justificativa (rap denso, faixa longa).
- Tags de secao em ingles, uma por linha, com linha em branco entre secoes: `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]`, `[End]`.
- Direcao local e voz dentro da mesma tag: `[Verse 2: Female Vocal, softer]`. Nao empilhar tags em linhas seguidas.
- Parenteses apenas para backing vocals e ad-libs que devem ser cantados.
- Repeticoes escritas por extenso; nunca `(x2)`, `2x` ou `bis`.
- Numeros por extenso; siglas soletradas.
- Terminar com `[Outro]` e `[End]`.
- Nenhuma explicacao, comentario ou titulo dentro do arquivo.

## Estilo

- Limite absoluto: 1.000 caracteres. Meta: 350–750.
- Em ingles, genero principal primeiro, 8–15 descritores fortes.
- Declarar a voz e o idioma (`Brazilian Portuguese vocals`). Em dueto, descrever as duas vozes e a regra de distribuicao.
- Somente afirmacoes positivas; negativos vao para `suno-exclude.txt`.
- Nunca usar nomes de artistas, bandas, produtores ou musicas.
- Nao narrar a historia da letra.

## Excluir

- 3–8 itens curtos em ingles, separados por virgula.
- Mirar os desvios mais provaveis desta faixa.
- Nunca incluir algo que esteja no Estilo.

## Configuracoes

Registrar em `project.yaml`:

```yaml
suno:
  model: "v6"
  weirdness: 35
  style_influence: 70
  variety: 0
  max_mode: false
```

Usar as faixas de `suno-guide.md`. Justificar em uma frase quando fugir do padrao.

## Entrega ao usuario

Quando uma musica for composta ou revisada, mostrar nesta ordem, cada campo em bloco de codigo para copiar:

1. `TITULO`
2. `LETRA`
3. `ESTILO PARA O SUNO`
4. `EXCLUIR`
5. `CONFIGURACOES`: modelo, Weirdness, Style Influence, Variety, Max Mode
6. `DICAS DE GERACAO`: no maximo tres, especificas desta faixa (ex.: "se o refrao vier sem coro, editar so o refrao pedindo group chant")
7. caminho salvo e versao criada

## Controle final

Validar com `validate_suno.py --project <pasta>`. Uma contagem estimada visualmente nao e suficiente. Corrigir erros; resolver ou justificar cada aviso antes de entregar.
