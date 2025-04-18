def test_set_differences():
    followers = {"a", "b", "c"}
    following = {"b", "c", "d"}

    not_back   = following - followers
    not_by_me  = followers - following

    assert not_back  == {"d"}
    assert not_by_me == {"a"}
