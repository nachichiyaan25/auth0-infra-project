resource "aws_security_group" "a0i_instances_sg" {
  name        = "${var.project_name}-${var.environment}-instances-sg"
  description = "Security group for EC2 instances of ${var.project_name} in ${var.environment} environment"
  vpc_id      = aws_vpc.a0i_vpc.id

  ingress {

    description = "Allow SSH access from anywhere"

    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {

    description = "Allow traffic from anywhere on port 8000"

    from_port = 8000
    to_port   = 8000
    protocol  = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_security_group" "a0i_alb_sg" {
  name        = "${var.project_name}-${var.environment}-alb-sg"
  description = "Security group for ALB of ${var.project_name} in ${var.environment} environment"
  vpc_id      = aws_vpc.a0i_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
