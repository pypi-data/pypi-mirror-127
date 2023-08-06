# PyS3 Tower :building_construction:


## Introduction

PyS3 Tower *(like the Pisa Tower)* is a Python library that can sync your local files to a S3 bucket. With PyS3 Tower you can easily sync your local files to a S3 bucket and also sync your S3 bucket to your local files.

This script work like xcopy on Windows. But it is more powerful, flexible and adapted to the needs of the S3 bucket.

\> PyS3 Tower work with the following rules:
- If a file is in the S3 bucket and not in the local folder, it will be deleted on the bucket,
- If a file is in the local folder and not in the S3 bucket, it will be uploaded to the bucket,
- If a file is in both the local and the S3 bucket, the local file will be updated on the bucket if it is different from the local file.


## Installation

    pip install pys3tower


## Usage

Import the PyS3 Tower library:

    import pys3tower

And create a PyS3 Tower object with your local file path, your S3 bucket name and your access key, secret key and region:

    pys3tower = pys3tower.PyS3Tower(local_path, s3_bucket_name, access_key, secret_key, region)

Then, run the pysetower.run() method:

    pys3tower.run()

Or you can use the CLI *(with the /example_scripts/pys3_tower_cli.py)* :

