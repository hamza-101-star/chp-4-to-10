def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    'ChatGPT', 'Assistant',
    age=3, 
    location='Online',
    favorite_language='Python'
)

print(my_profile)
