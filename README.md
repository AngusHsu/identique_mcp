# Identique MCP Server

A Model Context Protocol (MCP) server for validating and extracting information from national ID numbers worldwide. This server provides tools to validate national identification numbers from 70+ countries and extract embedded information like birth dates, gender, and location data where available.

## Features

- **Multi-country support**: Validate ID numbers from 70+ countries
- **Information extraction**: Extract birth dates, gender, and other embedded data
- **Batch validation**: Validate multiple ID numbers at once
- **Format information**: Get format details for each country's ID system
- **3-digit country codes**: Uses ISO 3166-1 alpha-3 country codes (USA, GBR, FRA, etc.)

## Supported Countries

The server supports national ID validation for countries including:
- 🇺🇸 United States (SSN)
- 🇬🇧 United Kingdom (NINO)
- 🇫🇷 France (INSEE)
- 🇩🇪 Germany (Tax ID)
- 🇧🇷 Brazil (CPF)
- 🇹🇼 Taiwan (National ID)
- 🇨🇳 China (National ID)
- 🇯🇵 Japan (My Number)
- 🇰🇷 South Korea (RRN)
- And many more...

## Installation & Usage

### Using uv (Recommended)

You can run the MCP server directly from the repository using uv:

```bash
# Run the server directly
uv run --with git+https://github.com/AngusHsu/identique_mcp.git identique_mcp

# Or clone and run locally
git clone https://github.com/AngusHsu/identique_mcp.git
cd identique_mcp
uv run identique_mcp
```

### Using pip

```bash
# Install from git
pip install git+https://github.com/AngusHsu/identique_mcp.git

# Run the server
identique_mcp
```

### Development Setup

```bash
git clone https://github.com/AngusHsu/identique_mcp.git
cd identique_mcp
uv sync
uv run identique_mcp
```

## MCP Client Configuration

To use this server with an MCP client like Claude Desktop, add the following to your MCP settings:

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "identique": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "git+https://github.com/AngusHsu/identique_mcp.git",
        "identique_mcp"
      ]
    }
  }
}
```

## Available Tools

### 1. `list_supported_countries`
Lists all supported countries with their codes and ID types.

```python
# Returns list of countries with:
# - code: 3-digit country code
# - name: Country name  
# - id_type: Type of national ID
```

### 2. `validate_national_id`
Validates a single national ID number.

```python
validate_national_id(
    country_code="USA",  # 3-digit country code
    id_number="123-45-6789"  # ID number to validate
)
# Returns validation result with extracted info
```

### 3. `parse_id_info`
Extracts detailed information from a valid ID number.

```python
parse_id_info(
    country_code="TWN",
    id_number="A123456789"
)
# Returns extracted birth date, gender, etc.
```

### 4. `validate_multiple_ids`
Validates multiple ID numbers in batch.

```python
validate_multiple_ids([
    {"country_code": "USA", "id_number": "123-45-6789"},
    {"country_code": "GBR", "id_number": "AB123456C"}
])
```

### 5. `get_country_id_format`
Gets format information for a country's ID system.

```python
get_country_id_format(country_code="USA")
# Returns pattern, length, description
```

## Example Usage

```python
# List supported countries
countries = list_supported_countries()
print(f"Supports {len(countries)} countries")

# Validate a US Social Security Number
result = validate_national_id("USA", "123-45-6789")
print(f"Valid: {result['is_valid']}")

# Extract info from a Taiwan National ID
info = parse_id_info("TWN", "A123456789")
if info['is_valid']:
    print(f"Extracted info: {info['extracted_info']}")

# Get format info
format_info = get_country_id_format("USA")
print(f"Pattern: {format_info['pattern']}")
```

## Country Codes

Use ISO 3166-1 alpha-3 country codes:
- `USA` - United States
- `GBR` - United Kingdom  
- `FRA` - France
- `DEU` - Germany
- `TWN` - Taiwan
- `CHN` - China
- `JPN` - Japan
- `KOR` - South Korea
- `BRA` - Brazil
- And many more...

## Privacy & Security

This tool validates ID number formats and checksums but does not:
- Store or transmit ID numbers
- Verify against government databases
- Guarantee the ID belongs to a real person
- Provide personal information beyond what's encoded in the ID format

Always handle ID numbers securely and in compliance with applicable privacy laws.

## Dependencies

- `fastmcp` - MCP server framework
- `idnumbers` - National ID validation library

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter issues:
1. Check that you're using the correct 3-digit country code
2. Verify the ID number format matches the country's standard
3. Open an issue on GitHub with details about the problem

## Related Projects

- [IDNumbers](https://github.com/Identique/idnumbers) - The underlying validation library
- [FastMCP](https://github.com/jlowin/fastmcp) - MCP server framework
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP specification
