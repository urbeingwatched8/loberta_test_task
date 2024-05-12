terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "2.10.1"
    }
    
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.22.0"
    }

    null = {
      source  = "hashicorp/null"
      version = "3.2.1"
    }
  }
  required_version = ">= 1.0.0"
}
