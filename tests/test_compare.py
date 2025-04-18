from comparar_instagram.cli import extract_usernames
def test_extract_simple():
    data = [{"string_list_data": [{"value": "pepe"}]}]
    assert extract_usernames(data) == {"pepe"}