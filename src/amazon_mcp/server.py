from mcp.server.fastmcp import FastMCP
from amazon.client import Amazon
import os
from typing import Dict, List, Optional


# Create FastMCP instance
mcp = FastMCP("Fewsats MCP Server")


def get_amazon():
    """Get or create an Amazon instance. 
    We want to create the class instance inside the tool, 
    so the init errors will bubble up to the tool and hence the MCP client instead of silently failing
    during the server creation.
    """
    return Amazon()


def handle_response(response):
    """
    Handle responses from Amazon methods.
    """
    if hasattr(response, 'status_code'):
        # This is a raw response object
        try: return response.status_code, response.json()
        except: return response.status_code, response.text
    # This is already processed data (like a dictionary)
    return response


@mcp.tool()
async def search(q: str) -> Dict:
    """
    Search for products matching the query.
    
    Args:
        q: The search query of a specific ASIN of a given product.
        
    Returns:
        The search results.
    """
    response = get_amazon().search(
        query=q,
    )
    return handle_response(response)


@mcp.tool()
async def get_payment_offers(asin: str, shipping_address: Dict,
                 user: Dict, quantity: int = 1) -> Dict:
    """
    Get the payment offers for a product.
    Before calling this tool, check if the user has already provided the shipping address and user information. 
    Otherwise, ask the user for the shipping address and user information.

    Args:
        asin: The product ASIN.
        quantity: The quantity to purchase.
        shipping_address: The shipping address.
        user: The user information.
        
    Example:
        shipping_address = {
            "full_name": "John Doe",
            "address": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "US",
            "postal_code": "10001"
        }
        
        user = {
            "full_name": "John Doe",
            "email": "john@example.com",
        }
        
    Returns:
        L402 offer that can be paid by L402-compatible clients.
    """
    response = get_amazon().buy_now(
        asin=asin,
        quantity=quantity,
        shipping_address=shipping_address,
        user=user
    )
    return handle_response(response)


@mcp.tool()
async def get_payment_offers_x402(asin: str, shipping_address: Dict,
                 user: Dict, quantity: int = 1) -> Dict:
    """
    Get the payment offers for a product.
    Before calling this tool, check if the user has already provided the shipping address and user information. 
    Otherwise, ask the user for the shipping address and user information.

    Args:
        asin: The product ASIN.
        quantity: The quantity to purchase.
        shipping_address: The shipping address.
        user: The user information.
        
    Example:
        shipping_address = {
            "full_name": "John Doe",
            "address": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "US",
            "postal_code": "10001"
        }
        
        user = {
            "full_name": "John Doe",
            "email": "john@example.com",
        }
        
    Returns:
        X402 offer that can be paid by X402-compatible clients.
    """
    response = get_amazon().buy_now_with_x402(
        asin=asin,
        quantity=quantity,
        shipping_address=shipping_address,
        user=user
    )
    return handle_response(response)


@mcp.tool()
async def pay_with_x402(x_payment: str, asin: str, shipping_address: Dict,
                 user: Dict, quantity: int = 1) -> Dict:
    """
    Pay for a product with X402.
    You need to add the generated X-PAYMENT header to the request.

    Args:
        x_payment: The generated X-PAYMENT header.
        asin: The product ASIN.
        quantity: The quantity to purchase.
        shipping_address: The shipping address.
        user: The user information.
        
    Example:
        shipping_address = {
            "full_name": "John Doe",
            "address": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "US",
            "postal_code": "10001"
        }
        
        user = {
            "full_name": "John Doe",
            "email": "john@example.com",
        }
        
    Returns:
        The payment response header.
    """
    response = get_amazon().buy_now_with_x402(
        asin=asin,
        quantity=quantity,
        shipping_address=shipping_address,
        user=user,
        x_payment=x_payment
    )
    return handle_response(response)


@mcp.tool()
async def get_order_by_external_id(external_id: str) -> Dict:
    """
    Get the status of a specific order.
    
    Args:
        external_id: The external ID of the order.
        
    Returns:
        The order details.
    """
    response = get_amazon().get_order_by_external_id(external_id=external_id)
    return handle_response(response)

@mcp.tool()
async def get_order_by_payment_token(payment_context_token: str) -> Dict:
    """
    Get the status of a specific order by payment context token.
    
    Args:
        payment_context_token: The payment context token of the order.
        
    Returns:
        The order details.
    """
    response = get_amazon().get_order_by_payment_token(payment_token=payment_context_token)
    return handle_response(response)


@mcp.tool()
async def get_user_orders() -> List[Dict]:
    """
    Get all orders for the current user.
    
    Returns:
        A list of orders.
    """
    response = get_amazon().get_user_orders()
    return handle_response(response)


def main():
    mcp.run()
