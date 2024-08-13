# Sandman: Backend do Classificador
Este projeto tem como objetivo o desenvolvimento do backend do classificador para o projeto Sandman, que está sendo realizado na disciplina de Engenharia de Software.

## 0 - Informações técnicas:
- O pacote utilizado para o desenvolvimento do classificador será o scikit-learn
- O pacote utilizado para a plotagem de imagens é o matplotlib em conjunto com o seaborn

## 1 - Rotas de acesso:
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
