import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Crawler } from './crawler';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class ApplicationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'LibQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });

    new Crawler(this, 'crawler')
  }
}
