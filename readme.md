# Prediksi Resiko Stroke 
## TK 5 - Belgis Anggita
1. Clone repository ini
    ```bash
    git clone https://github.com/belgisanggita/stroke-prediction-biomedis.git
    cd stroke-prediction-biomedis
    ```
2. Install library yang dibutuhkan
    ```bash
    pip install -r requirements.txt
    ```

3. Jalanin aplikasinya
    ```bash
    python app.py
    ```

## Running dengan Docker
1. Build image nya
    ```bash
    docker build -t stroke-prediction:latest .
    ```
2. Jalani sebagai docker container
    ```bash
    docker run -d --name stroke-prediction -p 5050:5050 stroke-prediction:latest
    ```
