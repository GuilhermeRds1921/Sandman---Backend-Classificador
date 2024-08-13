# Sandman: Backend do Classificador
Backend do classificador do projeto Sandman da disciplina de Engenharia de Software

## Rotas de acesso:
1. Enviar exame:
  - Link: /classifier/exam
  - Método: POST
  - Request Body:
    - eeg_reading: array<float>
  - Response Body:
    - queue_id: UUID 
2. Checar se classificação foi concluida / Retornar exame:
  - Link: /classifier/exam/<queue_id: UUID>
  - Método: GET
  - Response Body:
    - done: bool 
    - classified_eeg_reading: array<int>
    - eeg_reading_plot: Base64
    - classified_eeg_reading_plot: Base64
    - sleep_stages_distribution_plot: Base64
Obs: Todos os Base64 neste projeto são conversões de imagens PNG para strings.
