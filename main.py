import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


pipeline_options = PipelineOptions(
    temp_location='gs://Nracette/temp/',
    project="york-cdf-start",
    region="us-central1",
    staging_location="gs://Nracette/staging",
    job_name="nick-racette-capstone"
)

class TransformData(beam.DoFn):
    def process(self, element):
        print(element)
        yield element

def run():



    with beam.Pipeline(options=pipeline_options) as pipe:
        BQ_table1 = pipe | "read in " >> beam.io.ReadFromBigQuery(

        )

if __name__ == "__main__":
    run()
