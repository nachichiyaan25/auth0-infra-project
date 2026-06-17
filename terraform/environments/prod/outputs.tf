output "alb_dns_name" {
  value = module.auth0_infra.alb_dns_name
}

output "ec2_public_ip" {
  value = module.auth0_infra.ec2_public_ip
}

output "ec2_public_dns" {
  value = module.auth0_infra.ec2_public_dns
}