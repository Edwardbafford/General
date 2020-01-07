1. Create DataProc cluster with MySQL permissions and Sqoop dependencies, then we can use the gcloud commands to execute Sqoop actions as needed  
  
The DataProc cluster is just a regular cluster but we can use Sqoop to import data from MySQL before using the cluster as the processing agent  
  
2. Eval -- imports data from MySQL then executes a query using the cluster.. could also execute any kind of spark job as well  
3. Import -- uses parallel mappers to move data from MySQL to a bucket, faster than moving in series
