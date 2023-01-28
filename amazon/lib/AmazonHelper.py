import boto3
from boto3.dynamodb.conditions import Attr

from Util import Util

class AmazonHelper(Util):

    def __init__(self):
        super(AmazonHelper).__init__()
        self.debug = True
        self.table_name = ""

    def get_data(self, filter_expression):
        '''
        Queries data from amazon Dynamo DB table
        :param str table_name: DynamoDB table name 
        :param boto3.dynamodb.conditions.Attr filter_expression: expression used to search for content in table
        :returns: list of dictionaries with amazon Table info
        '''
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(self.table_name)

        response = table.scan(
            FilterExpression=filter_expression
        )

        return response['Items']
    # def set_table_name(self, table_name):
    #     """ Sets name of Dynamo DB Table
    #     :param: table_name: name of dynamoDB table
    #     :type: table_name: <str>
    #     :return: None
    #     """
    #     self.table_name = table_name

