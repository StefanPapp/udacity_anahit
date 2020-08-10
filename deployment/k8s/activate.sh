echo "executing kubectl apply -f aws-secret.yaml"
kubectl apply -f aws-secret.yaml
echo "executing kubectl apply -f backend-feed-deployment.yaml"
kubectl apply -f backend-feed-deployment.yaml
echo "executing kubectl apply -f backend-feed-service.yaml"
kubectl apply -f backend-feed-service.yaml
echo "executing kubectl apply -f backend-user-deployment.yaml"
kubectl apply -f backend-user-deployment.yaml
echo "executing kubectl apply -f backend-user-service.yaml"
kubectl apply -f backend-user-service.yaml
echo "executing kubectl apply -f frontend-deployment.yam"
kubectl apply -f frontend-deployment.yaml
echo "executing kubectl apply -f frontend-service.yaml"
kubectl apply -f frontend-service.yaml
echo "executing kubectl apply -f reverseproxy-deployment.yaml"
kubectl apply -f reverseproxy-deployment.yaml
echo "executing kubectl apply -f reverseproxy-service.yaml"
kubectl apply -f reverseproxy-service.yaml
