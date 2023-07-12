from mitmproxy import http
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
import cgi
import re
import io
import time

XML_OK_RESPONSE = '''<?xml version="1.0" encoding="UTF-8"?>
                    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
                    <plist version="1.0">
                    <dict>
                    <key>iPhone5,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone3,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone3,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone4,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad3,6</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,6</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad2,7</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPad4,6</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPod4,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPod5,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone5,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone5,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone5,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone6,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone6,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone8,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone8,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone8,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone9,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone9,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone9,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone9,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone10,6</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone11,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone11,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone11,6</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone11,8</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone12,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone12,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone12,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone13,1</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone13,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone13,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone13,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone14,2</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone14,3</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone14,4</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone14,5</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    <key>iPhone14,8</key>
                    <array>
                    <string>powerDiagnostics</string>
                    </array>
                    </dict>
                    </plist>'''

def request(flow: flow.Flow):
    path = flow.request.path
    print('Path is %s' % path)
    if path == '/ios/TestConfiguration/1.2':
        respond(flow, XML_OK_RESPONSE)
    elif path == '/MR3Server/ValidateTicket?ticket_number=000000':
        respond(flow, XML_OK_RESPONSE)
    elif path == '/MR3Server/MR3Post':
        save_content(flow, 'general')
        respond(flow, XML_OK_RESPONSE)
    elif path == '/ios/log/extendedUpload':
        save_content(flow, 'power')
        respond(flow, XML_OK_RESPONSE)

def save_content(flow: flow.Flow, prefix: str):
    decoded_data = io.BytesIO()
    decoded_data.write(flow.request.get_decoded_content())

    mime_type = flow.request.headers.get('Content-Type', '')
    multipart_boundary_re = re.compile('^multipart/form-data; boundary=(.*)$')
    matches = multipart_boundary_re.match(mime_type)

    decoded_data.seek(0)

    query = cgi.parse_multipart(decoded_data, {"boundary": matches.group(1)})

    with open("%s-%s.tar.gz" % (prefix, time.strftime("%Y%m%d-%H%M%S")), "wb") as logs:
        logs.write(query[b'log_archive'][0])

def respond(flow: flow.Flow, content: str):
    resp = HTTPResponse.make(
        200,
        content,
        Headers(Content_Type="text/xml")
    )
    flow.response = resp
