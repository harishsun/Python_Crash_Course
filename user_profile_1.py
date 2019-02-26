def build_profile(first, last, **use_info):
    """Build a dictionary containing everything you know about user!!"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in use_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'harish', 'sun', location='brentwood', field='systems')

print(user_profile)
