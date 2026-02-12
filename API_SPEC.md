# API specification

## Authentication
- All endpoints except `GET /api/goods/` require authentication via Django session cookies.
- Administrator/warehouse operations also require the user role to be `ADMIN` or `WAREHOUSE`.

## Endpoints

1. `GET /api/goods/`  
   - Response: `{ "goods": [ { "id", "name", "amount", "cost", "type", "company" }, ... ] }`  
   - Purpose: List all products for any authenticated or anonymous user.

2. `POST /api/goods/`  
   - Body: `{ "name": string, "amount": number, "cost": number }`  
   - Role: Warehouse or administrator.  
   - Response: Created product payload (status code 201) or error codes for validation.

3. `GET /api/goods/{id}/`  
   - Response: Single product payload.

4. `PUT /api/goods/{id}/`  
   - Role: Warehouse or administrator.  
   - Body: Partial fields `{ "name", "amount", "cost" }`.  
   - Response: Updated product.

5. `DELETE /api/goods/{id}/`  
   - Role: Warehouse or administrator.  
   - Response: `{ "status": "deleted" }`.

6. `GET /api/orders/`  
   - Role: authenticated user.  
   - Response: List of the user's orders and the donated items.

7. `POST /api/orders/checkout/`  
   - Role: authenticated user.  
   - Body: `{ "address": string, "items": [ { "good_id": int, "amount": int } ] }`.  
   - Response: `{ "order_id": X, "status": "created" }`.

Errors use HTTP status codes 4xx/5xx with JSON payload `{ "error": "message" }`.
