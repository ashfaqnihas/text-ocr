import os, io
import re
from google.cloud import vision
from google.cloud import storage
from google.protobuf import json_format

""" 
# pip install --upgrade google-cloud-storage
"""
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'My First Project-e34e49d05fd7.json'
client = vision.ImageAnnotatorClient()

batch_size = 2
mime_type = 'application/pdf'
feature = vision.types.Feature(
    type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)
#-------------------------------------------------------------------------------------------------
# for file in fileNames:
gcs_source_uri = 'gs://cess/part1.pdf'
gcs_source = vision.types.GcsSource(uri=gcs_source_uri)
input_config = vision.types.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

gcs_destination_uri = 'gs://cess/part1.out'
gcs_destination = vision.types.GcsDestination(uri=gcs_destination_uri)
output_config = vision.types.OutputConfig(gcs_destination=gcs_destination, batch_size=batch_size)

async_request = vision.types.AsyncAnnotateFileRequest(
    features=[feature], input_config=input_config, output_config=output_config)

operation = client.async_batch_annotate_files(requests=[async_request])
operation.result(timeout=18000)

storage_client = storage.Client()
match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
bucket_name = match.group(1)
prefix = match.group(2)
bucket = storage_client.get_bucket(bucket_name)

# List object with the given prefix
blob_list = list(bucket.list_blobs(prefix=prefix))


namelist = list(map(lambda x: x.name, blob_list))


# newSortedList=sorted_nicely(blob_list)
blob_list.sort(key=lambda x: int(re.match(r'.+-(\d+)-.+', x.name).group(1)))

print('Output files:')

with open( 'output.txt', 'w', encoding='utf8') as f:
    for item in blob_list:
        json_string = item.download_as_string()
        response = json_format.Parse(json_string, vision.types.AnnotateFileResponse())
        for singlePageResponse in response.responses:
            f.write(singlePageResponse.full_text_annotation.text)




#-------------------------------------------------------------------------------------------------
