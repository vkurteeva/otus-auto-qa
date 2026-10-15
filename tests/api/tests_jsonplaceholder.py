import pytest
from models.jsonplaceholder import PostCreateRequest, PostUpdateRequest, Response


@pytest.mark.parametrize(
    "post_id, exp_title, exp_user_id",
    [
        pytest.param(
            1,
            "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            1,
            id="post_id_1",
        ),
        pytest.param(2, "qui est esse", 1, id="post_id_2"),
        pytest.param(11, "et ea vero quia laudantium autem", 2, id="post_id_11"),
    ],
)
def test_get_single_post_by_id(api_client, post_id, exp_title, exp_user_id):
    res = api_client.get_post_by_id(post_id=post_id)

    assert res.id == post_id
    assert res.title == exp_title
    assert res.userId == exp_user_id
    assert isinstance(res.body, str)


@pytest.mark.parametrize(
    "query_params, exp_length, exp_user_id",
    [
        pytest.param({"userId": 1}, 10, 1, id="filter_by_user_1"),
        pytest.param({"userId": 5}, 10, 5, id="filter_by_user_5"),
    ],
)
def test_get_posts_list_filtering(api_client, query_params, exp_length, exp_user_id):
    user_id = query_params["userId"]
    res = api_client.get_posts(user_id=user_id)

    assert isinstance(res, list)
    assert len(res) == exp_length

    for post in res:
        assert post.userId == exp_user_id


def test_get_all_posts_structure(api_client):
    res = api_client.get_posts()

    assert isinstance(res, list)
    assert len(res) >= 100

    for post in res:
        assert isinstance(post.id, int)
        assert isinstance(post.title, str)


def test_create_post_success(api_client):
    payload = PostCreateRequest(title="QA Title", body="QA Body", userId=42)

    res = api_client.create_post(payload)

    assert res.id == 101
    assert res.title == "QA Title"
    assert res.userId == 42


def test_update_post_put_success(api_client):
    payload = PostCreateRequest(
        title="Just Changed Title", body="Updated Body", userId=1
    )
    res = api_client.update_post_put(post_id=1, post_data=payload)

    assert res.title == "Just Changed Title"
    assert res.body == "Updated Body"


def test_update_post_patch_success(api_client):
    payload = PostUpdateRequest(title="Just Changed Title2")
    res = api_client.update_post_patch(post_id=1, post_data=payload)

    assert res.title == "Just Changed Title2"


def test_delete_post_success(api_client):
    res = api_client.delete_post(post_id=1)

    assert res == {}


# def test_get_non_existent_post_returns_404(api_client):
#     with pytest.raises(AssertionError) as exc_info:
#         api_client.get(path="/posts/9999")
#
#     assert "API Error" in str(exc_info.value)
#
#
# def test_update_non_existent_post_returns_404(api_client):
#     payload = PostUpdateRequest(title="Ghost")
#
#     with pytest.raises(AssertionError) as exc_info:
#         api_client.update_post_patch(post_id=9999, post_data=payload)
#
#     assert "API Error" in str(exc_info.value)
