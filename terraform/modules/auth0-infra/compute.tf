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
}

resource "aws_instance" "a0i_instance_1" {

  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id = aws_subnet.a0i_public_subnet_1.id

  associate_public_ip_address = true

  key_name = var.key_name

  vpc_security_group_ids = [aws_security_group.a0i_instances_sg.id]

  user_data = <<-EOF
                #!/bin/bash
                
                set -e

                # Update packages
                apt-get update -y

                # Install and Enable Docker
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

                # Add SSH public key to authorized_keys
                mkdir -p /home/ubuntu/.ssh

                cat <<EOFSSH >> /home/ubuntu/.ssh/authorized_keys
                ${var.github_actions_public_key}
                EOFSSH

                chmod 700 /home/ubuntu/.ssh
                chmod 600 /home/ubuntu/.ssh/authorized_keys
                chown -R ubuntu:ubuntu /home/ubuntu/.ssh

                # Clone application
                cd /home/ubuntu

                if [ ! -d "/home/ubuntu/auth0-infra-project" ]; then
                git clone https://github.com/nachichiyaan25/auth0-infra-project.git
                fi

                # Request instance private IP from IMDS(Instance Metadata Service)
                TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
                -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

                PRIVATE_IP=$(curl -s \
                -H "X-aws-ec2-metadata-token: $TOKEN" \
                http://169.254.169.254/latest/meta-data/local-ipv4)

                # Create .env file with environment variables
                cat > /home/ubuntu/auth0-infra-project/.env <<'ENVFILE'
                ${local.env_file}
                ENVFILE

                # Append private IP to ALLOWED_HOSTS
                sed -i "s/^ALLOWED_HOSTS=.*/&,$PRIVATE_IP/" /home/ubuntu/auth0-infra-project/.env

                chown -R ubuntu:ubuntu /home/ubuntu/auth0-infra-project

                EOF

  tags = {
    Name = "${var.project_name}-${var.environment}-instance-1"
  }
}