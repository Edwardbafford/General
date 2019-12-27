# Creates a Dataproc cluster
# Scope - permissions
# Region, Zone - where hardware cluster exists
# Initialization actions for installations
# Hardware specifications
# Software versions

gcloud dataproc clusters create spark-etl --scopes=default --region "us-east1" --zone "us-east1-b" --initialization-actions=gs://dataproc-initialization-actions/jupyter/jupyter.sh  --master-machine-type n1-standard-1 --master-boot-disk-size 200 --num-workers 2 --worker-machine-type n1-standard-1 --worker-boot-disk-size 200 --image-version 1.3