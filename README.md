# Amazon Shopping with Claude

This integration allows you to search and buy Amazon products directly through your AI assistant. Shop Amazon's vast catalog by simply chatting with Claude!

## What You Need

1. [Claude Desktop App](https://claude.ai/download) - Your AI shopping assistant
2. [Fewsats Account](https://fewsats.com) - Required for secure payments (takes 2 minutes to set up)



## Quick Setup Guide

### Step 1: Install Claude Desktop App
1. Download Claude from [claude.ai/download](https://claude.ai/download)
2. Install and open the app

### Step 2: Set Up Fewsats
1. Go to [fewsats.com](https://fewsats.com) and create an account
2. Add a payment method (credit card, Apple Pay, or Google Pay)
3. Get your API key from [app.fewsats.com/api-keys](https://app.fewsats.com/api-keys)

### Step 3: Configure Claude
1. Find your Claude config file:
   - Mac: Open Terminal and paste: `open ~/Library/Application\ Support/Claude/claude_desktop_config.json`
   - Windows: Press Win+R, type `%APPDATA%/Claude`, and open `claude_desktop_config.json`

2. Add this configuration (replace YOUR_FEWSATS_API_KEY with your actual key):

```json
{
  "mcpServers": {
    "Amazon": {
      "command": "uvx",
      "args": [
        "amazon-mcp"
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

### Step 4: Install UV
UV is a small tool needed to run the Amazon integration:

- Mac: Open Terminal and run:
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Windows: Open PowerShell as Administrator and run:
  ```
  irm https://astral.sh/uv/install.ps1 | iex
  ```

## Start Shopping!

That's it! Now you can chat with Claude about Amazon products. Try these:

- "Find me a coffee maker under $50"
- "I need running shoes, what do you recommend?"
- "Can you search for kids' books about dinosaurs?"

Claude will help you search, compare products, and make purchases securely through Fewsats.

## Using with Cursor (For Developers)

If you're a developer using Cursor, the setup is similar. In Cursor's settings, add:

```json
{
  "mcpServers": {
    "Amazon": {
      "command": "uvx",
      "args": [
        "amazon-mcp"
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

## Security First: Policies

With Fewsats, you decide how purchases are handled:

- **Custom Budget Limits**: Set monthly or per-transaction spending caps
- **Approval Thresholds**: Auto-approve small purchases, review larger ones
- **Manual Review**: Option to approve every purchase before it's processed
- **Purchase History**: Track and review all transactions in one place


## About

This integration is powered by [Fewsats](https://fewsats.com), providing secure payment infrastructure for AI assistants. All purchases are protected by Fewsats' buyer protection policy.

[Amazon](https://www.amazon.com/) is the world's largest e-commerce platform, offering millions of products across diverse categories. With features like Prime shipping, competitive pricing, and extensive product reviews, Amazon provides a comprehensive shopping experience for customers worldwide.

## Need Help?

Visit [fewsats.com/support](https://fewsats.com/support) for assistance with payments or general questions.

