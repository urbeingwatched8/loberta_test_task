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
**# Task 3**

Run this to install Prometheus and Grafana:
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus kube-prometheus-stack --create-namespace --namespace prom
```
Use this [file](https://github.com/urbeingwatched8/loberta_test_task/blob/main/prom.yaml) to create prometheus ingress

```
kubectl apply -f prom.yaml
```
And add this to /etc/hosts
```
127.0.0.1 prom.local
```
Now you can access Prometheus at localhost:9090
To finish with setting up Grafana, enable port forwarding
```
kubectl port-forward deployment/prometheus-grafana -n prometheus-grafana 3000
```
Now you can access it at http://localhost:3000 with username admin and password admin.
To create Prometheus Dashboard, add it as Data Source:
Configuration>Data Sources>Add Data Source>Search For 'Prometheus'>Leave default 'prometheus' name>Add Url after getting external api from ifconfig 'http://External-Api:9090'

After saving you the connection will be tested. In case of problems with Url, try 'http://prometheus/9090'
![image](https://github.com/urbeingwatched8/loberta_test_task/blob/main/pics/GrafanaProm.png)
To create a Dashboard, you can look for existing ones, choose the most suitable (I decided to use 15055) and then go to:
Dashboards>New>Import Dashboard>Get it by number or Json file>Save
![image](https://github.com/urbeingwatched8/loberta_test_task/blob/main/pics/GrafanaBoard.png)

To install Loki, run
```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm upgrade - install loki - namespace=loki-stack grafana/loki-stack - create-namespace
```
Enable port forwarding:
```
kubectl -n loki port-forward svc/grafana 8080:80
```
To add Loki as Data Source:
Configuration>Data Sources>Add Data Source>Search For 'Prometheus'>Leave default 'loki' name>Add Url after getting external api from ifconfig 'http://loki:3100'
![image](https://github.com/urbeingwatched8/loberta_test_task/blob/main/pics/GrafanaLoki.png)
Now you can view logs in Explore
![image](https://github.com/urbeingwatched8/loberta_test_task/blob/main/pics/GrafanaLogs.png)


