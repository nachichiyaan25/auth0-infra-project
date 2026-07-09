output "alb_dns_name" {
  value = aws_lb.a0i_alb.dns_name
}

output "ec2_public_ip" {
  value = aws_instance.a0i_instance_1.public_ip
}

output "ec2_public_dns" {
  value = aws_instance.a0i_instance_1.public_dns
}

output "ec2_instance_id" {
  value = aws_instance.a0i_instance_1.id
}