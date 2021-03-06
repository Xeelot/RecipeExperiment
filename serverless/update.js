import * as dynamoDbLib from './libs/dynamodb-lib';
import { success, failure } from './libs/response-lib';

export async function main(event, context, callback) {
    const data = JSON.parse(event.body);
    const params = {
        TableName: 'HCE-IngredientCategories',
        Key: {
            userId: event.requestContext.authorizer.claims.sub,
            ingCatId: event.pathParameters.id,
        },
        UpdateExpression: 'SET category = :category, modifiedAt = :modifiedAt',
        ExpressionAttributeValues: {
            ':category': data.category ? data.category : null,
            ':modifiedAt': new Date().getTime(),
        },
        ReturnValues: 'ALL_NEW',
    };

    try {
        const result = await dynamoDbLib.call('update', params);
        callback(null, success({status: true}));
    } catch(e) {
        console.log(e);
        callback(null, failure({status: false}));
    }
}