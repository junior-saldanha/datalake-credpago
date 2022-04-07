resource "aws_glue_crawler" "glue_crawler" {
  database_name = "dms-credpago"
  name          = "dms-credpago"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://cp-datalake/dms/"
  }

  tags = local.common_tags

}