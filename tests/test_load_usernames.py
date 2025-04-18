import json
from comparar_instagram.cli import load_usernames


def _write(tmp_path, data, fname="sample.json"):
    p = tmp_path / fname
    p.write_text(json.dumps(data), encoding="utf-8")
    return p


def test_lista_plana(tmp_path):
    data = [
        {"string_list_data": [{"value": "user1"}]},
        {"string_list_data": [{"value": "user2"}]},
    ]
    f = _write(tmp_path, data)
    assert load_usernames(f) == {"user1", "user2"}


def test_dict_relationship_following(tmp_path):
    data = {
        "relationships_following": [
            {"string_list_data": [{"value": "alice"}]},
            {"string_list_data": [{"value": "bob"}]},
        ]
    }
    f = _write(tmp_path, data, "following.json")
    assert load_usernames(f) == {"alice", "bob"}
