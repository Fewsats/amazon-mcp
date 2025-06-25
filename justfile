# add a new dependency with `uv add <package>`.
# This will add it to the pyproject.toml file and the uv.lock file

# `uv tool run` is equivalent to `uvx`
# by default `uvx` will run the command with the same name as the package when run like `uvx <package>`.
# when run like `uv tool run . <package>` it should do the same as previous command, but locally.
run-dev:
    uv tool run . amazon-mcp

# When a new version is not found, you can refresh the package with:  uvx --refresh amazon-mcp@0.1.1
run:
    uvx --refresh amazon-mcp

# In order to release a new version, you need to:
# 0. Clean previous releases
clean:
    rm -rf dist

# 1. Update the version in the pyproject.toml file
# 2. Sync this new package version into the pyproject.toml with:
sync-version:
    uv sync

# 3. Build the package 
build: clean sync-version
    uv build

# 4.a Test the release locally using the release wheel. I am not sure why the command `amazon-mcp` can't be ommited here.
run-release: build
    uv tool run --with dist/amazon_mcp-0.1.0-py3-none-any.whl amazon-mcp

# 4.b Test the release from an MCP client using the path
# NOTE this can still fail / use old version depending on uv envs, not sure how to fix it
run-release-client: build
    uv --directory /Users/pengren/go/github.com/Fewsats/amazon-mcp run amazon-mcp

# 5. Release the package to PyPI
release: clean sync-version build
    uv publish --token {{PYPI_TOKEN}} 