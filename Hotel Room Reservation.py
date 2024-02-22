import requests
from xml.etree import ElementTree as ET

# Define the SOAP request XML template
soap_request_template = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hot="http://hotel.example.com">
   <soapenv:Header/>
   <soapenv:Body>
      <hot:BookingRequest>
         <hot:CheckInDate>{check_in_date}</hot:CheckInDate>
         <hot:CheckOutDate>{check_out_date}</hot:CheckOutDate>
         <hot:RoomType>{room_type}</hot:RoomType>
         <!-- Other booking information -->
      </hot:BookingRequest>
   </soapenv:Body>
</soapenv:Envelope>"""

# Define booking information
booking_info = {
    'check_in_date': '2024-03-01',
    'check_out_date': '2024-03-05',
    'room_type': 'single'
    # You can add other booking information here
}

# Build the SOAP request message
soap_request = soap_request_template.format(**booking_info)

# Set the request headers
headers = {'Content-Type': 'text/xml'}

# Send the SOAP request to the hotel booking system URL
url = 'http://hotel.example.com/booking'
response = requests.post(url, data=soap_request, headers=headers)

# Parse the server response
if response.status_code == 200:
    # Parse the SOAP response XML
    root = ET.fromstring(response.content)
    # Parse the booking result
    booking_result = root.find('.//{http://hotel.example.com}BookingResult').text
    print("Booking Result:", booking_result)
else:
    print("Request Failed:", response.status_code)