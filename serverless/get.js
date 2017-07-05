import * as dynamoDbLib from './libs/dynamodb-lib';
import {success, failure} from './libs/response-lib';

export async function main(event, context, callback) {
    const params = {
        TableName: 'HCE-IngredientCategories',
        Key: {
            userId: event.requestContext.authorizer.claims.sub,
            ingCatId: event.pathParameters.ingCatId,
        },
    };

    try {
        const result = await dynamoDbLib.call('get', params);
        if (result.Item) {
            callback(null, success(result.Item));
        } else {
            callback(null, failure({status: false, error: 'Item not found.'}));
        }
    } catch(e) {
        console.log(e);
        callback(null, failure({status: false}));
    }
}