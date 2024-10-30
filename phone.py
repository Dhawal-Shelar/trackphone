import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def track_number(number, country):
    print("Phase-two: Tracking number")

    # Get the country code using the provided country abbreviation
    get_country = track_countrycode(country)

    if not get_country:  # Handle case if the country code is not found
        return {"error": f"No country found for {country}"}

    # Construct the complete number with country code
    new_number = get_country + str(number)

    try:
        # Parse the phone number with the country code
        parsed_number = phonenumbers.parse(new_number)

        # Get location (country or region)
        location = geocoder.description_for_number(parsed_number, 'en')

        # Get service provider
        service_provider = carrier.name_for_number(parsed_number, 'en')

        # Get time zones
        time_zones = timezone.time_zones_for_number(parsed_number)

        print(f"Location: {location}")
        print(f"Service Provider: {service_provider}")
        print(f"Time Zones: {time_zones}")

        return {
            "location": location,
            "service_provider": service_provider,
            "time_zones": list(time_zones)
        }

    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")
        return {"error": "Invalid phone number"}

def track_countrycode(country):
    print("Phase-three: Retrieving country code")
    
    # Dictionary to map country codes
    list_country = {
        "IND": "+91",
        "USA": "+1"
    }

    # Return the country code if found, otherwise return None
    return list_country.get(country)