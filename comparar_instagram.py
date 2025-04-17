import json
import os

def load_usernames(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    usernames = set()

    # Si es un dict, asumimos que es 'following.json' con clave 'relationships_following'
    if isinstance(data, dict):
        for key in ['relationships_following', 'relationships_followers']:
            if key in data:
                data = data[key]

    # Ahora esperamos una lista de objetos con string_list_data
    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and "string_list_data" in entry:
                string_data = entry["string_list_data"]
                if isinstance(string_data, list) and len(string_data) > 0:
                    value = string_data[0].get("value")
                    if value:
                        usernames.add(value)

    return usernames

def main_console():
    downloads = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    followers_file = os.path.join(downloads, 'followers_1.json')
    following_file = os.path.join(downloads, 'following.json')

    followers = load_usernames(followers_file)
    following = load_usernames(following_file)

    not_following_back = following - followers
    not_followed_by_me = followers - following

    print("🔴 Usuarios a los que sigo y que NO me siguen de vuelta:")
    for user in sorted(not_following_back):
        print("  -", user)

    print("\n🟢 Usuarios que me siguen y que YO no sigo de vuelta:")
    for user in sorted(not_followed_by_me):
        print("  -", user)

if __name__ == '__main__':
    main_console()
