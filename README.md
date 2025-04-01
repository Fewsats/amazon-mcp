# Agora MCP

An MCP server for searching, discovering, and purchasing products through AI assistants like Claude or Cursor.

## What is Agora MCP?

Agora MCP connects AI assistants to [SearchAgora](https://www.searchagora.com/) - a universal product search engine that helps you discover and buy products from across the web. With this MCP, you can seamlessly search for products, compare options, manage your shopping cart, and complete purchases directly through your AI assistant.

## Prerequisites

- MCP Client like [Cursor](https://cursor.sh/) or [Claude Desktop](https://claude.ai/download)
- [UV](https://docs.astral.sh/uv/getting-started/installation/) installed
- A payment method through any L402-compatible client like [Fewsats](https://fewsats.com)

## Setting Up the MCP Server

### For Cursor

1. Open Cursor and go to Settings
2. Navigate to MCP Server Configuration
3. Add the following configuration:

```json
{
  "mcpServers": {
    "Agora": {
      "command": "uvx",
      "args": [
        "agora-mcp"
      ]
    },
    "Fewsats": {
      "command": "env",
      "args": [
        "FEWSATS_API_KEY=YOUR_FEWSATS_API_KEY",
        "uvx",
        "fewsats-mcp"
      ]
    }
  }
}
```

Make sure to replace `YOUR_FEWSATS_API_KEY` with your actual API key from [Fewsats](https://app.fewsats.com/api-keys).

### For Claude Desktop

1. Find the configuration file:
   - On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
   - On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

2. Add the following configuration:

```json
"mcpServers": {
  "Agora": {
    "command": "uvx",
    "args": [
      "agora-mcp"
    ]
  },
  "Fewsats": {
    "command": "env",
    "args": [
      "FEWSATS_API_KEY=YOUR_FEWSATS_API_KEY",
      "uvx",
      "fewsats-mcp"
    ]
  }
}
```

### Running a Local Development Version

For development purposes, you can run a local version of the Agora MCP from your own repository:

```json
"Agora": {
  "command": "uv",
  "args": [
    "--directory",
    "/path/to/your/agora-mcp",
    "run",
    "agora-mcp"
  ]
}
```

Replace `/path/to/your/agora-mcp` with the actual path to your local Agora MCP repository.

## Using Agora MCP With Your AI

Once configured, you can have natural conversations with your AI to search for and purchase products:

### Searching for Products

Simply ask your AI to search for products:

```
Can you find a cool t-shirt for me?
```

### Advanced Search Options

Refine your search with additional parameters:

```
Show me headphones under $100 sorted by highest rating
```

The search supports:
- Price ranges (min/max)
- Pagination
- Custom sorting
- Product filtering

### Coming Soon: Shopping Cart & Purchasing

Soon you'll be able to:

```
Add that red t-shirt to my cart
```

```
Show me what's in my cart
```

```
Checkout and purchase my items
```

## Supported Features

Currently, Agora MCP supports:

- Product search with customizable parameters:
  - Search query
  - Results per page
  - Page navigation
  - Price filtering (minimum and maximum)
  - Custom sorting options

Coming soon:
- Add products to cart
- View and manage shopping cart
- Complete purchases
- Save favorite products
- Track order status

## About SearchAgora

[SearchAgora](https://www.searchagora.com/) is a universal product search engine that helps you discover products from across the web. It offers a seamless shopping experience with comprehensive product information, price comparisons, and streamlined checkout processes.

