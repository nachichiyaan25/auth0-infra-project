output "alb_dns_name" {
  value = module.auth0_infra.alb_dns_name
}

output "ec2_public_ips" {
  value = module.auth0_infra.ec2_public_ips
}

output "ec2_instance_ids" {
  value = module.auth0_infra.ec2_instance_ids
}