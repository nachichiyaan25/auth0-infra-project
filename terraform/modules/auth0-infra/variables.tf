# General Variables

variable "region" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "ap-south-1"
}

variable "environment" {
  description = "The environment to deploy resources (e.g., dev, prod)"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "The name of the Project"
  type        = string
  default     = "auth0-infra"
}


# EC2 Variables

variable "ami_id" {
  description = "The Amazon Machine Image (AMI) ID to use for EC2 instances"
  type        = string
  default     = "ami-0650cc48f4b5304f0" # Ubuntu 24.04 LTS in ap-south-1
}

variable "instance_type" {
  description = "The type of EC2 instance to use"
  type        = string
  default     = "t3.micro"
}


# Networking Variables

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_1_cidr" {
  description = "CIDR block for public subnet 1"
  type        = string
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR block for public subnet 2"
  type        = string
  default     = "10.0.2.0/24"
}

variable "availability_zone_1" {
  description = "Availability Zone 1"
  type        = string
  default     = "ap-south-1a"
}

variable "availability_zone_2" {
  description = "Availability Zone 2"
  type        = string
  default     = "ap-south-1b"
}

variable "key_name" {
  description = "EC2 Key Pair Name"
  type        = string
}


# env Variables

variable "secret_key" {
  type      = string
  sensitive = true
}

variable "auth0_client_id" {
  type      = string
  sensitive = true
}

variable "auth0_client_secret" {
  type      = string
  sensitive = true
}

variable "auth0_domain" {
  type      = string
  sensitive = true
}

variable "auth0_audience" {
  type      = string
}

variable "auth0_m2m_client_id" {
  type      = string
  sensitive = true
}

variable "auth0_m2m_client_secret" {
  type      = string
  sensitive = true
}

variable "auth0_management_api_audience" {
  type      = string
  sensitive = true
}