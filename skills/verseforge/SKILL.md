---
name: verseforge
description: Orquestrar criacao musical interativa para Suno, desde uma ideia vaga e a direcao criativa ate a letra final, o prompt de estilo e o salvamento do projeto. Usar quando o usuario quiser explorar, criar, desenvolver ou organizar uma musica, single, releitura, mashup, EP ou album, especialmente quando ainda nao souber qual caminho seguir ou quiser receber ideias, dicas e perguntas curtas.
---

# VerseForge

Conduzir a criacao como parceiro musical. Entender a intencao antes de escrever, reduzir atrito durante as perguntas e sempre terminar com uma letra cantavel, um estilo pronto para o Suno e os arquivos salvos.

## Iniciar

1. Ler `references/interaction-flow.md`.
2. Detectar se o trabalho e single avulso ou faixa de album.
3. Se for faixa de album existente, ler primeiro `projects/albums/<album>/identity.md`, `album.yaml` e `tracklist.md`.
4. Escolher e seguir a skill especializada:
   - ideia vaga, exploracao ou pedido de dicas: `$develop-music-concept`;
   - releitura de uma musica: `$reinterpret-song`;
   - combinacao de duas ou mais: `$mashup-songs`;
   - composicao do zero: `$write-original-song`;
   - melhoria de uma letra existente: `$refine-song`;
   - conceito, identidade ou sequenciamento de album: `$build-album`.
5. Aplicar `references/output-contract.md` e `references/project-storage.md` em qualquer fluxo.

## Conduzir a conversa

- Fazer de uma a tres perguntas por rodada. Perguntar primeiro apenas o que muda materialmente a composicao.
- Reutilizar tudo que o usuario ja informou; nunca repetir questionario respondido.
- Oferecer poucas opcoes concretas quando o usuario estiver indeciso, com uma recomendacao explicada em uma frase.
- Quando a ideia estiver aberta, nao tentar extrair todas as decisoes por perguntas. Usar `$develop-music-concept` para propor caminhos e ajudar o usuario a reagir a opcoes concretas.
- Confirmar um briefing curto antes de compor: objetivo, nucleo narrativo, genero, voz, energia, limites e destino do projeto.
- Tratar `masculina`, `feminina` ou `dueto` como escolha artistica. Em dueto, definir quem canta cada secao e onde as vozes se encontram.
- Nao forcar preferencias pessoais, autobiografia, linguagem urbana ou referencias modernas. Usar apenas o que for organico.
- Se o pedido ja estiver completo, evitar perguntas cerimoniais e criar diretamente.

## Salvar e versionar

- Criar a pasta antes da primeira versao usando `scripts/new_project.py`.
- Salvar cada fonte fornecida pelo usuario em `sources/`.
- Atualizar `brief.md`, `lyrics.md`, `suno-style.txt` e os metadados do projeto.
- Criar uma versao imutavel com `scripts/snapshot_version.py` a cada entrega aprovada ou revisao importante.
- Nunca sobrescrever silenciosamente uma versao anterior.

## Validar e entregar

Executar `scripts/validate_suno.py --lyrics <lyrics.md> --style <suno-style.txt>`. Se falhar, compactar e validar novamente. Nao alegar conformidade sem resultado `OK`.

Quando uma musica tiver sido efetivamente composta ou revisada, mostrar sempre:

1. `LETRA` com no maximo 5.000 caracteres;
2. `ESTILO PARA O SUNO` com no maximo 1.000 caracteres;
3. o caminho onde o projeto foi salvo e a versao criada.

Em uma rodada apenas de exploracao criativa, terminar com a recomendacao atual, as decisoes salvas e uma pergunta decisiva; nao inventar uma letra prematuramente.

Nao incluir nomes de artistas no estilo. Nao buscar nem reconstruir letras comerciais que o usuario nao forneceu; pedir que ele cole as fontes que deseja transformar.
