output "alb_dns_name" {
  value = aws_lb.a0i_alb.dns_name
}

output "ec2_public_ips" {
  value = [
    aws_instance.a0i_instance_1.public_ip,
    aws_instance.a0i_instance_2.public_ip
  ]
}

output "ec2_instance_ids" {
  value = [
    aws_instance.a0i_instance_1.id,
    aws_instance.a0i_instance_2.id
  ]
}