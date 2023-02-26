#!/usr/bin/env python3

import sys
# import boto3

# from boto3.dynamodb.conditions import Attr
from pathlib import Path

# FIXME
path_to_util = "{}/util".format(Path(__file__).parent.parent)
print(path_to_util)
sys.path.append(path_to_util)

from Util import Util


class AmazonHelper(Util):

    def __init__(self):
        super(AmazonHelper).__init__()
        self.debug = True

    def get_data(self, table_name, filter_expression):
        '''Queries data from amazon Dynamo DB table
        
        :param table_name: DynamoDB table name
        :param filter_expression: boto3.dynamodb.conditions.Attr filter expression used to search for content in table
        :returns: list of dictionaries with amazon Table info
        '''
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        print(str(filter_expression))
        response = table.scan(
            FilterExpression=filter_expression,
        )

        return response['Items']

