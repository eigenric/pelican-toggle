from pelican_toggle.pelican_toggle import toggle_to_details


def test_toggle_to_details():
    # Create a sample generator object
    class MockGenerator:
        def __init__(self, articles):
            self.articles = articles

    # Create a sample article object
    class MockArticle:
        def __init__(self, content):
            self._content = content

    # Define the test input and expected output
    test_input = '<p>{% toggle %}Toggle content{% end_toggle %}</p>'
    expected_output = '<p><details><summary>Demostración</summary>Toggle content</details></p>'

    # Create a sample generator and article
    generator = MockGenerator([MockArticle(test_input)])

    # Call the function to be tested
    toggle_to_details(generator)

    # Check if the article content is updated correctly
    assert generator.articles[0]._content == expected_output
