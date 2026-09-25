# Armazenamento de projetos

## Single

```text
projects/singles/<slug>/
  project.yaml
  brief.md
  lyrics.md
  suno-style.txt
  suno-exclude.txt
  sources/
  versions/v001.md
```

## Album

```text
projects/albums/<slug>/
  album.yaml
  creative-direction.md
  identity.md
  source-map.md
  tracklist.md
  songs/01-<slug>/
    project.yaml
    brief.md
    lyrics.md
    suno-style.txt
    suno-exclude.txt
    sources/
    versions/v001.md
```

## Regras

- Usar slugs estaveis em minusculas; nao renomear pastas apos criar sem pedido explicito.
- Guardar texto-fonte do usuario em `sources/`, com origem descrita no `brief.md`.
- Tratar `lyrics.md`, `suno-style.txt`, `suno-exclude.txt` e o bloco `suno:` do `project.yaml` como a versao de trabalho atual.
- Tratar `versions/` como historico imutavel.
- Atualizar `tracklist.md` ao criar, renomear ou mudar a ordem de uma faixa.
- Atualizar `creative-direction.md` ao confirmar ou descartar uma direcao artistica.
- Manter em `source-map.md` apenas metadados e criterios ate o usuario fornecer as letras; salvar cada letra recebida na pasta `sources/` da faixa correspondente.
- Ler `identity.md` antes de qualquer nova faixa de album e registrar no briefing como a faixa preserva e expande a identidade.
- Nao salvar letras obtidas de fontes externas sem permissao clara; nao buscar letra comercial pelo titulo.
