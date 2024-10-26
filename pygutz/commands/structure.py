HEXAGONAL_STRUCTURE = {
    "app" : {
        "core": [
            "__init__.py", 
            {
                "entities": [
                    "__init__.py", 
                    "models.py", 
                    "schemas.py"
                ], 
                "interfaces":[
                    "__init__.py", 
                    "services.py", 
                    "repositories.py"
                ]
            }
        ],
        "pkgs": [
            "__init__.py", 
            "logs.py", 
            "database.py", 
            "utils.py"
        ],
        "server": [
            "__init__.py", 
            "deps.py", 
            "middlewares.py", 
            {
                "routes": [
                        "__init__.py"
                    ]
            }
        ],
        "services": [
            "__init__.py"
        ],
        "repositoies":[
            "__init__.py"
        ],
        "main.py": [],
        "settings.py": [],
        "__init__.py": []
    },
    "tests": {
        "__init__.py":[]
    },
    ".gitignore": []
}