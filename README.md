# **LOBERTA TEST TASK**
# 
---
Prequisites: install [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), [Kind](https://kind.sigs.k8s.io/docs/user/quick-start), [Docker](https://docs.docker.com/engine/install/ubuntu/), [Helm](https://helm.sh/docs/intro/install/)  and [python3](https://www.python.org/downloads/)

**# Task 1**
Kind is a lightweight solution for running kubernetes in Docker. To create cluster, copy this [file](https://github.com/urbeingwatched8/loberta_test_task/blob/main/kind_create_cluster.yaml) and use command
```
kind create cluster --config=kind_create_cluster.yaml
```
To create an ingress resource using Helm and Terraform, use this [file](https://github.com/urbeingwatched8/loberta_test_task/blob/main/ingress_nginx.tf) with [extra](https://github.com/urbeingwatched8/loberta_test_task/blob/main/versions.tf) [settings](https://github.com/urbeingwatched8/loberta_test_task/blob/main/nginx_vals.yaml) and run commands
```
terraform init
terraform plan
terraform apply
```
Settings for the new Service, Deployment and ports are specified [here](https://github.com/urbeingwatched8/loberta_test_task/blob/main/app/usage.yaml)
To apply, run
```
kubectl apply -f usage.yaml
```

To check the website, you can run 
```
curl  -kL http://localhost/
```
You should get My Test Site(base) without errors.

**# Task 2**
To install ArgoCD, run
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
To set up ArgoCD, create [ingress](https://github.com/urbeingwatched8/loberta_test_task/blob/main/argocd_ingress.yaml) and specify [configs](https://github.com/urbeingwatched8/loberta_test_task/blob/main/argocd.yaml)
Command to run:
```
kubectl apply -f argocd_ingress.yaml
```
or enable port forwarding in new commandline window:
```
kubectl port-forward svc/argocd-server 8080:443 -n argocd
```
Also add code below to /etc/hosts
```
127.0.0.1       argocd-server.local
```
To get password for user Admin so you can login to http://localhost:8080/ or http://argocd-server.local/:
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64
```
You should see that the app is Healthy and is NOT out of sync

We'll also run [simple tests](https://github.com/urbeingwatched8/loberta_test_task/blob/main/testing.py) written in Python. 
To run, use
```
python3 testing.py
```
You should see that it returns 'Ran 2 tests in 0.014s' and 'OK'. 
The request response text is a bit different from what we see on 'localhost', but that's completely fine

