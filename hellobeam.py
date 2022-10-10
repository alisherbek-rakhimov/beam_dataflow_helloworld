import argparse

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()

beam_options = PipelineOptions(
    beam_args,
    runner='DataflowRunner',
    # input='gs://dataflow-bucket-1997/my_data/text.txt',
    project='dataflow-project-1997',
    job_name='my-first-dataflow-job',
    temp_location='gs://dataflow-bucket-1997/temp/',
    # output='gs://dataflow-bucket-1997/results/output',
    region='us-central1'
)




with beam.Pipeline(options=beam_options) as pipeline:
    lines = pipeline | 'Read' >> ReadFromText('gs://dataflow-bucket-1997/my_data/text.txt')
    lines | 'Write' >> WriteToText('gs://dataflow-bucket-1997/results/output.txt')
