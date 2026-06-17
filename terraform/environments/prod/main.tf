terraform {
  backend "s3" {
    bucket         = "auth0-infra-tf-state"
    key            = "environments/prod/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "auth0-infra-state-locking"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

locals {
  environment = "prod"
}

module "auth0_infra" {
  source = "../../modules/auth0-infra"

  # Input Variables
  environment = local.environment
  key_name    = "auth0-infra-key"

  
  secret_key = var.secret_key

  auth0_client_id     = var.auth0_client_id
  auth0_client_secret = var.auth0_client_secret
 
  auth0_domain        = var.auth0_domain
  auth0_audience = var.auth0_audience

  auth0_m2m_client_id     = var.auth0_m2m_client_id
  auth0_m2m_client_secret = var.auth0_m2m_client_secret

  auth0_management_api_audience = var.auth0_management_api_audience

}