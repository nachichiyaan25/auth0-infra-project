locals {

  env_file = templatefile(
    "${path.module}/templates/env.tpl",
    {
      secret_key                     = var.secret_key

      auth0_client_id                = var.auth0_client_id
      auth0_client_secret            = var.auth0_client_secret
      
      auth0_domain                   = var.auth0_domain
      auth0_audience                 = var.auth0_audience

      auth0_m2m_client_id            = var.auth0_m2m_client_id
      auth0_m2m_client_secret        = var.auth0_m2m_client_secret
      auth0_management_api_audience  = var.auth0_management_api_audience

      alb_dns_name = aws_lb.a0i_alb.dns_name
    }
  )
}

resource "aws_instance" "a0i_instance_1" {

  ami                         = var.ami_id
  instance_type               = var.instance_type

  subnet_id                   = aws_subnet.a0i_public_subnet_1.id

  associate_public_ip_address = true

  key_name                    = var.key_name

  vpc_security_group_ids      = [aws_security_group.a0i_instances_sg.id]

  user_data = <<-EOF
                #!/bin/bash
                
                set -e

                # Update packages
                apt-get update -y

                # Install Docker
                apt-get install -y docker.io git curl

                systemctl enable docker
                systemctl start docker

                # Install Docker Compose
                mkdir -p /usr/local/lib/docker/cli-plugins

                curl -SL https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-linux-x86_64 \
                -o /usr/local/lib/docker/cli-plugins/docker-compose

                chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

                # Add ubuntu user to docker group
                usermod -aG docker ubuntu

                # Clone application
                cd /home/ubuntu

                if [ ! -d "/home/ubuntu/auth0-infra-project" ]; then
                git clone https://github.com/nachichiyaan25/auth0-infra-project.git
                fi

                cat > /home/ubuntu/auth0-infra-project/.env <<'ENVFILE'
                ${local.env_file}
                ENVFILE

                chown -R ubuntu:ubuntu /home/ubuntu/auth0-infra-project

                cd /home/ubuntu/auth0-infra-project

                docker compose down || true

                docker compose up -d --build

                docker ps

                EOF

  tags = {
    Name = "${var.project_name}-${var.environment}-instance-1"
  }
}