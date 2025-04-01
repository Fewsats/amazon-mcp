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
            "name": "John Doe",
            "address": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "US",
            "postal_code": "10001"
        }
        
        user = {
            "name": "John Doe",
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

# @mcp.tool()
# async def get_cart() -> Dict:
#     """
#     Get the current user's cart.
    
#     Returns:
#         The cart details.
#     """
#     response = get_amazon().get_cart()
#     return handle_response(response)


# @mcp.tool()
# async def add_to_cart(slug: str, product_id: str, variant_id: Optional[str] = None, quantity: int = 1) -> Dict:
#     """
#     Add an item to the user's cart. Some products do not have variants, in such cases use the product_id as variant_id too.
    
#     Args:
#         slug: The product slug.
#         product_id: The product ID.
#         variant_id: The product variant ID.
#         quantity: The quantity to add.
        
#     Returns:
#         The updated cart.
#     """
#     response = get_amazon().add_to_cart(
#         slug=slug,
#         product_id=product_id,
#         variant_id=variant_id,
#         quantity=quantity
#     )
#     return handle_response(response)


# @mcp.tool()
# async def update_cart_item(slug: str, product_id: str, variant_id: str, quantity: int) -> Dict:
#     """
#     Update the quantity of an item in the cart. Some products do not have variants, in such cases use the product_id as variant_id too.
    
#     Args:
#         slug: The product slug.
#         product_id: The product ID.
#         variant_id: The product variant ID.
#         quantity: The new quantity.
        
#     Returns:
#         The updated cart.
#     """
#     response = get_amazon().update_cart_item(
#         slug=slug,
#         product_id=product_id,
#         variant_id=variant_id,
#         quantity=quantity
#     )
#     return handle_response(response)


# @mcp.tool()
# async def clear_cart() -> Dict:
#     """
#     Clear all items from the cart.
    
#     Returns:
#         The response from the API.
#     """
#     response = get_amazon().clear_cart()
#     return handle_response(response)


@mcp.tool()
async def get_order(external_id: str) -> Dict:
    """
    Get details for a specific order.
    
    Args:
        external_id: The external ID of the order.
        
    Returns:
        The order details.
    """
    response = get_amazon().get_order(external_id=external_id)
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


@mcp.tool()
async def get_user_info() -> Dict:
    """
    Get the current user's profile and shipping addresses.
    
    Returns:
        Dict containing user profile info (firstname, lastname, email) and list of shipping addresses
    """
    response = get_amazon().get_user_info()
    return handle_response(response)


def main():
    mcp.run()
