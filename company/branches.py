#branch dictionary
BRANCHES = { 
    "MNL": {"city": "Manila", "country": "Philippines", "tz": "PHT", "offset": 8}, 
    "TYO": {"city": "Tokyo", "country": "Japan", "tz": "JST", "offset": 9}, 
    "DXB": {"city": "Dubai", "country": "United Arab Emirates", "tz": "GST", "offset": 4}, 
    "BOM": {"city": "Mumbai", "country": "India", "tz": "IST", "offset": 5.5},
} 

#employee dictionary
EMPLOYEES = { 
    "juan": {"password": "mnl123", "name": "Juan Dela Cruz", "branch": "MNL"}, 
    "yuki": {"password": "tyo123", "name": "Yuki Tanaka", "branch": "TYO"}, 
    "omar": {"password": "dxb123", "name": "Omar Haddad", "branch": "DXB"}, 
} 

#returns branch dictionary
def get_branch(code):
    """Return the branch dictionary for the given code, or None if not found."""
    return BRANCHES.get(code)

#returns branch code or branch index
def get_branch_codes():
    """Return a list of all branch codes."""
    return list(BRANCHES.keys())
