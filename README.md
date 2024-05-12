# **LOBERTA TEST TASK**
# 
---
Prequisites: install [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), [Kind](https://kind.sigs.k8s.io/docs/user/quick-start), [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Helm](https://helm.sh/docs/intro/install/)  

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
Settings for the new Service, Deployment and ports are specified [here](https://github.com/urbeingwatched8/loberta_test_task/blob/main/usage.yaml)
To apply, run
```
kubectl apply -f usage.yaml
```

To check the website, you can run 
```
curl  -kL http://localhost/
```
You should get My Test Site(base) without errors.
