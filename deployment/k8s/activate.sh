echo "executing kubectl apply -f aws-secret.yaml"
kubectl apply -f aws-secret.yaml

#  entitydetector
echo "executing kubectl apply -f entitydetector-deployment.yaml"
kubectl apply -f entitydetector-deployment.yaml

echo "executing kubectl apply -f entitydetector-service.yaml"
kubectl apply -f entitydetector-service.yaml

# sentimentsanalyzer
echo "executing kubectl apply -f sentimentsanalyzer-deployment.yaml"
kubectl apply -f sentimentsanalyzer-deployment.yaml

echo "executing kubectl apply -f sentimentsanalyzer-service.yaml"
kubectl apply -f sentimentsanalyzer-service.yaml
