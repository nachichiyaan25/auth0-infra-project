resource "aws_vpc" "a0i_vpc" {

  cidr_block = var.vpc_cidr

  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

resource "aws_internet_gateway" "a0i_igw" {

  vpc_id = aws_vpc.a0i_vpc.id

  tags = {
    Name = "${var.project_name}-${var.environment}-igw"
  }
}

resource "aws_subnet" "a0i_public_subnet_1" {

  vpc_id = aws_vpc.a0i_vpc.id

  cidr_block = var.public_subnet_1_cidr

  availability_zone = var.availability_zone_1

  map_public_ip_on_launch = true

  tags = {
    Name = "${var.project_name}-${var.environment}-public-subnet-1"
  }
}

resource "aws_subnet" "a0i_public_subnet_2" {

  vpc_id = aws_vpc.a0i_vpc.id

  cidr_block = var.public_subnet_2_cidr

  availability_zone = var.availability_zone_2

  map_public_ip_on_launch = true

  tags = {
    Name = "${var.project_name}-${var.environment}-public-subnet-2"
  }
}

resource "aws_route_table" "a0i_public_rt" {

  vpc_id = aws_vpc.a0i_vpc.id

  tags = {
    Name = "${var.project_name}-${var.environment}-public-rt"
  }
}

resource "aws_route" "internet_access" {

  route_table_id = aws_route_table.a0i_public_rt.id

  destination_cidr_block = "0.0.0.0/0"

  gateway_id = aws_internet_gateway.a0i_igw.id
}

resource "aws_route_table_association" "subnet_1" {

  subnet_id = aws_subnet.a0i_public_subnet_1.id

  route_table_id = aws_route_table.a0i_public_rt.id
}

resource "aws_route_table_association" "subnet_2" {

  subnet_id = aws_subnet.a0i_public_subnet_2.id

  route_table_id = aws_route_table.a0i_public_rt.id
}


resource "aws_lb" "a0i_alb" {

  name = "${var.project_name}-${var.environment}-alb"
  internal = false
  load_balancer_type = "application"

  security_groups = [
    aws_security_group.a0i_alb_sg.id
  ]

  subnets = [
    aws_subnet.a0i_public_subnet_1.id,
    aws_subnet.a0i_public_subnet_2.id
  ]

  tags = {
    Name = "${var.project_name}-${var.environment}-alb"
  }
}

resource "aws_lb_listener" "a0i_http_listener" {

  load_balancer_arn = aws_lb.a0i_alb.arn
  port = 80
  protocol = "HTTP"

  default_action {

    type = "forward"

    target_group_arn = aws_lb_target_group.a0i_tg.arn
  }
}

resource "aws_lb_target_group" "a0i_tg" {

  name     = "${var.project_name}-${var.environment}-tg"
  port     = 8000
  protocol = "HTTP"

  vpc_id = aws_vpc.a0i_vpc.id

  health_check {

    enabled = true

    path = "api/health/"

    port = "traffic-port"

    protocol = "HTTP"

    healthy_threshold   = 3
    unhealthy_threshold = 5

    timeout  = 5
    interval = 30

    matcher = "200"
  }

  tags = {
    Name = "${var.project_name}-${var.environment}-tg"
  }
}

resource "aws_lb_target_group_attachment" "a0i_instance_1_attachment" {

  target_group_arn = aws_lb_target_group.a0i_tg.arn

  target_id = aws_instance.a0i_instance_1.id

  port = 8000
}