# Sandman: Backend do Classificador
Este projeto tem como objetivo o desenvolvimento do backend do classificador para o projeto Sandman, que está sendo realizado na disciplina de Engenharia de Software.

## Indice
1. [O sono](#0---o-sono)
   1. [Awake](#1---awake)
   2. [NREM](#2---nrem)
      1. [N1](#21---n1)
      2. [N2](#22---n2)
      3. [N3](#23---n3)
   3. [REM](#3---rem)
2. [Informações técnicas](#1---informações-técnicas)
3. [Rotas de acesso](#2---rotas-de-acesso)
   1. [Enviar exame](#21---enviar-exame)
   2. [Checar se classificação foi concluída / Retornar exame](#22---checar-se-classificação-foi-concluída--retornar-exame)
   3. [Gerar laudo](#23---gerar-laudo)
4. [Instruções](#3---instruções)
   1. [Inicializando o projeto](#31---inicializando-o-projeto)
   2. [Salvando requisitos](#32---salvando-requisitos)

## 0 - O sono:
Informação retirada de [The Functions of Sleep](http://www.aimspress.com/article/10.3934/Neuroscience.2015.3.155), acessado em 18/04/2024
1. **Awake**: indivíduo está completamente alerta e responsivo ao ambiente. 
    - Atividade do EEG: atividade elétrica rápida e irregular em um EEG
2. **NREM**
    1. *N1*: transição entre a vigília e o sono. É uma fase de sono leve que dura apenas alguns minutos
        - Atividade do EEG: ondas cerebrais diminuem e pode haver ondas teta presentes
        - Funções: pode ajudar o corpo a relaxar e se preparar para estágios mais profundos do sono
    2. *N2*: compõe uma parte significativa do tempo total de sono. É um sono mais profundo do que o NREM 1, mas não tão profundo quanto o NREM 3
        - Atividade do EEG: ondas cerebrais incluem sleep spindles e K-complexes
        - Funções: consolidação da memória, processamento de informações e preparação para o sono profundo
    3. *N3*: fase mais profunda do sono NREM, também conhecida como sono de ondas lentas (SWS). É mais difícil acordar alguém durante esta fase
        - Atividade do EEG: ondas cerebrais são lentas (ondas delta) e sincronizadas.
        - Funções: restauração física, crescimento e reparo, bem como função imunológica e saúde geral</br>
    Obs: N3 e N4 estão separados no dataset, mas atualmente todas pesquisas consideram N3 e N4 como sendo apenas o estágio N3, segundo [Normal Human Sleep: An Overview. Principles and Practice of Sleep Medicine](https://www.researchgate.net/publication/287231408_Normal_Human_Sleep_An_Overview_Principles_and_Practice_of_Sleep_Medicine_MH_Kryger_Ed)
3. **REM**: caracterizado por movimentos rápidos dos olhos, paralisia muscular e sonhos vívidos
    - Atividade do EEG: ondas cerebrais são semelhantes à Awake, e há aumento da atividade neuronal.
    - Funções: crucial para a função cognitiva, regulação emocional, consolidação da memória e aprendizado

## 1 - Informações técnicas:
- O pacote utilizado para o desenvolvimento do classificador será o scikit-learn
- O pacote utilizado para a plotagem de imagens é o matplotlib em conjunto com o seaborn

## 2 - Rotas de acesso:
1. Enviar exame:
    - Link: /classifier/exam
    - Método: POST
    - Request Body:
      - eeg_reading: array<float>
    - Response Body:
      - job_id: UUID 
2. Checar se classificação foi concluida / Retornar exame:
    - Link: /classifier/exam/<job_id: UUID>
    - Método: GET
    - Response Body:
      - done: bool 
      - classified_eeg_reading: array<int>
      - eeg_reading_plot: Base64 (PNG) 
      - classified_eeg_reading_plot: Base64 (PNG)
      - sleep_stages_distribution_plot: Base64 (PNG)
3. Gerar laudo:
    - Link: /classifier/generate_report
    - Método: POST
    - Request Body:
      - job_id: UUID
      - notes: string
    - Response Body:
      - report_pdf: Base64 (PDF)

## 3 - Instruções:
### 3.1 - Inicializando o projeto: 
1. Download do repositório: ```https://github.com/NailsonChagas/Sandman---Backend-Classificador.git```
2. Acesse o repositório: ```cd Sandman---Backend-Classificador```
3. Criar ambiente virtual: ```python3 -m venv venv```
4. Abrir ambiente virtual: ```source ./venv/bin/activate```
5. Instalar requisitos: ```pip install -r requirements.txt```

### 3.2 - Salvando requisitos:
1. Salvar requisitos: ```pip freeze > requirements.txt```
2. Adicionar mudança: ```git add requirements.txt```
3. Fazer commit: ```git commit -m "update: atualizando requisitos"```
4. Subir para o repositório: ```git push -u origin main```
