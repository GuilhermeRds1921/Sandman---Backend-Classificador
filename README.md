# Sandman: Backend do Classificador
Backend do classificador do projeto Sandman da disciplina de Engenharia de Software

## Rotas de acesso:
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
