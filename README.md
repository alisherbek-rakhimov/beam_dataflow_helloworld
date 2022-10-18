#### System requirements - python SDK chosen

- Python `3.8.*`.
- apache-beam[gcp] 2.14.0

#### In case you need to run the job on Dataflow please consider first configuring your GCP environment

[Create a Dataflow pipeline using Python](https://cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python)

**Here is sample, make sure you will replace `PROJECT_ID`, `STORAGE_BUCKET` and `DATAFLOW_REGION` with your own as shown
in**

```shell
python3 main.py \
  --region us-central1 \
  --input gs://dataflow-bucket-1997/my_data/a.txt \
  --output gs://dataflow-bucket-1997/results/output \
  --runner DataflowRunner \
  --project dataflow-project-1997 \
  --temp_location gs://dataflow-bucket-1997/temp/
```

#### For local testing we can use DirectRunner with local file input and outputs andd we can see lowecase letters in `b.txt`

```shell
pip install "apache-beam[gcp]"
echo 'MY NAME IS THOMAS SHELBY' > a.txt
python3 main.py --input a.txt --output b.txt
```

#### For the case you could not get your env ready you can try DirectRunner in Docker container and configure .env file under your needs and do not forget to check outputs folder

```shell
docker-compose up --build -d
``` 