locals {

  env_file = templatefile(
    "${path.module}/templates/env.tpl",
    {
      secret_key = var.secret_key

      auth0_client_id     = var.auth0_client_id
      auth0_client_secret = var.auth0_client_secret

      auth0_domain   = var.auth0_domain
      auth0_audience = var.auth0_audience

      auth0_m2m_client_id           = var.auth0_m2m_client_id
      auth0_m2m_client_secret       = var.auth0_m2m_client_secret
      auth0_management_api_audience = var.auth0_management_api_audience

      alb_dns_name = aws_lb.a0i_alb.dns_name
    }
  )

  user_data = templatefile(
    "${path.module}/templates/user_data.sh.tpl",
    {
      github_actions_public_key = var.github_actions_public_key
      env_file                  = local.env_file
    }
  )
}



resource "aws_instance" "a0i_instance_1" {

  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id = aws_subnet.a0i_public_subnet_1.id

  associate_public_ip_address = true

  key_name = var.key_name

  vpc_security_group_ids = [aws_security_group.a0i_instances_sg.id]

  user_data = local.user_data

  tags = {
    Name = "${var.project_name}-${var.environment}-instance-1"
  }
}

resource "aws_instance" "a0i_instance_2" {

  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id = aws_subnet.a0i_public_subnet_2.id

  associate_public_ip_address = true

  key_name = var.key_name

  vpc_security_group_ids = [aws_security_group.a0i_instances_sg.id]

  user_data = local.user_data

  tags = {
    Name = "${var.project_name}-${var.environment}-instance-2"
  }
}