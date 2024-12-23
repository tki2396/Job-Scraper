import { aws_lambda as lambda } from "aws-cdk-lib";
import { Construct } from "constructs";
import path = require("path");

interface CrawlerProps {
  databaseName: string;
  role: string;
}

const SERVICE_NAME = "ingestion-service";
const SERVICE_DIR = path.resolve(__dirname, '../../')
console.log(`${SERVICE_DIR}/${SERVICE_NAME}`);


export class Crawler {
  constructor(scope: Construct, id: string, props?: CrawlerProps) {
    
    // Crawler Lambda function
    new lambda.DockerImageFunction(scope, id, {
      code: lambda.DockerImageCode.fromImageAsset(`${SERVICE_DIR}/${SERVICE_NAME}`),
    });
  }
}