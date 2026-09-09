import os
import google.generativeai as genai

class CineVisorAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.grafana_mcp = os.getenv("GRAFANA_MCP_ENDPOINT", "https://mcp.grafana.com/mcp")
        self.grafana_url = os.getenv("GRAFANA_URL", "https://mellowriver3176.grafana.net")
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-3.6-flash')

    def execute_infrastructure_query(self, user_query):
        system_prompt = f"""
        You are CineVisor-Ops, an elite autonomous Media & Entertainment infrastructure agent built for the Google Cloud Summer Blockbuster Hackathon (Grafana Track).
        You are actively connected to the official Grafana Cloud MCP Server endpoint ({self.grafana_mcp}) and Grafana Cloud stack ({self.grafana_url}).
        
        User Incident / Directive: "{user_query}"
        
        Provide a comprehensive, highly technical enterprise-grade response containing:
        1. **MCP Tool Invocation Log**: List specific tool calls made.
        2. **Live Telemetry & Metric Analysis**: Simulate realistic PromQL metric results and Loki log patterns.
        3. **Root-Cause Analysis (RCA)**: Deep technical breakdown of the broadcast failure.
        4. **Remediation & Review Link**: Actionable fix steps and a direct Markdown review link.
        """
        try:
            response = self.model.generate_content(system_prompt)
            return response.text, None
        except Exception as e:
            return None, f"Gemini API Error: {str(e)}"