terraform {
  backend "s3" {
    bucket = "auth0-infra-tf-state"
    key    = "import-bootstrap/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "auth0-infra-state-locking"
    encrypt = true
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


resource "aws_s3_bucket" "a0i_state_bucket" {
  bucket = "auth0-infra-tf-state"
  force_destroy = true

  tags = {
    Name        = "Auth0 Infra State Files Bucket"
  }
}

resource "aws_s3_bucket_versioning" "a0i_state_bucket_versioning" {
  bucket = aws_s3_bucket.a0i_state_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "a0i_state_bucket_encryption" {
  bucket = aws_s3_bucket.a0i_state_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}


resource "aws_dynamodb_table" "a0i_state_lock_table" {
  name         = "auth0-infra-state-locking"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name        = "Auth0 Infra State Lock Table"
  }
}