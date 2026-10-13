from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Send successful HTTP header response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # Enable CORS so the game client doesn't block the request
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()

        # 2. Check what the game client is asking for based on the URL path
        path = self.path.lower()
        
        # Simulated Network Handshake (Example: User Login/Auth)
        if "login" in path or "auth" in path or "status" in path:
            response_data = {
                "status": "success",
                "message": "Connected to Custom 2K Server Revival Backend",
                "online": True
            }
        
        # Simulated Roster Request (Example: Game asking for roster data)
        elif "roster" in path:
            response_data = {
                "roster_name": "2K Revival Custom Roster 2027",
                "version": "1.0",
                "players_updated": 450,
                "data": "Your roster matrix array values go here"
            }
            
        # Default fallback response for any other URL the game pings
        else:
            response_data = {
                "status": "online",
                "info": f"Server received custom ping at path: {self.path}"
            }

        # 3. Convert Python dictionary to JSON string text and send it back to the game
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return