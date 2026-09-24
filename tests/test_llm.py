from unittest.mock import Mock, patch

from src.app.llm import ask_llm


def test_ask_llm_returns_response_text():
    fake_response = Mock()
    fake_response.output_text = "Test response"

    with patch("src.app.llm.client") as fake_client:
        fake_client.responses.create.return_value = fake_response

        result = ask_llm("Hello")

        fake_client.responses.create.assert_called_once_with(
            model="gpt-5-mini",
            input="Hello",
        )

    assert result == "Test response"