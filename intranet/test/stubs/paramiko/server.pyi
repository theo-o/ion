# Stubs for paramiko.server (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import threading

class ServerInterface:
    def check_channel_request(self, kind, chanid): ...
    def get_allowed_auths(self, username): ...
    def check_auth_none(self, username): ...
    def check_auth_password(self, username, password): ...
    def check_auth_publickey(self, username, key): ...
    def check_auth_interactive(self, username, submethods): ...
    def check_auth_interactive_response(self, responses): ...
    def check_auth_gssapi_with_mic(self, username, gss_authenticated=..., cc_file=None): ...
    def check_auth_gssapi_keyex(self, username, gss_authenticated=..., cc_file=None): ...
    def enable_auth_gssapi(self): ...
    def check_port_forward_request(self, address, port): ...
    def cancel_port_forward_request(self, address, port): ...
    def check_global_request(self, kind, msg): ...
    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes): ...
    def check_channel_shell_request(self, channel): ...
    def check_channel_exec_request(self, channel, command): ...
    def check_channel_subsystem_request(self, channel, name): ...
    def check_channel_window_change_request(self, channel, width, height, pixelwidth, pixelheight): ...
    def check_channel_x11_request(self, channel, single_connection, auth_protocol, auth_cookie, screen_number): ...
    def check_channel_forward_agent_request(self, channel): ...
    def check_channel_direct_tcpip_request(self, chanid, origin, destination): ...
    def check_channel_env_request(self, channel, name, value): ...

class InteractiveQuery:
    name = ... # type: Any
    instructions = ... # type: Any
    prompts = ... # type: Any
    def __init__(self, name='', instructions='', *prompts): ...
    def add_prompt(self, prompt, echo=True): ...

class SubsystemHandler(threading.Thread):
    def __init__(self, channel, name, server): ...
    def get_server(self): ...
    def start_subsystem(self, name, transport, channel): ...
    def finish_subsystem(self): ...
