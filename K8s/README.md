## K8s Exposed Service  
kubectl create -f node-replicaset.yaml  
kubectl create -f node-svc-loadbalancer.yaml  
kubectl create -f node-ingress.yaml  
Update C:\Windows\System32\drivers\etc\hosts file with ingress ip and url or use loadbalancer ip to make request to node-app application 
  
## K8s Persistent Volume  
gcloud compute disks create --size=1GiB --zone=us-central1-a mongodb  
kubectl create -f storageclass-fast-gcepd.yaml  
kubectl create -f mongodb-pvc-dp.yaml  
kubectl create -f mongodb-pod-pvc.yaml  
kubectl exec -it mongodb mongo  
Work with mongdb command line  