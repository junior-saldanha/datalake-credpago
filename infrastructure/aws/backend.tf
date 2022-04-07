# Backend configuration require a AWS storage bucket.
terraform {
  backend "s3" {
    bucket = "terraform-state-credpago-datalake"
    key    = "state/credpago//terraform.tfstate"
    region = "us-east-1"
  }
}
