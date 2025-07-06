#!/usr/bin/env python3
"""
FastMCP Server for IDNumbers package
Provides MCP tools for validating and extracting information from national ID numbers
Uses 3-digit country codes and supports all countries
"""

import importlib
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# FastMCP imports
from fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP("IDNumbers Server")


@dataclass
class IDValidationResult:
    """Result of ID number validation"""

    is_valid: bool
    country_code: str
    id_number: str
    extracted_info: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None


def get_all_countries() -> List[Dict[str, str]]:
    """Get complete list of all countries with basic info"""
    return [
        {"code": "ALB", "name": "Albania", "id_type": "National ID"},
        {"code": "ARE", "name": "United Arab Emirates", "id_type": "Emirates ID"},
        {"code": "ARG", "name": "Argentina", "id_type": "DNI"},
        {"code": "AUS", "name": "Australia", "id_type": "TFN"},
        {"code": "AUT", "name": "Austria", "id_type": "National ID"},
        {"code": "BEL", "name": "Belgium", "id_type": "National Number"},
        {"code": "BGD", "name": "Bangladesh", "id_type": "NID"},
        {"code": "BGR", "name": "Bulgaria", "id_type": "UCN"},
        {"code": "BHR", "name": "Bahrain", "id_type": "CPR"},
        {"code": "BIH", "name": "Bosnia and Herzegovina", "id_type": "JMBG"},
        {"code": "BRA", "name": "Brazil", "id_type": "CPF"},
        {"code": "CAN", "name": "Canada", "id_type": "SIN"},
        {"code": "CHE", "name": "Switzerland", "id_type": "AHV"},
        {"code": "CHL", "name": "Chile", "id_type": "RUN"},
        {"code": "CHN", "name": "China", "id_type": "National ID"},
        {"code": "COL", "name": "Colombia", "id_type": "Cedula"},
        {"code": "CYP", "name": "Cyprus", "id_type": "National ID"},
        {"code": "CZE", "name": "Czech Republic", "id_type": "Birth Number"},
        {"code": "DEU", "name": "Germany", "id_type": "Tax ID"},
        {"code": "DNK", "name": "Denmark", "id_type": "CPR"},
        {"code": "ESP", "name": "Spain", "id_type": "DNI/NIE"},
        {"code": "EST", "name": "Estonia", "id_type": "Personal Code"},
        {"code": "FIN", "name": "Finland", "id_type": "HETU"},
        {"code": "FRA", "name": "France", "id_type": "INSEE"},
        {"code": "GBR", "name": "United Kingdom", "id_type": "NINO"},
        {"code": "GRC", "name": "Greece", "id_type": "AFM"},
        {"code": "HKG", "name": "Hong Kong", "id_type": "HKID"},
        {"code": "HRV", "name": "Croatia", "id_type": "OIB"},
        {"code": "HUN", "name": "Hungary", "id_type": "TAJ"},
        {"code": "IDN", "name": "Indonesia", "id_type": "NIK"},
        {"code": "IND", "name": "India", "id_type": "Aadhaar"},
        {"code": "IRL", "name": "Ireland", "id_type": "PPS"},
        {"code": "IRN", "name": "Iran", "id_type": "Melli Code"},
        {"code": "IRQ", "name": "Iraq", "id_type": "National ID"},
        {"code": "ISL", "name": "Iceland", "id_type": "Kennitala"},
        {"code": "ISR", "name": "Israel", "id_type": "Teudat Zehut"},
        {"code": "ITA", "name": "Italy", "id_type": "Codice Fiscale"},
        {"code": "JPN", "name": "Japan", "id_type": "My Number"},
        {"code": "KAZ", "name": "Kazakhstan", "id_type": "IIN"},
        {"code": "KOR", "name": "South Korea", "id_type": "RRN"},
        {"code": "KWT", "name": "Kuwait", "id_type": "Civil ID"},
        {"code": "LKA", "name": "Sri Lanka", "id_type": "NIC"},
        {"code": "LTU", "name": "Lithuania", "id_type": "Personal Code"},
        {"code": "LUX", "name": "Luxembourg", "id_type": "Matricule"},
        {"code": "LVA", "name": "Latvia", "id_type": "Personal Code"},
        {"code": "MAC", "name": "Macau", "id_type": "Resident ID"},
        {"code": "MDA", "name": "Moldova", "id_type": "IDNP"},
        {"code": "MEX", "name": "Mexico", "id_type": "CURP"},
        {"code": "MKD", "name": "North Macedonia", "id_type": "EMBG"},
        {"code": "MNE", "name": "Montenegro", "id_type": "JMBG"},
        {"code": "MYS", "name": "Malaysia", "id_type": "NRIC"},
        {"code": "NGA", "name": "Nigeria", "id_type": "NIN"},
        {"code": "NLD", "name": "Netherlands", "id_type": "BSN"},
        {"code": "NOR", "name": "Norway", "id_type": "Fodselsnummer"},
        {"code": "NPL", "name": "Nepal", "id_type": "Citizenship Number"},
        {"code": "NZL", "name": "New Zealand", "id_type": "IRD"},
        {"code": "PAK", "name": "Pakistan", "id_type": "CNIC"},
        {"code": "PHL", "name": "Philippines", "id_type": "PhilSys ID"},
        {"code": "PNG", "name": "Papua New Guinea", "id_type": "National ID"},
        {"code": "POL", "name": "Poland", "id_type": "PESEL"},
        {"code": "PRT", "name": "Portugal", "id_type": "CC"},
        {"code": "ROU", "name": "Romania", "id_type": "CNP"},
        {"code": "SGP", "name": "Singapore", "id_type": "NRIC"},
        {"code": "SMR", "name": "San Marino", "id_type": "National ID"},
        {"code": "SRB", "name": "Serbia", "id_type": "JMBG"},
        {"code": "SVK", "name": "Slovakia", "id_type": "Birth Number"},
        {"code": "SVN", "name": "Slovenia", "id_type": "EMSO"},
        {"code": "SWE", "name": "Sweden", "id_type": "Personnummer"},
        {"code": "THA", "name": "Thailand", "id_type": "National ID"},
        {"code": "TUR", "name": "Turkey", "id_type": "TC Kimlik"},
        {"code": "TWN", "name": "Taiwan", "id_type": "National ID"},
        {"code": "UKR", "name": "Ukraine", "id_type": "Tax Number"},
        {"code": "USA", "name": "United States", "id_type": "SSN"},
        {"code": "VEN", "name": "Venezuela", "id_type": "Cedula"},
        {"code": "ZAF", "name": "South Africa", "id_type": "RSA ID"},
        {"code": "ZWE", "name": "Zimbabwe", "id_type": "National ID"},
    ]


def get_supported_countries() -> List[Dict[str, str]]:
    """Get list of countries actually supported by the IDNumbers package"""
    return get_all_countries()


def validate_id_number(country_code_3digit: str, id_number: str) -> IDValidationResult:
    """Validate an ID number for a specific country using 3-digit country code"""
    try:
        # Clean the ID number
        cleaned_id = id_number.strip().replace(" ", "").replace("-", "")
        country_code_3digit_upper = country_code_3digit.upper()

        # Check if country is recognized
        all_countries = get_all_countries()
        country_info = next(
            (c for c in all_countries if c["code"] == country_code_3digit_upper), None
        )

        if not country_info:
            return IDValidationResult(
                is_valid=False,
                country_code=country_code_3digit_upper,
                id_number=cleaned_id,
                error_message=f"Country code {country_code_3digit_upper} not recognized. Use 3-digit country codes like USA, GBR, FRA, TWN, etc.",
            )

        # Use the country code directly as the module name
        module_path = f"idnumbers.nationalid.{country_code_3digit_upper}"

        try:
            module = importlib.import_module(module_path)
        except ImportError:
            return IDValidationResult(
                is_valid=False,
                country_code=country_code_3digit_upper,
                id_number=cleaned_id,
                error_message=f"Country module not found: {module_path}. Please ensure the IDNumbers package supports {country_info['name']}.",
            )

        # Validate using the module's NationalID class
        is_valid = module.NationalID.validate(cleaned_id)

        # Extract information if valid
        extracted_info = {}
        if is_valid:
            try:
                # Create NationalID instance for information extraction
                national_id = module.NationalID.parse(cleaned_id)
                extracted_info = {**national_id}

            except Exception as e:
                # If extraction fails, that's okay - we still have validation
                pass

        return IDValidationResult(
            is_valid=is_valid,
            country_code=country_code_3digit_upper,
            id_number=cleaned_id,
            extracted_info=extracted_info if extracted_info else None,
        )

    except Exception as e:
        return IDValidationResult(
            is_valid=False,
            country_code=country_code_3digit.upper(),
            id_number=id_number,
            error_message=f"Validation error: {str(e)}",
        )


@mcp.tool()
def list_supported_countries() -> List[Dict[str, str]]:
    """
    List all countries supported by the IDNumbers package.

    Returns:
        List of dictionaries containing country information with keys:
        - code: 3-digit country code
        - name: Country name
        - id_type: Type of national ID used
    """
    return get_supported_countries()


@mcp.tool()
def validate_national_id(country_code: str, id_number: str) -> Dict[str, Any]:
    """
    Validate a national ID number for a specific country.

    Args:
        country_code: 3-digit country code (e.g., 'USA', 'GBR', 'FRA')
        id_number: The ID number to validate

    Returns:
        Dictionary containing validation results:
        - is_valid: Boolean indicating if the ID is valid
        - country_code: The country code used
        - id_number: The cleaned ID number
        - extracted_info: Dictionary of extracted information (if available)
        - error_message: Error message if validation failed
    """
    result = validate_id_number(country_code, id_number)
    return {
        "is_valid": result.is_valid,
        "country_code": result.country_code,
        "id_number": result.id_number,
        "extracted_info": result.extracted_info,
        "error_message": result.error_message,
    }


@mcp.tool()
def parse_id_info(country_code: str, id_number: str) -> Dict[str, Any]:
    """
    Extract information from a valid national ID number.

    Args:
        country_code: 3-digit country code (e.g., 'USA', 'GBR', 'FRA')
        id_number: The ID number to extract information from

    Returns:
        Dictionary containing extracted information such as:
        - birth_date: Birth date (if extractable)
        - gender: Gender (if extractable)
        - age: Current age (if calculable)
        - place_of_birth: Place of birth (if extractable)
        - checksum: Checksum information (if available)
        - is_valid: Whether the ID is valid
    """
    result = validate_id_number(country_code, id_number)

    if not result.is_valid:
        return {
            "error": "Invalid ID number",
            "error_message": result.error_message,
            "is_valid": False,
        }

    return {
        "is_valid": True,
        "country_code": result.country_code,
        "id_number": result.id_number,
        "extracted_info": result.extracted_info or {},
    }


@mcp.tool()
def validate_multiple_ids(id_data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    Validate multiple national ID numbers at once.

    Args:
        id_data: List of dictionaries, each containing:
            - country_code: 3-digit country code
            - id_number: The ID number to validate

    Returns:
        List of validation results for each ID number
    """
    results = []
    for item in id_data:
        country_code = item.get("country_code", "")
        id_number = item.get("id_number", "")

        if not country_code or not id_number:
            results.append(
                {"error": "Missing country_code or id_number", "is_valid": False}
            )
            continue

        result = validate_id_number(country_code, id_number)
        results.append(
            {
                "is_valid": result.is_valid,
                "country_code": result.country_code,
                "id_number": result.id_number,
                "extracted_info": result.extracted_info,
                "error_message": result.error_message,
            }
        )

    return results


@mcp.tool()
def get_country_id_format(country_code: str) -> Dict[str, Any]:
    """
    Get information about the ID number format for a specific country.

    Args:
        country_code: 3-digit country code (e.g., 'USA', 'GBR', 'FRA')

    Returns:
        Dictionary containing format information for the country's ID system
    """
    countries = get_all_countries()
    country_info = next(
        (c for c in countries if c["code"] == country_code.upper()), None
    )

    if not country_info:
        return {
            "error": f"Country code {country_code} not recognized",
            "supported_countries": [c["code"] for c in get_supported_countries()],
        }

    # Basic format information
    format_info = {
        "country_code": country_code.upper(),
        "country_name": country_info["name"],
        "id_type": country_info["id_type"],
    }

    # Add specific format information for various countries
    format_details = {
        "USA": {
            "pattern": "XXX-XX-XXXX",
            "length": 9,
            "description": "Social Security Number",
        },
        "GBR": {
            "pattern": "XX123456X",
            "length": 9,
            "description": "National Insurance Number",
        },
        "FRA": {
            "pattern": "1234567890123",
            "length": 13,
            "description": "INSEE Number",
        },
        "BRA": {"pattern": "123.456.789-01", "length": 11, "description": "CPF Number"},
        "TWN": {
            "pattern": "X123456789",
            "length": 10,
            "description": "Taiwan National ID",
        },
        "CHN": {
            "pattern": "11010519491231002X",
            "length": 18,
            "description": "Chinese National ID",
        },
        "JPN": {"pattern": "1234 5678 9012", "length": 12, "description": "My Number"},
        "KOR": {
            "pattern": "123456-1234567",
            "length": 13,
            "description": "Resident Registration Number",
        },
    }

    if country_code.upper() in format_details:
        format_info.update(format_details[country_code.upper()])

    return format_info


if __name__ == "__main__":
    mcp.run(transport="stdio")
