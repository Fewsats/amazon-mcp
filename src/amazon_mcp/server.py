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
async def amazon_search(q: str, domain: str = "amazon.com") -> Dict:
    """
    Search for products matching the query in amazon.
    If the user does not specify a domain, try to infer the domain from the product description or user's language.

    Args:
        q: The search query of a specific ASIN of a given product.
        domain: The amazon domain of the search. E.g. amazon.com, amazon.es ...

    Returns:
        The search results.
    """
    response = get_amazon().search(
        query=q,
        domain=domain
    )
    return handle_response(response)


@mcp.tool()
async def amazon_get_payment_offers(product_url: str, shipping_address: Dict,
                 user: Dict, asin: str = "", quantity: int = 1, protocol: str = "L402") -> Dict:
    """
    Get the payment offers for a product.
    Before calling this tool, check if the user has already provided the shipping address and user information. 
    Otherwise, ask the user for the shipping address and user information.

    Args:
        product_url: The Amazon URL of the product returned by the search tool.
        shipping_address: The shipping address.
        user: The user information.
        asin: The product ASIN (optional).
        quantity: The quantity to purchase.
        
    Example:
        shipping_address = {
            "full_name": "John Doe",
            "phone": "+1234567890",
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
        HTTP Status 402 Payment Required and the L402 offer that can be paid by L402-compatible clients.
    """
    if protocol == "X402":
        response = get_amazon().buy_now_with_x402(
            product_url=product_url,
            shipping_address=shipping_address,
            user=user,
            asin=asin,
            quantity=quantity
        )
    else: # Use L402 protocol by default
        response = get_amazon().buy_now(
            product_url=product_url,
            shipping_address=shipping_address,
            user=user,
            asin=asin,
            quantity=quantity
        )
    return handle_response(response)


@mcp.tool()
async def pay_with_x402(x_payment: str, product_url: str, shipping_address: Dict,
                 user: Dict, asin: str = "", quantity: int = 1) -> Dict:
    """
    Pay for a product with X402.
    You need to add the generated X-PAYMENT header to the request.

    Args:
        x_payment: The generated X-PAYMENT header.
        product_url: The URL of the product.
        shipping_address: The shipping address.
        user: The user information.
        asin: The product ASIN (optional).
        quantity: The quantity to purchase.

    Example:
        shipping_address = {
            "full_name": "John Doe",
            "phone": "+1234567890",
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
        product_url=product_url,
        shipping_address=shipping_address,
        user=user,
        asin=asin,
        quantity=quantity,
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
