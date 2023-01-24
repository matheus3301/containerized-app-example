import os, platform

def get_os_info(): 
    return {
        "os": platform.platform(),
        "node-name": platform.node(),
        "architecture": platform.architecture()
    }